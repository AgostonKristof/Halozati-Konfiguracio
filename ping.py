import os
import platform
def ping_device(ip_address):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = f"ping {param} 3 {ip_address}"  #
    response = os.system(command)
    if response == 0:
        print(f"{ip_address} elérhető")
    else:
        print(f"{ip_address} nem elérhető")
ping_device('192.168.1.2')
