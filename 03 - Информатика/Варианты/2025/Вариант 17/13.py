from ipaddress import ip_network

for A in range(0, 256):
    net = ip_network(f"250.113.{A}.197/255.255.255.192", False)
    for ip in net:
        ip2 = f"{ip:b}"
        left = ip2[:16].count('1')
        right = ip2[16:].count('1')
        f = left >= right
        if not f: break
    else:
        print(A)
