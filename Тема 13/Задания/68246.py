from ipaddress import ip_address, ip_network

ip1 = ip_address('147.222.199.75')
ip2 = ip_address('147.222.222.147')

net = None
for mask in range(32, -1, -1):
    net1 = ip_network(f'{ip1}/{mask}', strict=False)
    net2 = ip_network(f'{ip2}/{mask}', strict=False)
    if net1 == net2:
        net = net1
        break

count = 0
for ip in net:
    if f'{ip:b}'.count('1') == 14:
        count += 1
print(count)

