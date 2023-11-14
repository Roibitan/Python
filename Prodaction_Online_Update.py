import filecmp
import os
import sys
import datetime
import shutil
import time
import colorama
from colorama import Fore
import glob
from typing import List, Tuple, Any

# insert Values
PROD = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
PROD_CURRENT = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
PROD_NEW = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
BackUP = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
Products_From_Build = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
BackupBuild_before_Prod = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
Date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
Date = Date.split("_")
Copy_Sources = "\\XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
# class Colors:
#     RESET = "\033[0m"
#     BLACK = "\033[30m"
#     RED = "\033[31m"
#     GREEN = "\033[32m"
#     YELLOW = "\033[33m"
#     BLUE = "\033[34m"
#     MAGENTA = "\033[35m"
#     CYAN = "\033[36m"
#     WHITE = "\033[37m"


# Functions
def compare_folders(folder1, folder2):
    dir_cmp = filecmp.dircmp(folder1, folder2)

    for file_only_in_folder1 in dir_cmp.left_only:
        file_path = os.path.join(dir_cmp.left, file_only_in_folder1)
        if file_only_in_folder1.startswith("ULOG."):
            continue  # Skip ULOG. files
        if file_path is None:
            pass
        else:
            sys.stdout.write("\033[33m")
            print("\n      Files only in:", folder1)
            print("       ", file_path)
            sys.stdout.write("\033[0m")
            print("   - Continue? Yes or No ")
            answer = input("     Answer: ")
            if answer == "Yes":
                pass
            else:
                sys.exit()

    for file_only_in_folder2 in dir_cmp.right_only:
        file_path = os.path.join(dir_cmp.right, file_only_in_folder2)
        if file_only_in_folder2.startswith("ULOG."):
            continue  # Skip ULOG. files
        if file_path is None:
            pass
        else:
            sys.stdout.write("\033[33m")
            print("\n      Files only in:", folder2)
            print("       ", file_path)
            sys.stdout.write("\033[0m")
            print("   - Continue? Yes or No ")
            answer = input("     Answer: ")
            if answer == "Yes":
                pass
            else:
                sys.exit()

    for common_dir in dir_cmp.common_dirs:
        new_folder1 = os.path.join(folder1, common_dir)
        new_folder2 = os.path.join(folder2, common_dir)

        d1_contents = set(os.listdir(new_folder1))
        d2_contents = set(os.listdir(new_folder2))
        common = list(d1_contents & d2_contents)
        common_files = [f for f in common if os.path.isfile(os.path.join(new_folder1, f))]

        for file_name in common_files:
            if file_name.startswith("ULOG."):
                continue  # Skip ULOG. files

            file_path1 = os.path.join(new_folder1, file_name)
            file_path2 = os.path.join(new_folder2, file_name)

            if os.path.isfile(file_path1) and os.path.isfile(file_path2):
                match, mismatch, errors = filecmp.cmpfiles(new_folder1, new_folder2, [file_name])
                if mismatch:
                    sys.stdout.write("\033[31m")
                    print('      Mismatch!!!')
                    print('        Folder:', new_folder1)
                    print('        Folder:', new_folder2)
                    print('        File:', mismatch)
                    sys.stdout.write("\033[0m")
                    print("   - Continue? Yes or No ")
                    answer = input("     Answer: ")
                    if answer == "Yes":
                        pass
                    else:
                        sys.exit()


def mismatch_files(folder1, folder2):
    d1_contents = set(os.listdir(folder1))
    d2_contents = set(os.listdir(folder2))
    common = list(d1_contents & d2_contents)
    common_files = [f for f in common if os.path.isfile(os.path.join(folder1, f)) and not f.startswith("ULOG.")]
    match, mismatch, errors = filecmp.cmpfiles(folder1, folder2, common_files)
    if mismatch == []:
        sys.stdout.write("\033[32m")
        print("    ~ All The Files & Folders Are The Same ~   ")
        sys.stdout.write("\033[0m")
        print("   - Continue? Yes or No ")
        answer = input("     Answer: ")
        if answer == "Yes":
            pass
        else:
            sys.exit()
    else:
        sys.stdout.write("\033[31m")
        print('      Mismatch!!!')
        print('        Folder: ', folder1)
        print('        Folder: ', folder2)
        print('        File: ', mismatch)
        sys.stdout.write("\033[0m")
        print("   - Continue? Yes or No ")
        answer = input("     Answer: ")
        if answer == "Yes":
            pass
        else:
            sys.exit()

