from ipaddress import *
for m in range(32, -1, -1):
    net1 = ip_network(f'84.77.47.132/{m}', False)
    net2 = ip_network(f'84.77.48.132/{m}', False)
    if net1 == net2:
        print(net1.netmask)
        break