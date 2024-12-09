from netmiko import ConnectHandler
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
}
try:
    connection = ConnectHandler(**device)
    connection.enable() 

    with open("running_config.txt", "r") as file:
        config_lines = file.readlines()
    output = connection.send_config_set(config_lines)
    print("Konfiguráció visszatöltve.")
    print(output)
except Exception as e:
    print(f"Hiba történt: {e}")
finally:
    connection.disconnect()