from ipaddress import ip_network

cnt = 0
network = ip_network("141.14.138.235/255.255.224.0", False)
for ip in network:
    octets = list(map(int, str(ip).split('.')))
    if all(o <= 200 for o in octets) and octets[-1] % 2 == 0 and octets[0] == 141:
        cnt += 1
print(cnt)
