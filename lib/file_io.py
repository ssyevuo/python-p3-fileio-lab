#helps working with file paths
from pathlib import Path

#writes code to a new file
def write_file(file_name, file_content):
    # adds the .txt extension to the file
    file_path = file_name.with_suffix(".txt") 
    #make use of write mode
    with open(file_path, mode='w', encoding='utf-8') as file:
        #write the content to the file
        file.write(file_content)


#appends content to an existing file
def append_file(file_name, append_content):
    # adds the .txt extension to the file
   file_path = file_name.with_suffix(".txt")
   #make use of append mode to add content to the end of the file
   with open(file_path, mode='a', encoding='utf-8') as file:
        #append the content to the file
       file.write(append_content)

#reads content from a file
def read_file(file_name):
    # adds the .txt extension to the file, 
    file_path = Path(file_name).with_suffix(".txt")
    #make use of read mode to read the content from the file
    with open(file_path, mode='r', encoding='utf-8') as file:
        #read the content from the file and return it
        return file.read()
