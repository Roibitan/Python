import filecmp
import os

def compare_folders(folder1, folder2):
    dir_cmp = filecmp.dircmp(folder1, folder2)

    # Print common files
    # print('##############')
    # print("Common files:")
    # print('##############')
    # for common_file in dir_cmp.common_files:
    #     print(os.path.join(dir_cmp.left, common_file))

    # Print files only in the first folder
    #print("\nFiles only in", dir_cmp.left + ":")
    print("\nFiles only in TFS:")
    for file_only_in_folder1 in dir_cmp.left_only:
        print(os.path.join(dir_cmp.left, file_only_in_folder1))

    # Print files only in the second folder
    print("\nFiles only in TFS2:")
    for file_only_in_folder2 in dir_cmp.right_only:
        print(os.path.join(dir_cmp.right, file_only_in_folder2))

    # Recursively compare subdirectories
    for common_dir in dir_cmp.common_dirs:
        new_folder1 = os.path.join(folder1, common_dir)
        new_folder2 = os.path.join(folder2, common_dir)
        print("\nComparing subfolders", new_folder1, "and", new_folder2)
        compare_folders(new_folder1, new_folder2)


# Provide the paths to the two folders you want to compare
folder1_path = "C:\\PS\\TFS"
folder2_path = "C:\\PS\\TFS2"

compare_folders(folder1_path, folder2_path)
d1_contents = set(os.listdir('C:/PS/TFS'))
d2_contents = set(os.listdir('C:/PS/TFS2'))
common = list(d1_contents & d2_contents)
common_files = [f for f in common if os.path.isfile(os.path.join('C:/PS/TFS', f))]
match, mismatch, errors = filecmp.cmpfiles('C:/PS/TFS', 'C:/PS/TFS2', common_files)
print(' ')
print('Mismatch:')
print(mismatch)