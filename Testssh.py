import getpass
from netmiko import ConnectHandler

print ("Enter Username and Password")
user = input ("Username: ")
password = getpass.getpass(prompt="Password: ")

# Read Basic Template
with open('L2BasicTemplate.txt') as f:
    commands_list = f.read().splitlines()

# List of devices to build
with open('devicelist.txt') as f:
    devices_list = f.read().splitlines()

# Fill dictionary for Netmiko connections
for devices in devices_list:
    print ('Connecting to device" ' + devices)
    ip_address_of_device = devices
    Cisco_ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': user,
        'password': password
    }
# Connect to the first device on dict Cisco IOS device
    sessionssh = ConnectHandler(**Cisco_ios_device)
    output = sessionssh.send_config_set(commands_list)
    print (output)




