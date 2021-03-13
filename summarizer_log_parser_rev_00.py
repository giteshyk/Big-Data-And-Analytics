#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import glob
import pandas as pd
import datetime
import time
import os
import shutil
import sys


# In[2]:


raw_data_files = glob.glob('C:\Temp\Applogs\*\*\summ*.log')


# In[3]:


gb_reads_name = "NF"
unexpected_events_name = "NF"
expected_events_name = "NF"
total_injections_name = "NF"
total_state_transitions_name = "NF"
transition_1_name = 0
transition_2_name = 0
transition_3_name = 0
transition_4_name = 0
transition_5_name = 0
transition_6_name = 0
transition_7_name = 0
transition_8_name = 0
transition_9_name = 0
transition_10_name = 0
transition_11_name = 0
transition_12_name = 0
transition_13_name = 0
transition_14_name = 0
transition_15_name = 0
transition_16_name = 0
transition_17_name = 0


# In[4]:


gb_reads = []
unexpected_events = []
expected_events = []
total_injections = []
total_state_transitions = []
transition_1 = []
transition_2 = []
transition_3 = []
transition_4 = []
transition_5 = []
transition_6 = []
transition_7 = []
transition_8 = []
transition_9 = []
transition_10 = []
transition_11 = []
transition_12 = []
transition_13 = []
transition_14 = []
transition_15 = []
transition_16 = []
transition_17 = []


# In[5]:


gb_reads_pattern = "\d+.\d+"
events_pattern = "\d+"


# In[6]:


for item1 in raw_data_files:
    with open(item1, "r") as f:
            sample_log = list(f)
            
    gb_reads_name = "NF"
    unexpected_events_name = "NF"
    expected_events_name = "NF"
    total_injections_name = "NF"
    total_state_transitions_name = "NF"
    transition_1_name = 0
    transition_2_name = 0
    transition_3_name = 0
    transition_4_name = 0
    transition_5_name = 0
    transition_6_name = 0
    transition_7_name = 0
    transition_8_name = 0
    transition_9_name = 0
    transition_10_name = 0
    transition_11_name = 0
    transition_12_name = 0
    transition_13_name = 0
    transition_14_name = 0
    transition_15_name = 0
    transition_16_name = 0
    transition_17_name = 0
            
    for item in sample_log:
        if(item.find("Garbage/bad reads:")) != -1:
            gb_reads_name = re.search(gb_reads_pattern,item).group(0)
        if(item.find("expected, out of total")) != -1:
            unexpected_events_name = re.findall(events_pattern,item)[0]
            expected_events_name = re.findall(events_pattern,item)[1]
            total_injections_name = re.findall(events_pattern,item)[2]
        if(item.find("total state_transitions:")) != -1:
            total_state_transitions_name = re.search("\d+",item).group(0)
            
        if(item.find("unused to BANK:r0:2a:")) != -1:
            transition_1_name = re.findall("\d+",item)[-1]
        if(item.find("unused to BANK:r0")) != -1:
            transition_2_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0:2a to BANK:r0:BANK:r1:2b")) != -1:
            transition_3_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0 to BANK:r0:r1")) != -1:
            transition_4_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0 to RANK:r0")) != -1:
            transition_5_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0 to BANK:RESPARE:r0:r1")) != -1:
            transition_6_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0 to BANK:r0:BANK:r1:6a")) != -1:
            transition_7_name = re.findall("\d+",item)[-1]    
        if(item.find("BANK:r0 to BANK:r0:BANK:r1")) != -1:
            transition_8_name = re.findall("\d+",item)[-1]
        if(item.find("RANK:r0 to RANK:r0:BANK:r1:6b")) != -1:
            transition_9_name = re.findall("\d+",item)[-1]
        if(item.find("RANK:r0 to RANK:r0:BANK:r1")) != -1:
            transition_10_name = re.findall("\d+",item)[-1]
        if(item.find("RANK:r0 to RANK:RESPARE:r0:BANK:r1")) != -1:
            transition_11_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0:BANK:r1:6a to RANK:r0:BANK:r1:6b")) != -1:
            transition_12_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0:BANK:r1 to RANK:r0:BANK:r1")) != -1:
            transition_13_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0:BANK:r1 to BANK:r0:RANK:r1")) != -1:
            transition_14_name = re.findall("\d+",item)[-1]
        if(item.find("RANK:r0:BANK:r1 to RANK:r0:RANK:r1")) != -1:
            transition_15_name = re.findall("\d+",item)[-1]
        if(item.find("BANK:r0:RANK:r1 to RANK:r0:RANK:r1")) != -1:
            transition_16_name = re.findall("\d+",item)[-1]
        if(item.find("RANK:RESPARE:r0:BANK:r1 to RANK:r0:RANK:r1")) != -1:
            transition_17_name = re.findall("\d+",item)[-1]
    
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


# In[18]:


data = {'Garbage/bad reads': gb_reads, 
        'Unexpected events' : unexpected_events, 
        'Expected events' : expected_events, 
        'Total injections' : total_injections, 
        'unused to BANK:r0:2a:' : transition_1, 
        'unused to BANK:r0' : transition_2, 
        'BANK:r0:2a to BANK:r0:BANK:r1:2b' : transition_3, 
        'BANK:r0 to BANK:r0:r1' : transition_4, 
        'BANK:r0 to RANK:r0' : transition_5, 
        'BANK:RESPARE:r0:r1' : transition_6, 
        'BANK:r0:BANK:r1:6a' : transition_7, 
        'BANK:r0:BANK:r1' : transition_8, 
        'RANK:r0:BANK:r1:6b' : transition_9, 
        'RANK:r0:BANK:r1' : transition_10, 
        'RANK:RESPARE:r0:BANK:r1' : transition_11, 
        'RANK:r0:BANK:r1:6b' : transition_12, 
        'RANK:r0:BANK:r1' : transition_13, 
        'BANK:r0:RANK:r1' : transition_14, 
        'RANK:r0:RANK:r1' : transition_15, 
        'RANK:r0:RANK:r1' : transition_16, 
        'RANK:r0:RANK:r1' : transition_17}


# In[19]:


summarizer_df = pd.DataFrame(data = data)


# In[20]:


summarizer_df.to_csv(path_or_buf = r"C:\Spark\CSVs\summarizer_CSV_" + time.strftime('%Y-%m-%d_%H-%S') + ".csv")


# In[21]:


summarizer_df


# In[ ]:




