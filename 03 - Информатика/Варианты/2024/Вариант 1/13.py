from ipaddress import ip_network

count = 0
mask = "255.224.0.0"
network = ip_network("177.32.0.0/11")
for ip in network:
    ip_bytes = str(ip).split('.')
    if len(set(ip_bytes)) == 3:
        print(ip, set(ip_bytes))
        count += 1
print(count - 2)