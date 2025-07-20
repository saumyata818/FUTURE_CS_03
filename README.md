# 🔐 Secure File Sharing System

A simple and secure web application built with Flask that allows users to upload and download files with AES encryption. Developed as part of **Future Interns - Cyber Security Task 3** by **Saumyata Nepal**.

---

## 📁 Project Structure

secure_file_sharing/
├── app.py # Main Flask application
├── encryption.py # AES encryption and decryption logic
├── templates/
│ └── index.html # Frontend for file upload/download
├── uploads/ # Stores encrypted uploaded files
├── downloads/ # Stores decrypted files for download



---

## 🔧 Features

- 📤 Secure file upload with AES encryption (AES-256 in CBC mode)  
- 🔐 Unique random key and IV generated for each file  
- 🔑 Downloadable encryption key for secure key management  
- 📥 Secure file download with automatic decryption  
- 🧼 Auto-deletion of decrypted files after download for enhanced security  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/secure_file_sharing.git
cd secure_file_sharing
2. Install dependencies
Make sure you have Python 3 installed.

bash
pip install flask pycryptodome
3. Run the application
bash
python app.py
Open your browser and go to:
http://127.0.0.1:5000
🔐 Encryption Details
Algorithm: AES (Advanced Encryption Standard)

Mode: CBC (Cipher Block Chaining)

Key Size: 256 bits (32 bytes)

Library Used: PyCryptodome

📸 Screenshots
You can add screenshots here such as:

Homepage 
![task 3 1](https://github.com/user-attachments/assets/c74d3a08-2e86-4c7f-91d2-19fef89dc7bd)





Flask app running on localhost:
![task 3 2 1](https://github.com/user-attachments/assets/19ebbc66-8046-4a94-9f48-99a2f32822d0)



Encryption key download prompt
<img width="1718" height="912" alt="image" src="https://github.com/user-attachments/assets/d1ed655d-ea21-4b4f-929e-15c2680ca478" />










🧑‍💻 Developed by
Saumyata Nepal
Intern @ Future Interns
Task: Cyber Security Task 3 - Secure File Sharing System

LinkedIn: https://www.linkedin.com/in/saumyata-nepal-1818a5312/

📄 License
This project is for educational use only and not intended for production deployment.

