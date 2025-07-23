from flask import Flask, request, send_file, render_template
from werkzeug.utils import secure_filename
import os
from crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = secure_filename(file.filename)
    encrypted = encrypt_file(file.read())

    with open(os.path.join(UPLOAD_FOLDER, filename + '.enc'), 'wb') as f:
        f.write(encrypted)

    return 'File uploaded and encrypted successfully.'

@app.route('/download/<filename>')
def download(filename):
    path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(path):
        return 'File not found', 404

    with open(path, 'rb') as f:
        decrypted = decrypt_file(f.read())

    temp_path = os.path.join(UPLOAD_FOLDER, 'temp_' + filename.replace('.enc', ''))
    with open(temp_path, 'wb') as temp:
        temp.write(decrypted)

    return send_file(temp_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
