import filecmp
import os
import sys
import datetime
import shutil
import time
import glob
from typing import List, Tuple, Any

# insert Values
PROD = "\\\\ctxaa01\\amdocs\\AmdocsGui\\Prod"
PROD_CURRENT = "\\\\ctxaa01\\amdocs\\AmdocsGui\\Prod.current\\"
PROD_NEW = "\\\\ctxaa01\\amdocs\\AmdocsGui\\Prod.new"
BackUP = "\\\\isiloncorp1\\archive\\cm_backup\\Online\\BackupProd "
Products_From_Build = "\\\\isiloncorp1\\archive\\cm_backup\\Online\\BackupBuild"
BackupBuild_before_Prod = "\\\\isiloncorp1\\archive\\cm_backup\\Online\\BackupBuild_before_Prod\\"
Date = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
Date = Date.split("_")
Copy_Sources = "\\\\celcm05\\D$\\Amdocs\\Online\\"



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
            print("\n   Files only in:", folder1)
            print(file_path)
            answer = input("  Continue? Yes or No ")
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
            print("\n   Files only in:", folder2)
            print(file_path)
            answer = input("  Continue? Yes or No ")
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
                    print('   Mismatch!!!')
                    print('   Folder:', new_folder1)
                    print('   Folder:', new_folder2)
                    print('   File:', mismatch)
                    answer = input("  Continue? Yes or No ")
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
        print(" *All The Files & Folders Are The Same*   ")
        answer = input("  Continue? Yes or No ")
        if answer == "Yes":
            pass
        else:
            sys.exit()
    else:
        print('   Mismatch!!!')
        print('   Folder: ', folder1)
        print('   Folder: ', folder2)
        print('   File: ', mismatch)
        answer = input("  Continue? Yes or No ")
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




# Activet Functions section 1-4
print('''
###############
# *Section 1* #
###############
''')
print("*Compering Prod & Prod.current   *   ")
print(" they must be diff  !!!! If they are not different then you need to understand why?")
compare_folders(PROD, PROD_CURRENT)
mismatch_files(PROD, PROD_CURRENT)
print(" ")
print('''
###############
# *Section 2* #
###############
''')
print("* copy Prod to Prod.current.  *   ")
#Copy_folders(PRODs, PROD_CURRENTs)
print(" ")
print('''
###################
# *Section 3 - 4* #
###################
''')
print("* Compering Prod & Prod.new   *   ")
print(" they must be identical (except log file **not must**)!!!! If they are diff then you need to understand why?")
compare_folders(PROD, PROD_NEW)
mismatch_files(PROD, PROD_NEW)
print(" ")
print(' if they are diff and you want to Copy Prod to Prod.new answer "Yes" if you want to continue with out copy answer "No" To Stop & Exit Press "Q"')
answer = input()
if answer == "Yes":
    print("*copy Prod to Prod.new.  *   ")
    # Copy_folders(PRODs, PROD_NEWs)
elif answer == "Q":
    sys.exit()
elif answer == "No":
    print('Continuing...')
    pass
else:
    sys.exit()
print(" ")


# BackUP section 5
print('''
###############
# *Section 5* #
###############
''')
print("*Backup Prod.current   *   ")
BackupProd = "\\\\isiloncorp1\\archive\\cm_backup\\Online\\BackupProd\\"
MkdirPath = BackupProd + "Prod_2012_" + Date[0]
print("*Creating Backup Folder on ", MkdirPath, "   *   ")
#os.mkdir(MkdirPaths)
MkdirPath_Prod_current = MkdirPath + '\Prod.current'
print(MkdirPath_Prod_current)
#os.mkdir(MkdirPath_Prod_currents)
print("*Copy to BackUp *   ")
#Copy_folders(PROD_CURRENT, MkdirPath_Prod_current)

# section 6 - Backup last sources of build from build machine
print('''
###############
# *Section 6* #
###############
''')
folder_path = Products_From_Build
os.startfile(folder_path)
search_value = input('Please inter folder name: ')
Before_prod_path = BackupBuild_before_Prod+search_value
print(Before_prod_path)
# os.mkdir(Before_prod_path)
Version_Number = input('Please inter Version Number: ')
Sor = Copy_Sources+Version_Number+'\\Sources'
print(Sor)
Sor_des = Before_prod_path+'\\Sources'
print(Sor_des)
# Copy_folders(Sors, Sor_dess)

