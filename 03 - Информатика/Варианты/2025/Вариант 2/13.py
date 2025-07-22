from ipaddress import ip_network, ip_address

network = ip_network("200.33.100.0/255.255.248.0", False)
cnt = 0
for ip in network:
    if f"{ip:b}".count('1') % 7 != 0:
        print(ip, "{ip:b}")
        cnt += 1
print(cnt)
