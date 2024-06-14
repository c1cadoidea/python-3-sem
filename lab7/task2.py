mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]

mac_cisco = []

for address in mac:
    groups = address.split(":")
    cisco_address = ".".join(groups)
    mac_cisco.append(cisco_address)

print("MAC-адреси у форматі Cisco:")
for cisco_addr in mac_cisco:
    print(cisco_addr)
