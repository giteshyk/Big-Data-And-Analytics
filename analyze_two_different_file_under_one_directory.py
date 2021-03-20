import re
import glob
import pandas as pd
import datetime
import time
import os
import shutil
import sys
import pathlib

#this was the file where i will get 90% of my data, although it didn't have data related to host_name and test_sequence_name
raw_data_files = glob.glob(r'C:\log_files\summarizer_log_files\*\Test\summary_adddc*.log')

#will store the data in lists, and in future these lists can be used in data_frames

#declare lists

list1 = []
list2 = []

#patterns if regular expressions are required to pull out data
some_pattern = r"((BA|JF)\S+-\S+)"
gb_reads_pattern = "\d+.\d+"
events_pattern = "\d+"
time_stamp_pattern = r"(\d{4}-\d{2}-\d{2})"
test_sequence_pattern = r"\[\[\S+\]\]"

for item1 in raw_data_files:
    
    with open(item1, "r") as f:
            sample_log = list(f)
    
    variable1 = 'NF'
    variable2 = 'NF'
            
    for item in sample_log:
        if(item.find("somthing that is present in log and if matches then extract data")) != -1:
            gb_reads_name = re.search(gb_reads_pattern,item).group(0)
        if(item.find("something that matches")) != -1:
            var_name1 = re.findall(events_pattern,item)[0]
            var_name2 = re.findall(events_pattern,item)[1]
            tbars_name3 = re.findall(events_pattern,item)[2]
        if(item.find("something that matches")) != -1:
            var_name4 = re.search("\d+",item).group(0)
            
        if(item.find("something that matches")) != -1:
            var_1_name5 = re.findall("\d+",item)[-1]
    
    
    sample_log = []
    auto_logs = []
    
    path_parent = os.path.dirname(item1)
    autologs = glob.glob(path_parent + '\*BACR*.log')
    
    for item in autologs:
        if (item.find("bios_serial_read") != -1) or (item.find("sut_listener") != -1):
            autologs.remove(item)
    
    with open(autologs[0], "r") as f:
            sample_log = list(f)
            
    for item in sample_log:
        if item.find("SUT Hostname is ") != -1:
            host_name = re.search(host_pattern, item).group(0)
            time_stamp_name = re.search(time_stamp_pattern, item).group(0)
                
        if item.find("test_sequence=") != -1:
            test_sequence_name = re.findall(test_sequence_pattern,item)[-1]
            
    hosts.append(host_name)
    time_stamps.append(time_stamp_name)
    test_sequence.append(test_sequence_name)
    gb_reads.append(gb_reads_name)
    unexpected_events.append(unexpected_events_name)
    expected_events.append(expected_events_name)
    total_injections.append(total_injections_name)
    total_state_transitions.append(total_state_transitions_name)
    transition_1.append(transition_1_name)
    transition_2.append(transition_2_name)
    transition_3.append(transition_3_name)
    transition_4.append(transition_4_name)
    transition_5.append(transition_5_name)
    transition_6.append(transition_6_name)
    transition_7.append(transition_7_name)
    transition_8.append(transition_8_name)
    transition_9.append(transition_9_name)
    transition_10.append(transition_10_name)
    transition_11.append(transition_11_name)
    transition_12.append(transition_12_name)
    transition_13.append(transition_13_name)
    transition_14.append(transition_14_name)
    transition_15.append(transition_15_name)
    transition_16.append(transition_16_name)
    transition_17.append(transition_17_name) 
    
data = {'Timestamp': time_stamps,
        'Hosts':hosts,
        'Test Sequence': test_sequence,
        'Garbage/bad reads': gb_reads, 
        'Unexpected events' : unexpected_events, 
        'Expected events' : expected_events, 
        'Total injections' : total_injections, 
        'unused to BANK:r0:2a:' : transition_1, 
        'unused to BANK:r0' : transition_2, 
        'BANK:r0:2a to BANK:r0:BANK:r1:2b' : transition_3, 
        'BANK:r0 to BANK:r0:r1' : transition_4, 
        'BANK:r0 to RANK:r0' : transition_5, 
        'BANK:r0 to BANK:RESPARE:r0:r1' : transition_6, 
        'BANK:r0 to BANK:r0:BANK:r1:6a' : transition_7, 
        'BANK:r0 to BANK:r0:BANK:r1' : transition_8, 
        'RANK:r0 to RANK:r0:BANK:r1:6b' : transition_9, 
        'RANK:r0 to RANK:r0:BANK:r1' : transition_10, 
        'RANK:r0 to RANK:RESPARE:r0:BANK:r1' : transition_11, 
        'BANK:r0:BANK:r1:6a to RANK:r0:BANK:r1:6b' : transition_12, 
        'BANK:r0:BANK:r1 to RANK:r0:BANK:r1' : transition_13, 
        'BANK:r0:BANK:r1 to BANK:r0:RANK:r1' : transition_14, 
        'RANK:r0:BANK:r1 to RANK:r0:RANK:r1' : transition_15, 
        'BANK:r0:RANK:r1 to RANK:r0:RANK:r1' : transition_16, 
        'RANK:RESPARE:r0:BANK:r1 to RANK:r0:RANK:r1' : transition_17}

summarizer_df = pd.DataFrame(data = data)

summarizer_df.to_csv(path_or_buf = r"target\path\to_CSV_file" + time.strftime('%Y-%m-%d_%H-%S') + ".csv")
