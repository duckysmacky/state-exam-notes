import ipaddress

net = ipaddress.ip_network('142.108.56.118/255.255.255.240', False)
cnt = 0
for ip in net:
    ip2 = f"{ip:b}"
    left = ip2[:16].count('1')
    right = ip2[16:].count('1')
    if left < right:
        cnt += 1
print(cnt)
