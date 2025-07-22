from ipaddress import ip_network

cnt = 0
network = ip_network("176.54.23.0/255.255.224.0", False)
for ip in network:
    if str(ip).count('2') % 3 == 0:
        cnt += 1
print(cnt)
