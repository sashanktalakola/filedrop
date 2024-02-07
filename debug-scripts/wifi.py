import socket
import ipaddress

def portScan(target_ip, target_port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            target_device_port_scan_result = s.connect_ex((target_ip, target_port))

            if target_device_port_scan_result == 0:
                return True
    except Exception as e:
        return False

def discoverDevices(method="port_scan", target_port=80, target_network="192.168.1.0/24"):
    
    for device_ip in ipaddress.IPv4Network(target_network):
        if portScan(str(device_ip), target_port):
            print(device_ip)
        else:
            print(device_ip, "No Available")
discoverDevices()
