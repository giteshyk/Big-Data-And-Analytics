import glob
import zipfile
from zipfile import ZipFile

#get the paths of the zip files
raw_data_files = glob.glob('path\to\zip_files\*.zip')

for item in raw_data_files:
    with zipfile.ZipFile(item,"r") as my_zip_file:
        my_zip_file.extractall("target\path\to\log_files_" + item[34:60])
