from scapy.all import sniff, IP
from collections import defaultdict
import time
THRESHOLD_PACKET_COUNT = 1000  
MONITORING_INTERVAL = 10
packet_count = 0
ip_counter = defaultdict(int)
start_time = time.time()
def log_suspicious_activity(packet_count, unique_ips):
    with open("alert_log.txt", "a") as log_file:
        log_file.write(f"Gyanús forgalom észlelve!\n")
        log_file.write(f"  Teljes csomagszám: {packet_count}\n")
        log_file.write(f"  Egyedi forrás IP-címek száma: {unique_ips}\n")
        log_file.write("\n")
def analyze_traffic():
    global packet_count, ip_counter
    unique_ips = len(ip_counter)
    if packet_count > THRESHOLD_PACKET_COUNT:
        log_suspicious_activity(packet_count, unique_ips)
    # Forgalmi adatok alaphelyzetbe állítása
    ip_counter.clear()
    packet_count = 0
def packet_handler(packet):
    global packet_count, ip_counter, start_time
    if IP in packet:
        src_ip = packet[IP].src
        packet_count += 1
        ip_counter[src_ip] += 1
    # Ellenőrizni, hogy lejárt-e a monitorozási intervallum
    current_time = time.time()
    if current_time - start_time > MONITORING_INTERVAL:
        analyze_traffic()
        start_time = time.time()
def main():
    print("=== Hálózatfigyelő elindítva ===")
    try:
        sniff(prn=packet_handler, store=False)
    except KeyboardInterrupt:
        print("\nProgram leállítva.")
if __name__ == "__main__":
    main()