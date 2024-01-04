import os
import tkinter as tk
from tkinter import filedialog
import boto3
from botocore.exceptions import NoCredentialsError

class Notepad:
    def __init__(self, root):
        self.root = root
        self.root.title("AWS Compatible Notepad")
        self.root.geometry("600x400")
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand="yes", fill="both")
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)  
        # Adds a command to create a new file
        self.file_menu.add_command(label="Open", command=self.open_file)  
        # Adds a command to open a file
        self.file_menu.add_command(label="Save", command=self.save_file)  
        # Adds a command to save the file
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)  
        # Adds a command to exit the application

    def new_file(self):
        self.text_area.delete(1.0, tk.END)  # Comment: Clears the text area to create a new file

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)  
                #Inserts the content of the opened file into the text area

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)  
                #Writes the content of the text area to the specified file
            # Upload the file to AWS S3
            bucket_name = 'your-S3-bucket-name'
            object_name = file_path.split("/")[-1]
            access_key = os.environ.get('AWS_ACCESS_KEY')
            secret_key = os.environ.get('AWS_SECRET_KEY')
            s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
            try:
                s3.upload_file(file_path, bucket_name, object_name)
                print("File successfully uploaded to AWS S3.")  
                #Prints a success message if the file is uploaded successfully
            except NoCredentialsError:
                print("Invalid AWS Credentials. Please check your access key and secret key.")  
                #Prints an error message if the AWS credentials are invalid

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
