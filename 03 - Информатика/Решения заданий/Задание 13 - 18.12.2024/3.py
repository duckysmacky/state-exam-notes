from ipaddress import ip_network

network = ip_network("142.96.56.118/255.255.255.240", False)
cnt = 0
for ip in network:
    left = f"{ip:b}"[:16].count('1')
    right = f"{ip:b}"[16:].count('1')
    if right > left:
        cnt += 1
print(cnt)
