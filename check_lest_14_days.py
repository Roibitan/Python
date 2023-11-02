import os
import datetime

file_path = "C:\Temp\Scripts\Test.txt"  # Replace with the path to your text file

try:
    with open(file_path, 'r') as file:
        for line in file:
            path = line.strip()  # Remove leading/trailing whitespaces and newline characters
            print(path)

            if not os.path.exists(path):
                print(f"Path '{path}' not found.")
                continue

            two_weeks_ago = datetime.datetime.now() - datetime.timedelta(days=14)
            for root, dirs, files in os.walk(path):
                for name in files + dirs:
                    full_path = os.path.join(root, name)
                    # Get the modification timestamp of the file/folder
                    modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
                    if modification_time > two_weeks_ago:
                        print(f"{name} in '{path}' is newer than 14 days.")

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")