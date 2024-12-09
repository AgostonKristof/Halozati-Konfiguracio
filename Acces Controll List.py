from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'enable_password',
}

net_connect = ConnectHandler(**device)
net_connect.enable()
config_commands = [
    'access-list deny icmp host 10.0.0.10 any',
    'do sh access-list'
]
output = net_connect.send_config_set(config_commands)
print(output)
net_connect.disconnect()