from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**device)
config_commands = [
    'interface GigabitEthernet0/1',
    'ip address 192.168.2.1 255.255.255.0',
    'no shutdown',
    'exit'
]
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()
