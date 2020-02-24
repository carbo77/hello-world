import getpass
from netmiko import ConnectHandler

print ("Enter Username and Password")
user = input ("Username: ")
password = getpass.getpass(prompt="Password: ")

# Read Basic Template
#with open("Misc_config.txt") as f:
#    Misc_Commands_list = f.read().splitlines()

# Read L2 Template
#with open("C9300_Ports_config.txt") as f:
#    L2_commands_list = f.read().splitlines()

# Read Basic Template
with open("L2BasicTemplate.txt") as f:
    commands_list = f.read().splitlines()

# List of devices to build
with open('devicelist.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print ('Connecting to device: ' + devices)
    ip_address_of_device = devices
    Floor = devices [-2:]

    # Fill dictionary for Netmiko connections
    Cisco_ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': user,
        'password': password
    }
# Connect to the first device on dict Cisco IOS device dict
    sessionssh = ConnectHandler(**Cisco_ios_device)

# Manual commands to create VLANs per floor
    manual_list = ["conf t ", "vlan 3"+Floor, "name Test"]
#    output = sessionssh.send_command('conf t)
#    output = sessionssh.send_command('vlan 3'+Floor)
#    output = sessionssh.send_command('name Test)
 #   output = sessionssh.send_command('end)
    output = sessionssh.send_config_set(manual_list)
    print (output)

    # Load commands sets from files
    output = sessionssh.send_config_set(commands_list)
    print (output)
