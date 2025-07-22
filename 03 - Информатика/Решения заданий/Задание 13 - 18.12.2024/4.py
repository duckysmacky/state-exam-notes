from ipaddress import ip_network

cnt = 0
for A in range(256):
    network = ip_network(f"207.0.{A}.163/255.255.255.192", False)
    for ip in network:
        left = f"{ip:b}"[:16].count('0')
        right = f"{ip:b}"[16:].count('0')
        if not (left > right): break
    else:
        cnt += 1
print(cnt)