'''
# Get a list of all subdirectories in the folder that contain the search value
subdirectories = [name for name in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, name)) and search_value in name]
# Iterate over the subdirectories and print their names and last modified dates
my_list = []
for subdirectory in subdirectories:
    subdirectory_path = os.path.join(folder_path, subdirectory)
    last_modified = os.path.getmtime(subdirectory_path)
    #print(f"Folder: {subdirectory} | Last Modified: {last_modified}")
    my_list.append({subdirectory} | {last_modified})
print(my_list[1])
sorted_list = sorted(my_list)
first_string = sorted_list[-1]
print(first_string)
'''

# section 7
print('''
###############
# *Section 7* #
###############
''')
print('''
#######################################################################################
The next section you need to do menuely:

7.	Check ini files – in case of a change
You can verify that there are no modified ini files in the following way:
7.1. Connect to celcm05 as tfsservice and open Visual Studio. 
Choose AmdocsOnline_PROD_tfs-prod_celcm05_tfsservice workspace (This workspace's local folder is D:\PROD_Online).
In the current version's branch go to Sources/ini/prod/ini and verify that all the files in the workspace are latest (Latest = Yes).
If there are files that are not latest, you need to ask the developers.
If the files should be in Prod, do the following steps:
7.1.1 Get the specified ini files from Sources/ini/prod/ini.
7.1.2 Copy the files to \\ctxaa01\amdocs\amdocsgui\Prod.new\Ini
7.1.3	Compare the folders  \\ctxaa01\amdocs\amdocsgui\Prod\Ini
And \\ctxaa01\amdocs\amdocsgui\Prod.new\Ini
Check that the only differences between files were verified with the developer.
If not notify relevant developers.
Choose(return back) Work space  : AmdocsOnline_tfs-prod_celcm05_tfsservice
#######################################################################################
''')
print('   Done? Continue? Yes or No')
Continue = input()
if Continue == 'Yes':
    print('   Continuing...')
    pass
elif Continue == 'No':
    print('Aborted')
    sys.exit()
# section 8 and 9
print('''
###################
# *Section 8 - 9* #
###################
''')

print('We must be notified (from the team leader) with the specific applications/ files that need to be distributed to production. ')
storage = '\\\\ctxaa01\\Amdocs\\amdocsgui\\Testing\\'
itpet = "itpet"+Version_Number
itpet_bin = storage+itpet
itpet_bin_Dosview = storage+itpet
AB = list(os.listdir(itpet_bin))

try:
    try:
        index = AB.index("A")
        print('Storage found: ', AB[index])
        itpet_bin = storage + itpet + '\\Bin32_A'
    except:
        index = AB.index("B")
        print('Storage found: ', AB[index])
        itpet_bin = storage + itpet + '\\Bin32_B'
except:
    print("No Storage found")
    sys.exit()

itpet_comper = PROD_NEW + '\\Bin32'
print('Comparing: ', itpet_bin, '*TO*', itpet_comper)
compare_folders(itpet_bin, itpet_comper)
mismatch_files(itpet_bin, itpet_comper)
print('''
Copy only the relevant files from itpet directory to Prod.new directory. 
*** Do not copy “win.ini” and “RUN_BAP.bat” ***
''')
# Copy_folders(itpet_bin, itpet_comper)




# section 10
print('''
################
# *Section 10* #
################
''')

DOSVIEW1 = itpet_bin_Dosview + '\\DOSVIEW'
DOSVIEW2 = PROD_NEW + '\\DOSVIEW'
print("Comparing : ", DOSVIEW1, '*TO* ', DOSVIEW2)
print("*** If a mismatch was found ,consult the developer whether to sync*** ")
compare_folders(DOSVIEW1, DOSVIEW2)
mismatch_files(DOSVIEW1, DOSVIEW2)




# section 11
print('''
################
# *Section 11* #
################
''')

SQLScripts1 = itpet_bin_Dosview + '\\SQLScripts'
SQLScripts2 = PROD_NEW + '\\SQLScripts'
print("Comparing : ", SQLScripts1, '*TO* ', SQLScripts2)
print("*** If a mismatch was found ,consult the developer whether to sync*** ")
compare_folders(SQLScripts1, SQLScripts2)
mismatch_files(SQLScripts1, SQLScripts2)


# section 12
print('''
################
# *Section 12* #
################
''')


# Provide the network path you want to search
win_ini_path = r'\\ctxaa01\Amdocs\amdocsgui\Prod.new\Bin32'

# Call the function to count "win.ini" files
win_ini_count = count_win_ini_files(win_ini_path)

print(f"Number of 'win.ini' files found: {win_ini_count}")

