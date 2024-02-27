import os
from flask import Flask, render_template, request, send_file
from lib.cipherDriver import encryptCipher, decryptCipher
import base64
import io

app = Flask(__name__)

fileData = None
fileName = None
fileExtension = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global fileData, fileName, fileExtension
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
                

            if request.form.get('action') == 'encrypt':
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

            if file:

                if (request.form.get('action') == 'encrypt'):
                    fileContent = base64.b64encode(file.read()).decode()

                    fileData = encryptCipher(cipherType, plainText=fileContent, key=key, a=0, b=0)
                    if fileData == "Invalid cipher":
                        return render_template('index.html', fileData=fileData, cipherText="Invalid cipher", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)
                    
                    fileData = fileData.encode()

                    cipherText = base64.b64encode(fileData)
                    cipherText = cipherText.decode()

                else:
                    fileContent = file.read().decode()

                    fileData = decryptCipher(cipherType, cipherText=fileContent, key=key, a=0, b=0)
                    if fileData == "Invalid cipher":
                        return render_template('index.html', fileData=fileData, cipherText="Invalid cipher", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)

                    fileData = base64.b64decode(fileData)
                    cipherText = fileData

                originalFileName = file.filename
                fileName = os.path.splitext(originalFileName)[0]
                fileExtension = os.path.splitext(originalFileName)[1]
            else:
                return render_template('index.html', fileData=fileData, cipherText="No file uploaded", cipherType=cipherType, key=key, m=0, b=0, isFileInput=True)

            return render_template('index.html', fileData=fileData, cipherText=cipherText, cipherType=cipherType, key=key, m=0, b=0, fileName=fileName, fileExtension=fileExtension, isFileInput=True)
    return render_template('index.html')

@app.route('/download')
def download_file():
    global fileData, fileExtension, fileName
    if fileData == None:
        return render_template('index.html', cipherText="No file uploaded", isFileInput=True)
    file = io.BytesIO(fileData)
    return send_file(file, as_attachment=True, download_name=fileName + "_encrypted" + fileExtension)