from ipaddress import ip_network

network = ip_network("176.54.23.0/255.255.192.0", False)
cnt = 0
for ip in network:
    if f"{ip:b}".count('1') % 3 == 0:
        cnt += 1
print(cnt)
