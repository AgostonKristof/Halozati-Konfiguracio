from netmiko import ConnectHandler
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "secret": "cisco"
}
connection = ConnectHandler(**cisco_device)
connection.enable()
config_output = connection.send_command("show running-config")
with open('current_config.txt', 'w') as file:
    file.write(config_output)
with open('stored_config.txt', 'r') as file:
    stored_config = file.read()
if config_output == stored_config:
    print("A konfiguráció megfelel a szabványoknak.")
else:
    print("A konfiguráció eltér a kívánt állapottól.")
