import errno
import os
import stat
import paramiko

paramiko.util.log_to_file('/tmp/paramiko.log')
paramiko.util.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))

host = 'local'
port = 22
username = 'user'

remote_dir = r"C:\Temp\AutoLogs"
local_dir = r"C:\log_files\from_remote"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh_client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())
ssh_client.connect('ip_address_here', port=port, username= "username", password = "password")

sftp_client = ssh_client.open_sftp()
source_folder = r"C:\Temp\AutoLogs"
local_folder = r"C:\log_files\from_remote"
inbound_files = sftp_client.listdir(source_folder)
print(inbound_files)

for ele in inbound_files:
    try:
        path_from = source_folder + '/' + ele
        path_to = local_folder + '/'+ ele
        sftp_client.get(path_from, path_to)
    except:
        print(ele)

sftp_client.close()
ssh.close()
