import os
from flask import Flask, render_template, request, send_file
from lib.cipherDriver import encryptCipher, decryptCipher
import base64
import io

app = Flask(__name__)

fileData = None
isEncrypt = None
cipherType = None
originalFileName = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global fileData, isEncrypt, cipherType, originalFileName

    # print all the request data
    print(request.form)
    print(request.files)

    if request.method == 'POST':
        
        isFileInput = request.form.get('isFileInput')
        print("isFileInput: ", isFileInput, "action: ", request.form.get('action'))
        if isFileInput == None:
            
            plainText = request.form.get('plainText')
            cipherType = request.form.get('cipherType')
            key = request.form.get('key')
            a = 0
            b = 0
            if cipherType == 'affine' or cipherType == 'product':
                a = int(request.form.get('aKey'))
                b = int(request.form.get('bKey'))
            if cipherType != 'product':
                key = key.replace(' ', '')

            # Validating input
            if cipherType == 'affine':
                if a % 2 == 0 or a % 13 == 0:
                    return render_template('index.html', cipherText="Invalid key, multiplier must be relatively prime with 26", plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)
                
            if plainText == '':
                return render_template('index.html', cipherText="Invalid plain text, plain text cannot be empty", plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)
            
            if key == '':
                return render_template('index.html', cipherText="Invalid key, key cannot be empty", plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)

            isEncrypt = request.form.get('action')
            if isEncrypt == 'encrypt':
                cipherText = encryptCipher(cipherType, plainText=plainText, key=key, a=a, b=b)
                if cipherText == "Invalid cipher":
                    return render_template('index.html', cipherText=cipherText, plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)
                
                cipherText = cipherText.encode()
                cipherText = base64.b64encode(cipherText)
                cipherText = cipherText.decode()
            else:
                cipherText = plainText.encode()
                cipherText = base64.b64decode(plainText)
                cipherText = cipherText.decode()
                cipherText = decryptCipher(cipherType, cipherText=cipherText, key=key, a=a, b=b)
            
            return render_template('index.html', cipherText=cipherText, plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)
        else:
            file = request.files['file']
            cipherType = request.form.get('cipherType')
            key = request.form.get('key')
            key = key.replace(' ', '')
            a = 0
            b = 0
            if cipherType == 'affine' or cipherType == 'product':
                a = int(request.form.get('aKey'))
                b = int(request.form.get('bKey'))
            if cipherType != 'product':
                key = key.replace(' ', '')                

            # Validating input
            if cipherType == 'affine':
                if a % 2 == 0 or a % 13 == 0:
                    return render_template('index.html', fileData=file, cipherText="Invalid key, multiplier must be relatively prime with 26", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)
            
            if key == '':
                return render_template('index.html', fileData=file, cipherText="Invalid key, key cannot be empty", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)

            if file:
                isEncrypt = request.form.get('action')
                if (isEncrypt == 'encrypt'):
                    if cipherType != 'extendedVigenere' and cipherType != 'autokey':
                        # filtering non-alphabet characters
                        fileContent = file.read().decode()
                        fileContent =  ''.join([i for i in fileContent if i.isalpha()])
                    else:
                        fileContent = base64.b64encode(file.read()).decode()
                        # adding original file name and extension in the beginning of the file as metadata separated unique character '|'
                        originalFileName = file.filename + '|'
                        fileContent = originalFileName + fileContent

                    fileData = encryptCipher(cipherType, plainText=fileContent, key=key, a=0, b=0)
                    if fileData == "Invalid cipher":
                        return render_template('index.html', fileData=fileData, cipherText="Invalid cipher", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)
                    
                    fileData = fileData.encode()

                    cipherText = base64.b64encode(fileData)
                    cipherText = cipherText.decode()

                else:
                    if cipherType != 'extendedVigenere' and cipherType != 'autokey':
                        fileContent = file.read().decode()
                        fileContent =  ''.join([i for i in fileContent if i.isalpha()])
                    else:
                        fileContent = file.read().decode()

                    print("----------------------")
                    print(originalFileName)

                    fileData = decryptCipher(cipherType, cipherText=fileContent, key=key, a=0, b=0)
                    if fileData == "Invalid cipher":
                        return render_template('index.html', fileData=fileData, cipherText="Invalid cipher", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)

                    if cipherType != 'extendedVigenere' and cipherType != 'autokey':
                        fileData = fileData.encode()
                    else:
                        print(fileData)
                        fileData = fileData.split('|')
                        originalFileName = fileData[0]
                        fileData = fileData[1]
                        fileData = base64.b64decode(fileData)
                        
                    cipherText = fileData
            else:
                return render_template('index.html', fileData=fileData, cipherText="No file uploaded", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)


            fileName = os.path.splitext(originalFileName)[0]
            fileExtension = os.path.splitext(originalFileName)[1]
            return render_template('index.html', fileData=fileData, cipherText=cipherText, cipherType=cipherType, key=key, m=0, b=0, fileName=fileName, fileExtension=fileExtension, isFileInput=True)
    return render_template('index.html')

@app.route('/download')
def download_file():
    global fileData, isEncrypt, cipherType, originalFileName
    if fileData == None:
        return render_template('index.html', cipherText="No file uploaded", isFileInput=True)
    
    if isEncrypt == 'encrypt':
        file = io.BytesIO(fileData)
        return send_file(file, as_attachment=True, download_name="encrypted.hts")
    else:
        file = io.BytesIO(fileData)
        if cipherType != 'extendedVigenere' and cipherType != 'autokey':
            return send_file(file, as_attachment=True, download_name="decrypted.txt")
        else:
            return send_file(file, as_attachment=True, download_name=originalFileName)