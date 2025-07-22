from ipaddress import ip_network

network = ip_network("192.168.32.160/255.255.255.240")
cnt = 0
for ip in network:
    if f"{ip:b}".count('1') % 2 != 0:
        cnt += 1
print(cnt)
