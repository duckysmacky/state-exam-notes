from ipaddress import ip_network

for x in range(0, 9):
    A = int('1' * x + '0' * (8 - x), 2)
    net = ip_network(f"108.8.190.123/255.255.{A}.0", False)
    for ip in net:
        ip2 = f"{ip:b}"
        left = ip2[:16].count('1')
        right = ip2[16:].count('1')
        if not left <= right:
            break
    else:
        print(A)
        break
