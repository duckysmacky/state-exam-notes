ip = "91.62.203.130"
net = "91.62.192.0"

print(f"ip: {ip}")
for n in map(int, ip.split('.')): print(bin(n)[2:])

print(f"\nnet: {net}")
for n in map(int, net.split('.')): print(bin(n)[2:])

# 11000000 - mask 3
# 11001011 - 203
# 11000000 - 130
# 2

# 00000000 - mask 4
# 10000010 - 192
# 00000000 - 0
# 0

print(8 + 8 + 2 + 0)