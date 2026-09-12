import os
import sys
# Add the project root (one level up from functions/) to sys.path
# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:

    # if file path out of working directory 
    # return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    #if the file path not a file 
    # f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        working_dir_abs= os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

            
        return content
    except Exception as e:
        return f"Error: {e}"
