import os
def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
            working_dir_abs= os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
            # Will be True or False
            valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
            if not valid_target_dir:
                return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
            if not os.path.isdir(target_dir):
                return f'Error: "{directory}" is not a directory'
            list_of_contents =os.listdir(target_dir)
            contents_lines=[]
            for content in list_of_contents:
                content_path = os.path.join(target_dir,content)
                content_size =os.path.getsize(content_path)
                is_dir = os.path.isdir(content_path)
                contents_lines.append(f"- {content}: file_size={content_size} bytes, is_dir={is_dir}")
            return "\n".join(contents_lines)
            # return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"