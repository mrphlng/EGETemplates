from ipaddress import*
net = ip_network('105.224.200.224/255.255.255.224',0)
c = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1')%4 == 0:
        c += 1
print(c)