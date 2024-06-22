import os
from rembg import remove
from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import io
import zipfile
import mysql.connector
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Required for flashing messages

# MySQL connection configuration
mysql_config = {
    'host': os.getenv('MYSQL_HOSTNAME'),
    'user': os.getenv('MYSQL_USERNAME'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
}

# Function to get a MySQL connection
def get_mysql_connection():
    return mysql.connector.connect(**mysql_config)

# Ensure the table exists
def create_images_table():
    conn = get_mysql_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            data LONGBLOB NOT NULL
        )
    """)
    conn.commit()
    conn.close()

create_images_table()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_images():
    temp_dir = 'temp_images'
    os.makedirs(temp_dir, exist_ok=True)
    files = request.files.getlist('images')
    action = request.form.get('action')

    for file in files:
        img_data = file.read()
        output_data = remove(img_data)

        filename = file.filename

        output_path = os.path.join(temp_dir, filename)
        with open(output_path, 'wb') as f:
            f.write(output_data)

    if action == 'download':
        # Create zip file
        zip_path = "processedImages/processed_files.zip"
        with zipfile.ZipFile(zip_path, 'w') as zip_file:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.basename(file_path))

        # Clean up the temporary directory
        for root, _, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(temp_dir)

        flash('Images downloaded successfully!', 'success')
        return send_file(zip_path, as_attachment=True)
    elif action == 'save':
        # Save processed images to MySQL
        conn = get_mysql_connection()
        cursor = conn.cursor()

        for file in os.listdir(temp_dir):
            with open(os.path.join(temp_dir, file), 'rb') as f:
                img_data = f.read()
                filename = file
                cursor.execute("INSERT INTO images (filename, data) VALUES (%s, %s)", (filename, img_data))

        conn.commit()
        conn.close()

        # Clean up the temporary directory
        for root, _, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        os.rmdir(temp_dir)

        flash('Images saved to MySQL successfully!', 'success')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
