import os

def delete_files_with_extension(folder_path, extension):
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(extension):
                file_path = os.path.join(folder_path, filename)
                os.remove(file_path)
                print(f"Deleted: {filename}")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    folder_path = "/path/to/your/local/folder"  # Replace this with the actual folder path
    extension_to_delete = ".rdp"

    delete_files_with_extension(folder_path, extension_to_delete)
