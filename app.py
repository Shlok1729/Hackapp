<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
import uuid
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = r"C:\Users\shlok\OneDrive\Desktop\Hack 5.0\multiple" # Change this to your desired folder
DATA_FILE = r'C:\Users\shlok\OneDrive\Desktop\Hack 5.0\users data\data.json'  # File to store user details
EXCEL_FILE = r'C:\Users\shlok\OneDrive\Desktop\Hack 5.0\users data\resume_data.xlsx'  # Excel file to store user details
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)
if not os.path.exists(EXCEL_FILE):
    pd.DataFrame(columns=["name", "mobile", "email", "file_path"]).to_excel(EXCEL_FILE, index=False)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return '''
    <html>
    <head>
        <title>Resume Upload</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
            form { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px gray; display: inline-block; }
            input, button { margin: 10px; padding: 10px; width: 90%; }
            button { background: #28a745; color: white; border: none; cursor: pointer; }
            button:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h2>Upload Your Resume</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="text" name="name" placeholder="Full Name" required><br>
            <input type="text" name="mobile" placeholder="Mobile Number" required><br>
            <input type="email" name="email" placeholder="Email ID" required><br>
            <input type="file" name="file" required><br>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    file = request.files['file']

    if not name or not mobile or not email:
        return 'Please fill in all details.'
    if 'file' not in request.files:
        return 'No file part'
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        unique_id = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_id + os.path.splitext(file.filename)[1])
        file.save(filepath)
        
        # Save details to JSON file
        with open(DATA_FILE, 'r+') as f:
            data = json.load(f)
            data.append({"name": name, "mobile": mobile, "email": email, "file_path": filepath})
            f.seek(0)
            json.dump(data, f, indent=4)
        
        # Save details to Excel file
        df = pd.read_excel(EXCEL_FILE)
        new_entry = pd.DataFrame([{"Name": name, "Mobile": mobile, "Email": email, "File Path": filepath}])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        
        return f'Thank you {name}! Your resume has been uploaded successfully.'
    else:
        return 'Invalid file format. Only PDF and DOCX allowed.'

@app.route('/resumes', methods=['GET'])
def list_resumes():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

=======
from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
import uuid
import pandas as pd

app = Flask(__name__)
UPLOAD_FOLDER = r"C:\Users\shlok\OneDrive\Desktop\Hack 5.0\multiple" # Change this to your desired folder
DATA_FILE = r'C:\Users\shlok\OneDrive\Desktop\Hack 5.0\users data\data.json'  # File to store user details
EXCEL_FILE = r'C:\Users\shlok\OneDrive\Desktop\Hack 5.0\users data\resume_data.xlsx'  # Excel file to store user details
ALLOWED_EXTENSIONS = {'pdf', 'docx'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)
if not os.path.exists(EXCEL_FILE):
    pd.DataFrame(columns=["name", "mobile", "email", "file_path"]).to_excel(EXCEL_FILE, index=False)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return '''
    <html>
    <head>
        <title>Resume Upload</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; padding: 50px; }
            form { background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px gray; display: inline-block; }
            input, button { margin: 10px; padding: 10px; width: 90%; }
            button { background: #28a745; color: white; border: none; cursor: pointer; }
            button:hover { background: #218838; }
        </style>
    </head>
    <body>
        <h2>Upload Your Resume</h2>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="text" name="name" placeholder="Full Name" required><br>
            <input type="text" name="mobile" placeholder="Mobile Number" required><br>
            <input type="email" name="email" placeholder="Email ID" required><br>
            <input type="file" name="file" required><br>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    file = request.files['file']

    if not name or not mobile or not email:
        return 'Please fill in all details.'
    if 'file' not in request.files:
        return 'No file part'
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        unique_id = str(uuid.uuid4())
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_id + os.path.splitext(file.filename)[1])
        file.save(filepath)
        
        # Save details to JSON file
        with open(DATA_FILE, 'r+') as f:
            data = json.load(f)
            data.append({"name": name, "mobile": mobile, "email": email, "file_path": filepath})
            f.seek(0)
            json.dump(data, f, indent=4)
        
        # Save details to Excel file
        df = pd.read_excel(EXCEL_FILE)
        new_entry = pd.DataFrame([{"Name": name, "Mobile": mobile, "Email": email, "File Path": filepath}])
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        
        return f'Thank you {name}! Your resume has been uploaded successfully.'
    else:
        return 'Invalid file format. Only PDF and DOCX allowed.'

@app.route('/resumes', methods=['GET'])
def list_resumes():
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

>>>>>>> 69e1e0d (Initial commit with dependencies)
