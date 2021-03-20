import re
import glob
import pandas as pd
import datetime
import time
import os 


def cr_auto_log_parser():
    # using glob to extract the path names that are specific to required log files
    raw_data_files = glob.glob('C:\Temp\AutoLogs\*.log')

    # arrays belonging to each field that is going to be in our pandas dataframe obatined after processing
    warnings = []
    kernel_panics = []
    hosts = []
    host_os = []
    mem_config = []
    final_exec = []
    bkc = []
    bios_actual = []
    software_actual = []
    time_taken = []
    time_stamp = []
    work_week = []
    test_sequence = []

    # using regex patterns to extract certain fields for our dataset (very flexible and useful if certain field
    # follows a
    # pattern)
    host_pattern = r"((BA|JF)\S+-\S+)"
    os_pattern = r"(\<\D+\>)"
    mem_pattern = r"([\d+-]+\d+)"
    final_exec_pattern = r"([A-Z]+)"
    bkc_pattern = r"(WW\S+)"
    bios_pattern = r"(=\s\S+)"
    software_pattern = r"=\s\S+"
    time_pattern = r'(\d+\.\d+)'
    time_stamp_pattern = r"(\d{4}-\d{2}-\d{2})"

    for item1 in raw_data_files:
        with open(item1, "r") as f:
            sample_log = list(f)

        count = 0
        kernel_panic = 0
        warnings_count = 0

        host_name = "NF"
        host_os_name = "NF"
        mem_config_name = "NF"
        test_sequence_name = "NF"
        bios_name = "NF"
        bkc_name = "NF"
        software_name = "NF"
        final_execution_name = "Interrupted"
        time_taken_name = "NF"
        time_stamp_name = "NF"
        work_week_name = 0

        for item in sample_log:

            count += 1

            if (item.find("Warning:")) != -1:
                warnings_count += 1

            if (item.find("Kernel Panic found in log!")) != -1:
                kernel_panic += 1

            if (item.find("SUT Hostname is ")) != -1:
                host_name = re.search(host_pattern, item).group(0)
                time_stamp_name = re.search(time_stamp_pattern, item).group(0)
                temp = time_stamp_name
                work_week_name = datetime.date(int(temp[0] + temp[1] + temp[2] + temp[3]), int(temp[5] + temp[6]),
                                               int(temp[8] + temp[9])).strftime("%V")
                work_week_name = int(work_week_name)

            if (item.find("Operating System: ")) != -1:
                host_os_name = re.search(os_pattern, item).group(0)

            if (item.find("Mem config :")) != -1:
                mem_config_name = re.findall(mem_pattern, item)[-1]

            if (item.find("TEST SEQUENCE SETUP")) != -1:
                test_sequence_name = sample_log[count + 1]

            if (item.find("BKC (unconfirmed) -------------- =")) != -1:
                bkc_name = re.search(bkc_pattern, item).group(0)

            if (item.find("BIOS (actual) --------------- =")) != -1:
                bios_name = re.search(bios_pattern, item).group(0)[1:]

            if (item.find("Software (actual) -------------- =")) != -1:
                software_name = re.search(software_pattern, item).group(0)[1:]

            if (item.find("FINAL EXECUTION:")) != -1:
                final_execution_name = re.findall(final_exec_pattern, item)[-1]

            if (item.find("Testing Completed after")) != -1:
                time_taken_name = re.search(time_pattern, item).group(0)
                time_taken_name = float(time_taken_name)

        if final_execution_name != "Interrupted":
            time_stamp.append(time_stamp_name)
            hosts.append(host_name)
            host_os.append(host_os_name)
            mem_config.append(mem_config_name)
            bkc.append(bkc_name)
            bios_actual.append(bios_name)
            software_actual.append(software_name)
            test_sequence.append(test_sequence_name)
            time_taken.append(time_taken_name)
            final_exec.append(final_execution_name)
            warnings.append(warnings_count)
            kernel_panics.append(kernel_panic)
            work_week.append(work_week_name)

    data = {'Time_stamp': time_stamp, 'Work_week': work_week, 'Host_name': hosts, 'Host_OS': host_os,
            'Mem_config': mem_config, 'Test Sequence': test_sequence, 'BKC': bkc, 'Software': software_actual,
            'BIOS': bios_actual, 'Warnings': warnings, 'Kernel Panics': kernel_panics, 'Final Execution': final_exec,
            'Time_taken(m)': time_taken}

    logs_df = pd.DataFrame(data=data)
    if not os.path.exists("C:\Temp\CRAuto_csvs"):
        os.makedirs("C:\Temp\CRAuto_csvs")
    logs_df.to_csv(path_or_buf=r"C:\Temp\CRAuto_csvs\CRAuto_CSV_" + time.strftime('%Y-%m-%d_%H-%S') + ".csv")

if __name__ == '__main__':
    cr_auto_log_parser()
