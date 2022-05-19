from paramiko import SSHClient, AutoAddPolicy
from username import send_user, send_pass
import time

client = SSHClient()
client.load_host_keys('C:/Users/nelson/.ssh/known_hosts')
client.load_system_host_keys()

client.set_missing_host_key_policy(AutoAddPolicy())


client.connect('nellienel2.synology.me', username = 'nelson', password = 'Welkom123!!??')

print("succesvol verbonden")

time.sleep(3)

command = '/interface print \n'

stdin, stdout, stderr = client.exec_command(command)
response = stdout.readlines()

print(''.join(map(str,response)))

client.close()

print("uitgelogd")

