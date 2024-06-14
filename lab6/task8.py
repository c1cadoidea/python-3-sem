def ip_to_columns(ip):
    bytes_ip = ip.split('.')
    
    decimal_bytes = [int(byte) for byte in bytes_ip]
    
    binary_bytes = [bin(int(byte))[2:].zfill(8) for byte in bytes_ip]
    
    decimal_row = ''.join(f'{byte:<10}' for byte in decimal_bytes)
    binary_row = ''.join(f'{byte:<10}' for byte in binary_bytes)
    
    print(decimal_row)
    print(binary_row)

ip = "192.168.3.1"
ip_to_columns(ip)
