from ipaddress import ip_network

cnt = 0
network = ip_network("252.32.33.87/255.255.0.0", False)
for ip in network:
    ip = f"{ip:b}"
    left = ip[:16].count("1")
    right = ip[16:].count("1")
    if right > 2 * left:
        cnt += 1
print(cnt)
