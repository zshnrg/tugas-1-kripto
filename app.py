from flask import Flask, render_template, request, redirect, url_for, flash, session
from lib.cipherDriver import encryptCipher, decryptCipher, fileHandler

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        isFileInput = request.form.get('isFileInput')
        print("isFileInput: ", isFileInput, "action: ", request.form.get('action'))
        if isFileInput == None:
            
            plainText = request.form.get('plainText')
            cipherType = request.form.get('cipherType')
            key = request.form.get('key')
            m = 0
            b = 0
            if cipherType == 'affine':
                m = int(request.form.get('affineMKey'))
                b = int(request.form.get('affineBKey'))

            if (request.form.get('action') == 'encrypt'):
                cipherText = encryptCipher(cipherType, plaintext=plainText, key=key, m=m, b=b)
            else:
                cipherText = decryptCipher(cipherType, ciphertext=plainText, key=key, m=m, b=b)
            
            print(cipherText)
            return render_template('index.html', cipherText=cipherText, plainText=plainText, cipherType=cipherType, key=key, m=m, b=b, isFileInput=isFileInput)
        else:
            file = request.files['file']
            file_data = fileHandler(file)
            cipherType = request.form.get('cipherType')
            key = request.form.get('key')
            if cipherType == 'affine':
                m = int(request.form.get('affineMKey'))
                b = int(request.form.get('affineBKey'))

            print(file_data)

            # if (request.form.get('action') == 'encrypt'):
            #     encrypt(
            #         cipher_type,
            #         file_data,
            #         key,
            #         m,
            #         b,
            #     )
            # else:
            #     decrypt(
            #         cipher_type,
            #         file_data,
            #         key,
            #         m,
            #         b,
            #     )        
        # Perform any necessary processing
        
        # For demonstration purposes, just print the form data
    return render_template('index.html')