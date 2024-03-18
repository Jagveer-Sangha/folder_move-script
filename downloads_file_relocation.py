import os
import shutil


def move_pictures(file: str):
    pic_path = "C:/Users/jagve/Pictures"
    shutil.move(file, pic_path)
    print(f"{file} has been moved to pictures")


def move_to_documents(file: str):
    documents_path = "C:/Users/jagve/Documents"
    shutil.move(file, documents_path)
    print(f"{file} has been moved to documents")


try:
    file_path = "C:/Users/jagve/Downloads/"
    file_dir = os.listdir(file_path)
    print("Script Starting")

    if len(file_dir) == 0:
        print("Folder is empty")

    for file in file_dir:

        if file.endswith(".exe"):
            os.remove(file)
            print(f"{file} has been removed")

        elif file.endswith(".zip") or file.endswith(".pdf") or file.endswith(".txt"):
            move_to_documents(file_path+file)

        elif file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):

            move_pictures(file_path+file)

        elif os.path.isdir(file_path+file):
            move_to_documents(file_path+file)

        else:
            print("Nothing avaiable to move ")
except Exception as e:
    print(e)

print("Script Completed")
