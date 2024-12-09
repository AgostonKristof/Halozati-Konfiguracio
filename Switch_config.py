from netmiko import ConnectHandler
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'cisco',
}

net_connect = ConnectHandler(**cisco_device)
config_commands = [
    'vlan 30',
    'name Titkarsag',
    'exit',
    'vlan 40',
    'name Logisztika',
    'exit',
    'interface range FastEthernet 0/1-12',
    'switchport mode access',
    'switchport access vlan 30',
    'exit',
    'interface range FastEthernet 0/13-24',
    'switchport mode access',
    'switchport access vlan 40',
    'exit',
    'interface GigabitEthernet0/1',
    'switchport mode access',
    'switchport port-security',
    'switchport port-security maximum 1',
    'switchport port-security mac-address sticky',
    'switchport port-security violation shutdown',
]
output = net_connect.send_config_set(config_commands)
print(output)