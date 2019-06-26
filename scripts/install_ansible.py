#!/usr/bin/python

#
#
#
import subprocess
import os
import time
import re

def update_host():
    
subprocess.call(['apt-get', 'update', '-y')

# END update_host()

def install_ansible():
   
subprocess.call(['sudo', 'apt-add-repository', 'ppa:ansible/ansible', '-y'])
time.sleep(5)
subprocess.call(['sudo', 'apt-get', 'update', '-y'])
time.sleep(5)
subprocess.call(['sudo', 'apt-get', 'install', 'ansible', '-y'])
time.sleep(5)
subprocess.call(['sudo', 'apt-get', 'install', 'python3-pip', '-y'])
time.sleep(5)    
subprocess.call(['sudo', 'pip3', 'install', 'requests', 'google-auth'])

# END install_ansible()
    
def configure_ansible()
    
f_old = open("/etc/ansible/ansible.cfg")
f_new = open("/etc/ansible/ansible-config-new.cfg", "w")

for line in f_old:
    if 'enable_plugins = ' in line:
       c = line
       d = re.sub('#enable_plugins = ', 'enable_plugins = gcp_compute, ', c)
       f_new.write(d)
    else:
        f_new.write(line)

f_old.close()
f_new.close()

subprocess.call(['sudo', 'mv', '/etc/ansible/ansible.cfg', 'ansible-config.bak'])
subprocess.call(['sudo', 'mv', '/etc/ansible/ansible-config-new.cfg', '/etc/ansible/ansible.cfg'])

# END configure_ansible()

def main()

    update_host()
    install_ansible()
    configure_ansible()

# END main()