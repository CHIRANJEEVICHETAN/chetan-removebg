import os
from rembg import remove
from flask import Flask, render_template, request, send_file
import io
import zipfile

app = Flask(__name__)

app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)