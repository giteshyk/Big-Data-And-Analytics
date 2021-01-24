
from pyspark.context import SparkContext
from pyspark.sql.context import SQLContext
from pyspark.sql.session import SparkSession
from pyspark.sql.functions import *
from pyspark import SparkConf
from pyspark.sql.types import *
from pyspark.sql.window import Window  
    
sc = SparkContext()
sqlContext = SQLContext(sc)
spark = SparkSession(sc)

# load up other dependencies
import re
import glob
import pandas as pd
import datetime
raw_data_files = glob.glob('C:\Logs\*.log')
base_df = spark.read.text(raw_data_files)
#type(base_df)
print((base_df.count(),len(base_df.columns)))
base_df.show(truncate=False)

sample_logs = [item['value'] for item in base_df.take(134077)]

time_taken = []
time_pattern = r'(\d+\.\d+)'
for item in sample_logs:
    if item.find("Testing Completed after") != -1:
        time_taken.append(re.search(time_pattern,item).group(0)) 

completed_tests = 0
for item in sample_logs:
    if(item.find("==  FINAL EXECUTION:")) != -1:
        completed_tests += 1

count = 0
warnings = [0]*completed_tests

for item in sample_logs:
    if(item.find("WARNING:")) != -1 :
        warnings[count] += 1
    if(item.find("==  FINAL EXECUTION:")) != -1:
        count += 1

time_stamp = []
workweek = []
time_stamp_pattern = r"(\d{4}-\d{2}-\d{2})"
for item in sample_logs:
    if(item.find("==  FINAL EXECUTION:")) != -1:
        time_stamp.append(re.search(time_stamp_pattern,item).group(0)) 

for item in time_stamp:
    workweek.append(datetime.date(int(item[0]+item[1]+item[2]+item[3]),int(item[5]+item[6]),int(item[8]+item[9])).strftime("%V"))


hosts = []
host_os = []
mem_config = []
test_sequence = []

host_pattern = r'((BA|JF)\S+-\S+)'
os_pattern = r"(\<\D+\>)"
mem_pattern = r"([\d+-]+\d+)"


for item in sample_logs:
    if(item.find("SUT Hostname is ")) != -1:
        hosts.append(re.search(host_pattern,item).group(0))
    if(item.find("Operating System: ")) != -1:
        host_os.append(re.search(os_pattern,item).group(0))
    if(item.find("Mem config :")) != -1:
        mem_config.append(re.findall(mem_pattern,item)[-1])

data = {'Time_stamp' : time_stamp, 'Work_week' : workweek,'Host_name' : hosts,'Host_OS' : host_os,'Mem_config' : mem_config,'Warnings': warnings,'Time_taken' : time_taken}

logs_df = pd.DataFrame(data = data)

logs_df

logs_df_spark = spark.createDataFrame(logs_df);

