import os
from flask import Flask, render_template, render_template_string, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
from PIL import Image
import pytesseract
import imghdr

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png']
app.config['UPLOAD_PATH'] = 'uploads'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or file_ext != validate_image(uploaded_file.stream):
            abort(400, description="Invalid file type")

        file_path = os.path.join(app.config['UPLOAD_PATH'], filename)
        uploaded_file.save(file_path)
    
        text = pytesseract.image_to_string(Image.open(file_path))
        os.remove(file_path)
    return render_template_string(f"<h3>{text}</h3>")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)