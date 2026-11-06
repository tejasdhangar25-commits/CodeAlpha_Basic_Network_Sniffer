# 🛡️ Basic Network Sniffer

A Python-based network packet capturing and analysis tool developed using **Scapy**.

This project captures live network traffic and displays useful packet information, including IP addresses, protocols, port numbers, and payload previews.

## 🚀 Features

- Live network packet capturing
- Source and destination IP address detection
- TCP, UDP and ICMP protocol identification
- Source and destination port detection
- Packet payload size analysis
- Hexadecimal payload preview
- Packet timestamps
- Real-time packet information display

## 🛠️ Technologies Used

- Python
- Scapy
- Npcap
- Git and GitHub

## 💻 Requirements

- Windows 10/11
- Python 3.x
- Scapy
- Npcap

## 📥 Installation

**1. Clone the repository**

```bash
git clone https://github.com/tejasdhangar25-commits/CodeAlpha_Basic_Network_Sniffer.git
```

**2. Navigate to the project directory**

```bash
cd CodeAlpha_Basic_Network_Sniffer
```

**3. Install Scapy**

```bash
pip install scapy
```

**4. Install Npcap**

Download and install Npcap:

https://npcap.com/

## ▶️ How to Run

Open the terminal in your project directory and execute:

```bash
python network_sniffer.py
```

On Windows, run the terminal as Administrator if packet capture requires elevated permissions.

## 📊 Sample Output

```text
PACKET NUMBER: 1

Source IP        : 192.168.31.162
Destination IP   : 1.1.1.1
Protocol         : ICMP
Source Port      : N/A
Destination Port : N/A
Payload Size     : 0 bytes
Payload Preview  : No payload
```

## 🔐 Important Notes

- Use this tool only on networks and devices you own or have permission to monitor.
- HTTPS traffic is encrypted using TLS. This tool displays packet metadata and captured bytes, not decrypted website content.
- Packet capture may require administrator privileges on Windows.

## 🎯 Project Objective

The objective of this project is to understand network communication, packet structures, IP addressing, transport-layer protocols, and basic network traffic analysis.

## 👨‍💻 Developer

**Tejas Bagul**

GitHub: https://github.com/tejasdhangar25-commits

## 📜 License

This project is available for educational and learning purposes.
