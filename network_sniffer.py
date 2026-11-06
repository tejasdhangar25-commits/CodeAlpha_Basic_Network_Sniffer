
from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw
from datetime import datetime

# Your active Ethernet interface
INTERFACE = r"\Device\NPF_{7408C3BA-E97A-491C-9314-57609598B8DF}"

packet_count = 0


def analyze_packet(packet):
    global packet_count

    if IP not in packet:
        return

    packet_count += 1

    source_ip = packet[IP].src
    destination_ip = packet[IP].dst

    source_port = "N/A"
    destination_port = "N/A"

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    else:
        protocol = "OTHER"

    if Raw in packet:
        payload = bytes(packet[Raw].load)
        payload_size = len(payload)
        payload_preview = payload[:32].hex()
    else:
        payload_size = 0
        payload_preview = "No payload"

    print("\n" + "=" * 55)
    print("PACKET NUMBER:", packet_count)
    print("=" * 55)

    print("Time             :", datetime.now())
    print("Source IP        :", source_ip)
    print("Destination IP   :", destination_ip)
    print("Protocol         :", protocol)
    print("Source Port      :", source_port)
    print("Destination Port :", destination_port)
    print("Payload Size     :", payload_size, "bytes")
    print("Payload Preview  :", payload_preview)

    print("=" * 55)


print("\n==========================================")
print("         BASIC NETWORK SNIFFER")
print("==========================================")
print("Interface: Ethernet")
print("Status: Capturing network packets...")
print("Press CTRL + C to stop.")
print("==========================================")

try:
    sniff(
        iface=INTERFACE,
        filter="ip",
        prn=analyze_packet,
        store=False
    )

except KeyboardInterrupt:
    print("\nNetwork Sniffer Stopped.")
    print("Total Packets Captured:", packet_count)

except Exception as error:
    print("\nError:", error)
