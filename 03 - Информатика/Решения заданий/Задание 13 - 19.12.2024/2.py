from ipaddress import ip_network

cnt = 0
network = ip_network("181.165.17.108/255.255.192.0", False)
for ip in network:
    if f"{ip:b}".count("0") % 9 == 0:
        cnt += 1
print(cnt)
