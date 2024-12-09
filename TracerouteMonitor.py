import time
from datetime import datetime
from scapy.all import IP, ICMP, sr1
def traceroute(destination, max_hops):
    ttl = 1
    while ttl <= max_hops:
        packet = IP(dst=destination, ttl=ttl) / ICMP()

        start_time = time.time()
        reply = sr1(packet, verbose=False, timeout=1)

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if reply is None:
            print(f"{ttl}. * * *   {current_time}")
        elif reply.haslayer(ICMP) and reply.getlayer(ICMP).type == 0:
            print(f"{ttl}. {reply.src}   {current_time} {round((time.time() - start_time) * 1000, 2)} ms")
            break
        else:
            print(f"{ttl}. {reply.src}   {current_time} {round((time.time() - start_time) * 1000, 2)} ms")
        ttl += 1
destination = "8.8.8.8"
max_hops = 30
traceroute(destination, max_hops)

