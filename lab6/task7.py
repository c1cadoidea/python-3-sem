mac = "AAAA:BBBB:CCCC"
mac_clean = mac.replace(":", "")
binary_mac = "".join(format(int(digit, 16), "08b") for digit in mac_clean)
print(binary_mac)
