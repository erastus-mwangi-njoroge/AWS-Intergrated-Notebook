# Notepad Application

This is a professional notepad application developed using Python and the Tkinter library. The application allows users to create new files, open existing files, and save files. It also integrates with AWS S3 to enable users to upload their files to the cloud.

## Features

- Create new files
- Open existing files
- Save files
- Upload files to AWS S3

## Usage

1. Run the application by executing the `notepad.py` file.
2. The application window will open with a text area.
3. Use the "File" menu to create a new file, open an existing file, or save the current file.
4. To upload a file to AWS S3, make sure you have valid AWS credentials set as environment variables (`AWS_ACCESS_KEY` and `AWS_SECRET_KEY`).
5. Select the "Save" option from the "File" menu to save the file and upload it to AWS S3.

## Dependencies

- Python 3.x
- Tkinter
- boto3

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
