# RemoveBg using Python, Flask

RemoveBg is a web application built with Python and Flask that allows users to remove backgrounds from images. It supports two main actions: downloading processed images as a ZIP file or saving them directly to a MySQL database.

## Features

- **Upload Images**: Users can upload JPG or PNG images to be processed.
- **Remove Background**: Uses the Rembg library to remove backgrounds from uploaded images.
- **Download**: Option to download processed images as a ZIP file.
- **Save to MySQL**: Option to save processed images to a MySQL database.
- **Flash Messages**: Displays success messages after images are processed.

## Technologies Used

- Python
- Flask
- Rembg
- MySQL

## Setup

Follow these steps to set up and run the RemoveBg application locally:

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd RemoveBg
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:

   Create a `.env` file in the root directory with the following variables:

   ```plaintext
   MYSQL_HOSTNAME=your_mysql_hostname
   MYSQL_USERNAME=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DATABASE=remove_bg
   ```

   Replace `your_mysql_hostname`, `your_mysql_username`, and `your_mysql_password` with your MySQL server details.

4. **Initialize the database**:

   Ensure your MySQL server is running. The application will create the necessary table (`images`) automatically on startup.

5. **Run the application**:

   ```bash
   python app.py
   ```

   Open your web browser and go to `http://localhost:5000` to access the RemoveBg application.

## Usage

1. **Upload Images**:

   - Click on the "Choose File" button and select one or more JPG or PNG images.
   - Select an action: "Download ZIP" or "Save to MySQL".
   - Click the "Process" button.

2. **Download ZIP**:

   - If you select "Download ZIP", a ZIP file containing processed images without backgrounds will be downloaded.

3. **Save to MySQL**:

   - If you select "Save to MySQL", processed images will be saved directly to the MySQL database.

4. **View Flash Messages**:
   - After processing, a success message will appear indicating the successful download or save operation.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

- **Maintainer**: @CHIRANJEEVICHETAN
- **Email**: chiranjeevichetan1998@gmail.com

Feel free to reach out if you have any questions or feedback about the project.
