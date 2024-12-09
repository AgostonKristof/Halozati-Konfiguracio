from scapy.all import sniff, IP, TCP
from collections import defaultdict
import time
PORT_SCAN_THRESHOLD = 20  # portokhoz próbál csatlakozni
TIME_WINDOW = 10  # Másodpercben
port_scan_tracker = defaultdict(set)
start_time = time.time()
def detect_port_scan(packet):
    "Csomagfigyelés és port scan érzékelése."
    global start_time, port_scan_tracker
    if IP in packet and TCP in packet:
        src_ip = packet[IP].src
        dst_port = packet[TCP].dport
        port_scan_tracker[src_ip].add(dst_port)
        if len(port_scan_tracker[src_ip]) > PORT_SCAN_THRESHOLD:
            print(f"⚠️ Port scan észlelve! Forrás IP: {src_ip}, Vizsgált portok: {len(port_scan_tracker[src_ip])}")
        if time.time() - start_time > TIME_WINDOW:
            print("\n--- Időablak vége ---")
            for ip, ports in port_scan_tracker.items():
                print(f"  {ip}: {len(ports)} portot próbált elérni")
            port_scan_tracker.clear()
            start_time = time.time()
def start_port_scan_monitor(interface="eth0"):
    "Port scan monitor indítása egy adott interfészen."
    print(f"Port scan monitor indítása az {interface} interfészen...")
    sniff(iface=interface, prn=detect_port_scan, store=False)
if __name__ == "__main__":
    try:
        network_interface = input("Add meg a hálózati interfészt (pl. eth0, wlan0): ").strip()
        start_port_scan_monitor(interface=network_interface)
    except KeyboardInterrupt:
        print("\nPort scan monitor leállítva.")