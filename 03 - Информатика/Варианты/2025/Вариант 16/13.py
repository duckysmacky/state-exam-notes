from ipaddress import ip_network

for n in range(0, 9):
    b = '1' * n + '0' * (8 - n)
    A = int(b, 2)
    net = ip_network(f"255.211.33.160/255.255.{A}.0", False)
    for ip in net:
        ip2 = f'{ip:b}'
        left = ip2[:16].count('1')
        right = ip2[16:].count('1')
        if not left >= right:
            break
    else:
        print(A)
        break
