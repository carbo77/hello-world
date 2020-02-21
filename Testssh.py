from netmiko import ConnectHandler

MyDevices = {
    'device_type': 'cisco_ios',
    'ip': '10.3.254.22',
    'username': 'wbohsainadm',
    'password': 'Maybe20?'
}

connected = ConnectHandler(**MyDevices)
output = connected.send_command('terminal lenght 0')
output = connected.send_command('show run')
ConfigBckp = open(MyDevices['ip']+".txt","w")

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
