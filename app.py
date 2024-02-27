import os
from flask import Flask, render_template, request, send_file
from lib.cipherDriver import encryptCipher, decryptCipher, fileHandler
import base64
import io

app = Flask(__name__)

fileBytes = None
fileExtension = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global fileBytes, fileExtension
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
                
                cipherText = cipherText.encode('utf-8')
                cipherText = base64.b64encode(cipherText)
                cipherText = cipherText.decode('utf-8')
            else:
                cipherText = plainText.encode('utf-8')
                cipherText = base64.b64decode(plainText)
                cipherText = cipherText.decode('utf-8')
                cipherText = decryptCipher(cipherType, cipherText=cipherText, key=key, a=a, b=b)
            
            return render_template('index.html', cipherText=cipherText, plainText=plainText, cipherType=cipherType, key=key, a=a, b=b, isFileInput=False)
        else:
            file = request.files['file']
            # turning file into bytes and then into string
            fileData = fileHandler(file)
            cipherType = request.form.get('cipherType')
            key = request.form.get('key')
            key = key.replace(' ', '')

            print(fileData.encode('utf-8'))

            cipherText = ""

            if (request.form.get('action') == 'encrypt'):
                fileData = encryptCipher(cipherType, plainText=fileData, key=key, a=0, b=0)
                fileBytes = fileData.encode('utf-8')
                cipherText = fileData
            else:
                fileData = decryptCipher(cipherType, cipherText=fileData, key=key, a=0, b=0)
                print("\n\n\n\n ----------------------------", fileData)
                fileBytes = fileData
                cipherText = fileData


            originalFileName = file.filename
            fileName = os.path.splitext(originalFileName)[0]
            fileExtension = os.path.splitext(originalFileName)[1]


            return render_template('index.html', fileData=fileData, cipherText=cipherText, cipherType=cipherType, key=key, m=0, b=0, fileName=fileName, fileExtension=fileExtension, isFileInput=True)
    return render_template('index.html')

@app.route('/download')
def download_file():
    global fileBytes
    global fileExtension
    print("fileBytes: ", fileBytes)
    print("fileExtension: ", fileExtension)
    file = io.BytesIO(fileBytes.encode("utf-8"))
    return send_file(file, as_attachment=True, download_name="encrypted" + fileExtension)