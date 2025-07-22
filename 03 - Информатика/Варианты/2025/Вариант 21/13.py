import ipaddress

for A in range(0, 256):
    net = ipaddress.ip_network(f"250.113.{A}.197/255.255.255.192", False)
    for ip in net:
        ip2 = f'{ip:b}'
        left = ip2[:16].count('1')
        right = ip2[16:].count('1')
        if not (left >= right): break
    else:
        print(A)