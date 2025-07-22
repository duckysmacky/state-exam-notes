import ipaddress as ip

addr = ip.ip_address("185.49.34.122")
for network_bits in range(32 + 1):
    net = ip.ip_network(f"185.49.32.0/{network_bits}", False)
    if addr in net:
        print(net.netmask)