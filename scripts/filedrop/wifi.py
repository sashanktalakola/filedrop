import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor


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
    
    discovered_devices = []

    for device_ip in ipaddress.IPv4Network(target_network):
        if portScan(str(device_ip), target_port):
            discovered_devices.append(
                    {
                        "ip_address": device_ip
                    }
                )
    return discovered_devices

def discoverDevices2(method="port_scan", target_port=80, target_network="192.168.1.0/24"):

    discovered_devices = []

    def scanDevice(device_ip):
        if portScan(str(device_ip), target_port):
            return { "ip_address": device_ip }
        else:
            return None

    with ThreadPoolExecutor() as executor:

        future_results = {executor.submit(scanDevice, device_ip): device_ip for device_ip in ipaddress.IPv4Network(target_network)}

        for future_result in future_results:
            result = future_result.result()

            if result:
                discovered_devices.append(result)
    return discovered_devices
