from netmiko import ConnectHandler
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
    "secret": "cisco"
}

config_backup = net_connect.send_command("show running-config")
with open("backup_config.txt", "w") as backup_file:
    backup_file.write(config_backup)
print("Konfiguráció mentése sikeres.")
