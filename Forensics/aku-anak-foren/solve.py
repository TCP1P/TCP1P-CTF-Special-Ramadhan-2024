import pyshark

fc = pyshark.FileCapture("./capture.pcap")

def extract_http_requests(packet):
    if 'HTTP' in packet and hasattr(packet.http, 'request_method'):
        return packet

for packet in fc:
    http_data = extract_http_requests(packet)
    if http_data:
        if "urlencoded-form" in http_data:
            print(http_data["urlencoded-form"].key, end="")
