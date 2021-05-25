import re
import glob
import pandas as pd
import datetime
import time
import os
import shutil
import sys
import socket
from zipfile import ZipFile
from zipfile import BadZipFile
from shutil import copyfile

#get all the zip files from certain location with glob,in my case a shared location 
raw_data_files = glob.glob(r'\\Logs\*\*\*\*.zip') 

#list that will have locaitons of the required files
zip_with_summary_files = []

for item in raw_data_files:
    #try will ignore the files that are corrupt,otherwise code exits with BadZipFile error
    try:
        with ZipFile(raw_data_files[item], 'r') as zip:
            file_list = zip.namelist()
            
        for item_1 in file_list:
            #I needed files which had 'summary' in their names
            if(item_1.find("summary") != -1):
                zip_with_summary_files.append(item)
            
    except BadZipFile:
        pass

   
for item in zip_with_summary_files:
    shutil.copy(item, r'\local\path\here')
