import bluetooth

def discoverDevices(duration=10):
    nearby_devices = bluetooth.discover_devices(duration=duration, lookup_names=True, lookup_class=True)

    formatted_nearby_devices = []

    if nearby_devices:
        for mac_address, device_name, device_class in nearby_devices:
            formatted_nearby_devices.append(
                    {
                        "mac_address": mac_address,
                        "device_name": device_name,
                        "device_class": device_class
                    }
                )

    return formatted_nearby_devices
