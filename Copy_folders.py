import json
import shutil
import os
import sys
import re
import glob


System_Path = os.environ['Sys']
Environment = os.environ['Env']
json_file_PATH = os.environ['Servers_json']
json_file = json_file_PATH+'\\XXXXXXX\\DevOps\\XXXXXXX\\Servers.json'
source_folder = System_Path+'\\XXXXXXX\\drop\\'


def copy_files_with_pattern(source_folder, target_folder, pattern):
    for file_path in glob.glob(os.path.join(source_folder, pattern)):
        if os.path.isfile(file_path):
            shutil.copy(file_path, target_folder)

def replicate_files(src_folder, dst_folder):
    if not os.path.exists(dst_folder):
        os.makedirs(dst_folder)
    files = os.listdir(src_folder)
    for file in files:
        src_file = os.path.join(src_folder, file)
        dst_file = os.path.join(dst_folder, file)
        if os.path.isfile(src_file):
            shutil.copy(src_file, dst_file)
            #print(f'Copied {src_file} to {dst_file}')


with open(json_file, 'r') as f:
  data = json.load(f)
result1 = data["servers"]
if Environment == 'PROD':
  for r in result1:
    if r['Env'] == 'PROD':
      print(r['server_name'])
      src = source_folder
      dst = r['Path']
      files = os.listdir(src)
      files.sort()
      regex = re.compile('CTASK*')
      Files_list = ['bundle.js', 'Index.html', 'bundle.js.license.txt']
      for i in range(len(Files_list)):
        copy_files_with_pattern(src, dst, Files_list[i])
      src_folder = src+'\\images'
      dst_folder = dst+'\\images'
      replicate_files(src_folder, dst_folder)
if Environment == 'QA':
  for r in result1:
    if r['Env'] == 'QA':
      print(r['server_name'])
      src = source_folder
      dst = r['Path']
      files = os.listdir(src)
      files.sort()
      regex = re.compile('CTASK*')
      Files_list = ['bundle.js', 'Index.html', 'bundle.js.license.txt']
      for i in range(len(Files_list)):
        copy_files_with_pattern(src, dst, Files_list[i])
      src_folder = src+'\\images'
      dst_folder = dst+'\\images'
      replicate_files(src_folder, dst_folder)