from scapy.all import rdpcap
packets = rdpcap("network_capture.pcap")
for packet in packets:
    if packet.haslayer("IP"):
        print("Source IP:", packet["IP"].src)
        print("Destination IP:", packet["IP"].dst)
    if packet.haslayer("TCP"):
        print("Source Port:", packet["TCP"].sport)
        print("Destination Port:", packet["TCP"].dport)
    print("\n")