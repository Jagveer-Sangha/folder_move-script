import os
import shutil
from dotenv import load_dotenv #Env vars

load_dotenv()  # reads .env and loads its values
PIC_PATH = os.getenv("PIC_PATH")
DOCUMENTS_PATH = os.getenv("DOCUMENTS_PATH")
FILE_PATH = os.getenv("FILE_PATH") #Make sure it has a '/' at the end

def move_pictures(file: str):
    shutil.move(file, PIC_PATH)
    print(f"{file} has been moved to pictures")


def move_to_documents(file: str):
    shutil.move(file, DOCUMENTS_PATH)
    print(f"{file} has been moved to documents")


try:
    file_dir = os.listdir(FILE_PATH)
    print("Script Starting")

    if len(file_dir) == 0:
        print("Folder is empty")

    for file in file_dir:
        if file.endswith(".exe"):
            os.remove(file)
            print(f"{file} has been removed")

        elif file.endswith(".zip") or file.endswith(".pdf") or file.endswith(".txt"):
            move_to_documents(FILE_PATH+file)

        elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            move_pictures(FILE_PATH+file)

        elif os.path.isdir(FILE_PATH+file):
            move_to_documents(FILE_PATH+file)

        elif file.endswith(".ini"):
            print(f'ignoring .ini file {file}')
            
        else:
            print("Nothing available to move")
except Exception as e:
    print(e)

print("Script Completed")
