from ipaddress import ip_network

cnt = 0
network = ip_network("231.168.192.196/255.255.255.240", False)
for ip in network:
    if f"{ip:b}".count("1") % 2 != 0:
        cnt += 1
print(cnt)
