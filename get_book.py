import os

def get_book_text(path):

    if not path or not os.path.exists(path):
        return "File not found!"

    try:
        with open(path) as file:
            file_content = file.read()
    except Exception as e:
        return f"Error occurred: {e}"
    
    if not file_content:
        return "The file is empty!"

    return file_content