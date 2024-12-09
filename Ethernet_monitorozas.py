import psutil
import time
def monitor_network(interface):
    net_stat1 = psutil.net_io_counters(pernic=True)[interface]
    time.sleep(1) 
    net_stat2 = psutil.net_io_counters(pernic=True)[interface]
    bytes_sent = (net_stat2.bytes_sent - net_stat1.bytes_sent) * 8 / 1024
    bytes_recv = (net_stat2.bytes_recv - net_stat1.bytes_recv) * 8 / 1024
    packets_sent = net_stat2.packets_sent - net_stat1.packets_sent
    packets_recv = net_stat2.packets_recv - net_stat1.packets_recv
    dropin = net_stat2.dropin - net_stat1.dropin
    dropout = net_stat2.dropout - net_stat1.dropout
    utilization = ((bytes_sent + bytes_recv) / (1024 * 100)) * 100
    print(f"Adat küldés: {bytes_sent:.2f} Kbps")
    print(f"Adat fogadás: {bytes_recv:.2f} Kbps")
    print(f"Küldött csomagok: {packets_sent}")
    print(f"Fogadott csomagok: {packets_recv}")
    print(f"Hibásan fogadott csomagok: {dropin}")
    print(f"Hibásan küldött csomagok: {dropout}")
    print(f"Hálózat kihasználtság: {utilization:.2f}%")
interface_name = "Ethernet" 
monitor_network(interface_name)