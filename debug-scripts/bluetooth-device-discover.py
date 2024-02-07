import bluetooth

nearby_devices = bluetooth.discover_devices(duration=10, lookup_names=True, lookup_class=True)

if nearby_devices:
	print("Nearby Devices:")
	for addr, name, _ in nearby_devices:
		print(f"Device Name: {name}, Address: {addr}, Class: {_}")
else:
	print("No nearby devices found.")
