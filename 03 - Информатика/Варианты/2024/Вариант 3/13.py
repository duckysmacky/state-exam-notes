import ipaddress as ip

ipaddr = ip.ip_address("172.49.54.172")

for m in range(16, 32 + 1):
    network = ip.ip_network(f"172.49.48.0/{m}", strict=False)
    if ipaddr in network.hosts():
        print(network.netmask)