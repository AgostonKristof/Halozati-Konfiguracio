import subprocess
def blokkol_ip(ip_cim):
    try:
        subprocess.run(
            ["netsh", "advfirewall", "firewall", "add", "rule", "name=Blokkolt_IP", "dir=in", "action=block", f"remoteip={ip_cim}"],
            check=True,
            shell=True
        )
        print(f"{ip_cim} sikeresen blokkolva lett.")
    except subprocess.CalledProcessError as e:
        print(f"Hiba történt az IP-cím blokkolásakor: {e}")

def eltavolit_ip(ip_cim):
    try:
        subprocess.run(
            ["netsh", "advfirewall", "firewall", "delete", "rule", "name=Blokkolt_IP", f"remoteip={ip_cim}"],
            check=True,
            shell=True
        )
        print(f"{ip_cim} sikeresen eltávolítva lett.")
    except subprocess.CalledProcessError as e:
        print(f"Hiba történt az IP-cím eltávolításakor: {e}")
ip_cim = "192.168.1.100"
blokkol_ip(ip_cim)  
eltavolit_ip(ip_cim)  