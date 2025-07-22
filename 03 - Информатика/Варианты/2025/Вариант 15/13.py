from ipaddress import ip_network, ip_address

ip1 = ip_address("211.115.61.154")
ip2 = ip_address("211.115.59.137")
for b in range(0, 9):
    byte = 16 + b
    net = ip_network(f"211.115.59.0/{byte}", False)
    ips = list(net)
    if ip1 in ips and ip2 in ips:
        print(net.netmask)
