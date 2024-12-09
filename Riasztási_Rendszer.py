from netmiko import ConnectHandler
import time
device = {
    "device_type": "cisco_ios",
    "host": "192.168.1.1",
    "username": "admin",
    "password": "admin",
}
MEMORY_THRESHOLD = 80

def monitor_router():
    while True:
        try:
            net_connect = ConnectHandler(**device)
            print("Router elérhető.")
            output = net_connect.send_command("show ip interface brief")
            if "down" in output:
                print("Riasztás: Egy vagy több interface 'down' állapotban van!")            
             # Memóriahasználat ellenőrzése
            memory_usage = net_connect.send_command("show processes memory | include Processor Pool")
            memory_percent = int(memory_usage.split()[4][:-1])
            if memory_percent > MEMORY_THRESHOLD:
                print(f"Riasztás: Magas memóriahasználat ({memory_percent}%)!")
            net_connect.disconnect()    
        except Exception as e:
            print("Riasztás: A router nem elérhető vagy hibás válasz érkezett!")
            print(f"Hiba: {e}")
        time.sleep(10)
monitor_router()