def Copy_folders(Copy1, Copy2):
    shutil.copytree(Copy1, Copy2, dirs_exist_ok=True)


def count_win_ini_files(win_ini_path):
    count = 0

    for root, dirs, files in os.walk(win_ini_path):
        for file in files:
            if file.lower() == "win.ini":
                count += 1

    return (count)


def copy_folder_with_exceptions(source_folder, destination_folder, exceptions):
    for root, dirs, files in os.walk(source_folder):
        relative_path = os.path.relpath(root, source_folder)
        destination_path = os.path.join(destination_folder, relative_path)

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        for file in files:
            if file not in exceptions:
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_path, file)

                #shutil.copy2(source_file_path, destination_file_path)







# Activet Functions section 1-4
sys.stdout.write("\033[35m")                            
print('''
        ###############
        # *Section 1* #
        ###############
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")                           
print("* Compering Prod & Prod.current *   ")
print("   - they must be diff!!!! If they are not different then you need to understand why?")
sys.stdout.write("\033[0m")                           
compare_folders(PROD, PROD_CURRENT)
mismatch_files(PROD, PROD_CURRENT)
print(" ")
sys.stdout.write("\033[35m")                            
print('''
        ###############
        # *Section 2* #
        ###############
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")                           
print("* copy Prod to Prod.current. *   ")
sys.stdout.write("\033[0m")                           
#Copy_folders(PRODs, PROD_CURRENTs)
sys.stdout.write("\033[32m")                            
print("     Done")
sys.stdout.write("\033[0m")
sys.stdout.write("\033[35m")                           
print('''
        ###################
        # *Section 3 - 4* #
        ###################
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")                           
print("* Compering Prod & Prod.new   *   ")
print("   - they must be identical (except log file **not must**)!!!! If they are diff then you need to understand why?")
sys.stdout.write("\033[0m")                           
compare_folders(PROD, PROD_NEW)
mismatch_files(PROD, PROD_NEW)
print(" ")
sys.stdout.write("\033[33m")                            
print('* After cheking why if you want to Copy Prod to Prod.new answer "Yes" if you want to continue with out copy answer "No" To Stop & Exit Press "Q" *')
sys.stdout.write("\033[0m")                           
answer = input("     Answer: ")
if answer == "Yes":
    sys.stdout.write("\033[33m")
    print("* copy Prod to Prod.new.  *   ")
    sys.stdout.write("\033[0m")                           
    # Copy_folders(PRODs, PROD_NEWs)
    sys.stdout.write("\033[32m")
    print("     Done")
    sys.stdout.write("\033[0m")                           
elif answer == "Q":
    sys.exit()
elif answer == "No":
    print('     Continuing...')
    pass
else:
    sys.exit()

# BackUP section 5
sys.stdout.write("\033[35m")                            
print('''
        ###############
        # *Section 5* #
        ###############
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")                           
print("* Backup Folder Prod.current *   ")
sys.stdout.write("\033[0m")
BackupProd = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"

MkdirPath = BackupProd + "Prod_2012_" + Date[0]
sys.stdout.write("\033[33m")                            
print("   - Creating Backup Folder ", MkdirPath)
sys.stdout.write("\033[0m")                           
#os.mkdir(MkdirPaths)
MkdirPath_Prod_current = MkdirPath + '\Prod.current'
#os.mkdir(MkdirPath_Prod_currents)
sys.stdout.write("\033[33m")                            
print("   - Copy Prod.current to BackUp Folder  ")
sys.stdout.write("\033[0m")                           
#Copy_folders(PROD_CURRENT, MkdirPath_Prod_current)

# section 6 - Backup last sources of build from build machine
sys.stdout.write("\033[35m")                            
print('''
        ###############
        # *Section 6* #
        ###############
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")                           
print("* Backup last sources of build from build machine *")
folder_path = Products_From_Build
print("   - Locate the correct version name from the next window path")
sys.stdout.write("\033[0m")                           
time.sleep(2)
os.startfile(folder_path)
search_value = input('     Please insert folder name: ')
Before_prod_path = BackupBuild_before_Prod+search_value
# os.mkdir(Before_prod_path)
Version_Number = input('     Please insert Version Number: ')
Sor = Copy_Sources+Version_Number+'\\Sources'
Sor_des = Before_prod_path+'\\Sources'
sys.stdout.write("\033[33m")                            
print("     Copy Sources from", Sor, "To", Sor_des)
sys.stdout.write("\033[0m")                           
# Copy_folders(Sors, Sor_dess)

# section 7
sys.stdout.write("\033[35m")                            
print('''
        ###############
        # *Section 7* #
        ###############
''')
sys.stdout.write("\033[0")
sys.stdout.write("\033[34m")                          
print('''
################################################################################################################################################################################
                                The next section you need to do menuely:

                                1. Check ini files – in case of a change
                                You can verify that there are no modified ini files in the following way:
                                 1.1. Connect to celcm05 as tfsservice and open Visual Studio. 
                                 Choose AmdocsOnline_PROD_tfs-prod_celcm05_tfsservice workspace (This workspace's local folder is D:\PROD_Online).
                                 In the current version's branch go to Sources/ini/prod/ini and verify that all the files in the workspace are latest (Latest = Yes).
                                 If there are files that are not latest, you need to ask the developers.
                                 If the files should be in Prod, do the following steps:
                                  1.1.1 Get the specified ini files from Sources/ini/prod/ini.
                                  1.1.2 Copy the files to XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX
                                  1.1.3	Compare the folders  XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX
                                  And XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX
                                  Check that the only differences between files were verified with the developer.
                                  If not notify relevant developers.
                                  Choose(return back) Work space  : AmdocsOnline_tfs-prod_celcm05_tfsservice
################################################################################################################################################################################
''')
sys.stdout.write("\033[0m")                           
print('   Done? Continue? Yes or No')
Continue = input("     Answer: ")
if Continue == 'Yes':
    print('     Continuing...')
    pass
elif Continue == 'No':
    print('     Aborted')
    sys.exit()
# section 8 and 9
sys.stdout.write("\033[35m")                            
print('''
        ###################
        # *Section 8 - 9* #
        ###################
''')
sys.stdout.write("\033[0m")
sys.stdout.write("\033[33m")
print('   - We must be notified (from the team leader) with the specific applications/ files that need to be distributed to production. ')
sys.stdout.write("\033[0m")
storage = 'XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX'
itpet = "itpet"+Version_Number
itpet_bin = storage+itpet
itpet_bin_Dosview = storage+itpet
AB = list(os.listdir(itpet_bin))

try:
    try:
        index = AB.index("A")
        sys.stdout.write("\033[32m")
        print('       Storage found: ', AB[index])
        sys.stdout.write("\033[0m")
        itpet_bin = storage + itpet + '\\Bin32_A'
    except:
        index = AB.index("B")
        sys.stdout.write("\033[32m")
        print('       Storage found: ', AB[index])
        sys.stdout.write("\033[0m")
        itpet_bin = storage + itpet + '\\Bin32_B'
except:
    sys.stdout.write("\033[31m")
    print("       No Storage found")
    sys.stdout.write("\033[0m")                           
    sys.exit()

itpet_comper = PROD_NEW + '\\Bin32'
sys.stdout.write("\033[33m")                            
print('     Comparing: ', itpet_bin, '*TO*', itpet_comper)
sys.stdout.write("\033[0m")                           
compare_folders(itpet_bin, itpet_comper)
mismatch_files(itpet_bin, itpet_comper)


itpet_comper = "H:\PROD_Test\win"
# Provide the source folder and destination folder paths
source_folder = itpet_bin
destination_folder = itpet_comper

# Provide the file names to exclude from copying
exceptions = ["win.ini", "RUN_BAP.bat"]

sys.stdout.write("\033[33m")                            
print("* Copy from: ", source_folder, "To: ", destination_folder, "With Exceptions: ", exceptions, " *")
sys.stdout.write("\033[0m")                           
# Call the function to copy the folder with exceptions
copy_folder_with_exceptions(source_folder, destination_folder, exceptions)


# section 10
sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 10* #
        ################
''')
sys.stdout.write("\033[0m")                           

DOSVIEW1 = itpet_bin_Dosview + '\\DOSVIEW'
DOSVIEW2 = PROD_NEW + '\\DOSVIEW'
sys.stdout.write("\033[33m")                            
print("* Comparing : ", DOSVIEW1, 'TO: ', DOSVIEW2, " *")
print("   - If a mismatch was found ,consult the developer whether to sync ")
sys.stdout.write("\033[0m")                           
compare_folders(DOSVIEW1, DOSVIEW2)
mismatch_files(DOSVIEW1, DOSVIEW2)




# section 11
sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 11* #
        ################
''')
sys.stdout.write("\033[0m")                           

SQLScripts1 = itpet_bin_Dosview + '\\SQLScripts'
SQLScripts2 = PROD_NEW + '\\SQLScripts'
sys.stdout.write("\033[33m")                            
print("* Comparing : ", SQLScripts1, 'TO: ', SQLScripts2, " *")
print("   - If a mismatch was found ,consult the developer whether to sync ")
sys.stdout.write("\033[0m")                           
compare_folders(SQLScripts1, SQLScripts2)
mismatch_files(SQLScripts1, SQLScripts2)


# section 12
sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 12* #
        ################
''')
sys.stdout.write("\033[0m")

# Provide the network path you want to search
win_ini_path = r'XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX'

# Call the function to count "win.ini" files
win_ini_count = count_win_ini_files(win_ini_path)
sys.stdout.write("\033[33m")                            
print('   - You shold have 15 win.ini files!')
print(f'       ~ "win.ini" files found: {win_ini_count}')
sys.stdout.write("\033[0m")                           
print("   - Continue? Yes or No")

answer = input("     Answer: ")
if answer == "Yes":
    print("     Continuing... ")
    pass
elif answer == "No":
    print('     Aborting. ')
    sys.exit()
else:
    sys.exit()
print(" ")


# section 13
sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 13* #
        ################
''')
sys.stdout.write("\033[0m")

sys.stdout.write("\033[33m")                            
print('* Compare All Four csmflds locations, In case of mismatch ,notify the developers!!! * ')
print("   - You need to check what is the lest unix storage and write the folder name in the answer")
sys.stdout.write("\033[0m")                           
storage_path = 'XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX'
os.startfile(storage_path)
storage_num = input("     Answer: ")



# Provide the two network paths you want to compare
csmflds1 = r'"XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"'
csmflds2 = "H:XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
csmflds3 = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"



mismatched_files = []
def compare_csmflds_files(csmflds1, csmflds2):
    mismatched_files = []

    for root, dirs, files in os.walk(csmflds1):
        for file in files:
            if file.lower() == "csmflds":
                file_csmflds1 = os.path.join(root, file)
                file_csmflds2 = os.path.join(csmflds2, root.lstrip('\\'), file)

                if os.path.isfile(file_csmflds2):
                    with open(file_csmflds1, 'r') as f1, open(file_csmflds2, 'r') as f2:
                        content1 = f1.read().strip().lower()
                        content2 = f2.read().strip().lower()

                        if content1 != content2:
                            mismatched_files.append(file_csmflds1)

    return mismatched_files




if len(mismatched_files) > 0:
    sys.stdout.write("\033[31m")
    print("      Mismatched 'csmflds' files found:")
    sys.stdout.write("\033[0m")                           
    for file in mismatched_files:
        sys.stdout.write("\033[31m")
        print("      ", file)
        sys.stdout.write("\033[0m")
        print('   - To continue write "Yes" to Abort write "No"')
        answer = input("     Answer: ")
        if answer == "Yes":
            pass
        else:
            sys.exit()
else:
    sys.stdout.write("\033[32m")
    print("      No mismatched 'csmflds' files found.")
    sys.stdout.write("\033[0m")                           
    print('   - To continue write "Yes" to Abort write "No"')
    answer = input("     Answer: ")
    if answer == "Yes":
        pass
    else:
        sys.exit()





# Call the function to compare "csmflds" files
mismatched_files = compare_csmflds_files(csmflds1, csmflds2)
mismatched_files = compare_csmflds_files(csmflds1, csmflds3)



# Provide the two network paths you want to compare
intflds1 = r'"XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"'
intflds2 = "H:XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"
intflds3 = "XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX"


mismatched_files2 = []
def compare_intflds_files(intflds1, intflds2):
    mismatched_files2 = []

    for root, dirs, files in os.walk(intflds1):
        for file in files:
            if file.lower() == "intflds":
                file_intflds1 = os.path.join(root, file)
                file_intflds2 = os.path.join(intflds2, root.lstrip('\\'), file)

                if os.path.isfile(file_intflds2):
                    with open(file_intflds1, 'r') as f1, open(file_intflds2, 'r') as f2:
                        content1 = f1.read().strip().lower()
                        content2 = f2.read().strip().lower()

                        if content1 != content2:
                            mismatched_files2.append(file_intflds1)

    return mismatched_files2




if len(mismatched_files2) > 0:
    sys.stdout.write("\033[31m")
    print("      Mismatched 'intflds' files found:")
    sys.stdout.write("\033[0m")                           
    for file in mismatched_files2:
        sys.stdout.write("\033[31m")
        print(file)
        sys.stdout.write("\033[0m")
        print('   - To continue write "Yes" to Abort write "No"')
        answer = input("     Answer: ")
        if answer == "Yes":
            pass
        else:
            sys.exit()
else:
    sys.stdout.write("\033[32m")
    print("      No mismatched 'intflds' files found.")
    sys.stdout.write("\033[0m")                           
    print('   - To continue write "Yes" to Abort write "No"')
    answer = input("     Answer: ")
    if answer == "Yes":
        pass
    else:
        sys.exit()





# Call the function to compare "csmflds" files
mismatched_files2 = compare_intflds_files(intflds1, intflds2)
mismatched_files2 = compare_intflds_files(intflds1, intflds3)

sys.stdout.write("\033[35m")
print('''




        ################
        # *Section 14* #
        ################
''')
sys.stdout.write("\033[0m")

sys.stdout.write("\033[33m")                            
print("* Update version.txt file with the details of version update * ")
sys.stdout.write("\033[0m")                           
Version_txt = r'XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX'
os.startfile(Version_txt)
time.sleep(8)

sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 15* #
        ################
''')
sys.stdout.write("\033[0m")                           

sys.stdout.write("\033[33m")                            
print("* Compare Prod & Prod.new directories and make sure the only differences are those that should be upgraded. *")
sys.stdout.write("\033[0m")                           
compare_folders(PROD, PROD_NEW)
mismatch_files(PROD, PROD_NEW)


sys.stdout.write("\033[35m")
print('''
        ################
        # *Section 16* #
        ################
''')
sys.stdout.write("\033[0m")                           

sys.stdout.write("\033[33m")                            
print("* Backuping: ",  PROD_NEW, "directory to: ", MkdirPath, " *")
sys.stdout.write("\033[0m")                           
#MkdirPath_Prod = MkdirPath + "\Prod.new"
#Copy_folders(PROD_NEW, MkdirPath_Prod)

sys.stdout.write("\033[35m")                            
print('''
        ################
        # *Section 17* #
        ################
''')
sys.stdout.write("\033[0m")                           

sys.stdout.write("\033[33m")                            
print("Now you need to Send email with the instructions bellow:")
sys.stdout.write("\033[0m")                           

sys.stdout.write("\033[34m")                            
print("""


17	Notify ORG-TECH-SYSTEM NT TEAM ORG-TECH-SYSTEMNTTEAM@CELLCOM.CO.IL:

To: 	XXXXXXXXXXXXXXXXXX
CC: 	XXXXXXXXXXXXXXXXXX
Subject:	XXXXXXXXXXXXXXXXXX


היי,
הפצת מחסנים מוכנה ב Online Citrix
XXX:\\XXXXX\\XXXXXX\\XXXXXXX\\XXXXXX\\XXXXXX
נודה לביצוע ההפצה בCITRIX היום בלילה כאשר במערכות יהיו למטה

""")
sys.stdout.write("\033[0m")

print('     Done? Continue? Yes or No')
Continue = input("     Answer: ")
if Continue == 'Yes':
    print('   Continuing...')
    pass
elif Continue == 'No':
    print('   Aborted')
    sys.exit()





sys.stdout.write("\033[32m")
print("""
#####################################################
#####################################################
#####################################################
         Done, until the next time ;)
#####################################################
#####################################################
#####################################################
""")
sys.stdout.write("\033[0m")


time.sleep(5)