print(' You shold have 15 files.! if you have 15 continue with "Yes" if you dont stop with "No"')
print("Do you have 15?")
answer = input()
if answer == "Yes":
    print(" Continuing... ")
    pass
elif answer == "No":
    print('Aborting. ')
    sys.exit()
else:
    sys.exit()
print(" ")


# section 13
print('''
################
# *Section 13* #
################
''')


print('Compare All Four csmflds locations, In case of mismatch ,notify the developers!!! ')
print("You need to check what is the lest unix storage and write the folder name in the answer")
storage_path = '\\\\itpet1\\AMD\\TST\\storage'
os.startfile(storage_path)
storage_num = input()



# Provide the two network paths you want to compare
csmflds1 = r'"\\ctxaa01\Amdocs\amdocsgui\Prod.new\Bin32\"'
csmflds2 = "\\\\itpet1\\AMD\\TST\\storage\\"+storage_num+"\\common_lib\\"
csmflds3 = "\\\\itpet1\\AMD\\TST\\storage\\"+storage_num+"\\lib"



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
    print("Mismatched 'csmflds' files found:")
    for file in mismatched_files:
        print(file)
        print('To continue write "Yes" to Abort write "No"')
        answer = input()
        if answer == "Yes":
            pass
        else:
            sys.exit()
else:
    print("No mismatched 'csmflds' files found.")
    print('To continue write "Yes" to Abort write "No"')
    answer = input()
    if answer == "Yes":
        pass
    else:
        sys.exit()





# Call the function to compare "csmflds" files
mismatched_files = compare_csmflds_files(csmflds1, csmflds2)
mismatched_files = compare_csmflds_files(csmflds1, csmflds3)



# Provide the two network paths you want to compare
intflds1 = r'"\\ctxaa01\Amdocs\amdocsgui\Prod.new\Bin32\"'
intflds2 = "\\\\itpet1\\AMD\\TST\\torage\\"+storage_num+"\\common_lib\\"
intflds3 = "\\\\itpet1\\AMD\\TST\\storage\\"+storage_num+"\\lib"


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
    print("Mismatched 'intflds' files found:")
    for file in mismatched_files2:
        print(file)
        print('To continue write "Yes" to Abort write "No"')
        answer = input()
        if answer == "Yes":
            pass
        else:
            sys.exit()
else:
    print("No mismatched 'intflds' files found.")
    print('To continue write "Yes" to Abort write "No"')
    answer = input()
    if answer == "Yes":
        pass
    else:
        sys.exit()





# Call the function to compare "csmflds" files
mismatched_files2 = compare_intflds_files(intflds1, intflds2)
mismatched_files2 = compare_intflds_files(intflds1, intflds3)


print('''




################
# *Section 14* #
################
''')


print("Update version.txt file with the details of version update ")
Version_txt = r'\\ctxaa01\amdocs\AmdocsGui\Prod.new\Bin32\version.txt'
os.startfile(Version_txt)



print('''
################
# *Section 15* #
################
''')

print("   Compare Prod & Prod.new directories and make sure the only differences are those that should be upgraded.")
compare_folders(PROD, PROD_NEW)
mismatch_files(PROD, PROD_NEW)



print('''
################
# *Section 16* #
################
''')

print("   Backup: Copy",  PROD_NEW, "directory to: ", MkdirPath)
#MkdirPath_Prod = MkdirPath + "\Prod.new"
#Copy_folders(PROD_NEW, MkdirPath_Prod)

print('''
################
# *Section 17* #
################
''')



print("""


17	Notify ORG-TECH-SYSTEM NT TEAM ORG-TECH-SYSTEMNTTEAM@CELLCOM.CO.IL:

email: 	ORG-TECH-SYSTEM NT TEAM ORG-TECH-SYSTEMNTTEAM@CELLCOM.CO.IL
CC: 	Amdocs_cm; TECH-BILLING TIFUL TECH-BILLING-TIFUL@cellcom.co.il
Subject:	Online files for production - Citrix 2012


היי,
הפצת מחסנים מוכנה ב Online Citrix
\\ctxaa01\amdocs\amdocsgui\Prod.new
נודה לביצוע ההפצה בCITRIX היום בלילה כאשר במערכות יהיו למטה

""")


print('   Done? Continue? Yes or No')
Continue = input()
if Continue == 'Yes':
    print('   Continuing...')
    pass
elif Continue == 'No':
    print('Aborted')
    sys.exit()






print("""
#####################################################
#####################################################
#####################################################
         Done, until the next time ;)
#####################################################
#####################################################
#####################################################
""")
