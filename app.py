from flask import Flask, render_template, request, send_file
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "downloads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    encrypted_path = encrypt_file(filepath)

    # Return only the encrypted filename to avoid path issues
    encrypted_filename = os.path.basename(encrypted_path)
    return f"✅ File uploaded and encrypted: <b>{encrypted_filename}</b><br><br>Copy this filename and paste it in the download section to decrypt."

@app.route('/download', methods=['POST'])
def download():
    filename = request.form['filename']

    # Join upload path with user input filename
    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)

    # Check if file exists before attempting decryption
    if not os.path.exists(encrypted_path):
        return f"❌ File not found: {filename}", 404

    decrypted_path = decrypt_file(encrypted_path)

    # Send decrypted file back to user
    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
