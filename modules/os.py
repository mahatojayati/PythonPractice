import os 
# This script demonstrates various functionalities of the os module in Python.
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir())
print("Is the current directory a directory?", os.path.isdir(os.getcwd()))
print("Is the current directory a file?", os.path.isfile(os.getcwd()))
print("Is the current directory a symbolic link?", os.path.islink(os.getcwd()))
print("Absolute path of the current directory:", os.path.abspath(os.getcwd()))
print("Size of the current directory:", os.path.getsize(os.getcwd()), "bytes")
print("Last modified time of the current directory:", os.path.getmtime(os.getcwd()))
print("Creation time of the current directory:", os.path.getctime(os.getcwd()))
os.mkdir("test_directory")

