from scapy.all import sniff, IP

def packet_handler(packet):
    if IP in packet:
        print("Source:", packet[IP].src)
        print("Destination:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)
        print("-" * 40)

# capture 10 packets
sniff(prn=packet_handler, count=10)

