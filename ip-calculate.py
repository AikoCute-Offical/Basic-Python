import ipaddress
from ipaddress import IPv4Address, IPv4Network

IP_Addr = ipaddress.ip_interface(input('Enter IP address in IP/Mask Form : '))

Net_Addr = IP_Addr.network
pref_len = IP_Addr.with_prefixlen
Mask = IP_Addr.with_netmask
wildcard = IP_Addr.hostmask
broadcast_address = Net_Addr.broadcast_address
gateway = Net_Addr.network_address + 1

classA = IPv4Network(("10.0.0.0", "255.0.0.0"))
classB = IPv4Network(("172.16.0.0", "255.240.0.0"))
classC = IPv4Network(("192.168.0.0", "255.255.0.0"))


print(chr(27) + "[2J")
print('IP_Address Short : ', IP_Addr)
print('Network Address : ', str(Net_Addr).split('/')[0])
print('Broadcast Address : ' , broadcast_address)
print('CIDR Notation : ', pref_len.split('/')[1])
print('Subnet Mask : ', Mask.split('/')[1])
print('Wildcard Mask : ' , wildcard)
print('First IP : ' , list(Net_Addr.hosts())[0])
print('Last IP : ' , list(Net_Addr.hosts())[-1])
print('IP Range : ' , list(Net_Addr.hosts())[0], ' - ', list(Net_Addr.hosts())[-1])
print('Number of Hosts : ' , Net_Addr.num_addresses - 2)
print('Default Gateway : ' , gateway)
if IP_Addr.network.network_address in classA:
    print('Belong Class : A')
elif IP_Addr.network.network_address in classB:
    print('Belong Class : B')
elif IP_Addr.network.network_address in classC:
    print('Class : C')
else:
    print('Class : D or E')