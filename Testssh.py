from netmiko import ConnectHandler

SW1 = {
    'device_type': 'cisco_ios',
    'ip': '10.3.254.22',
    'username': 'wbohsainadm',
    'password': 'Maybe20?'
}

SW2 = {
    'device_type': 'cisco_ios',
    'ip': '10.3.254.23',
    'username': 'wbohsainadm',
    'password': 'Maybe20?'
}

Switches = [SW1,SW2]

for Devices in Switches:
    connected = ConnectHandler(**Devices)
    output = connected.send_command('terminal lenght 0')
    output = connected.send_command('show run')
    ConfigBckp = open(Devices['ip']+".txt","w")
    ConfigBckp.write(output)
    ConfigBckp.write("\n")
    ConfigBckp.write("by WB")
    ConfigBckp.close()
    print (output)



#config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
#output = net_connect.send_config_set(config_commands)
#print (output)

#for n in range (2,21):
#    print ("Creating VLAN " + str(n))
#    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)
