# from ipaddress import IPv4Address, IPv6Address, AddressValueError

with open('lol.txt') as my_file:
	iptables_array = my_file.readlines()

output_file = open("iptables.j2", "w")

with open("iptables.j2", "w") as output:
	output_file.write("IPTable Rule for host\n")
	for entry in iptables_array:
		output_file.write("-A Firewall-1-INPUT -s " + entry.replace('\n','') + " -p tcp --dport 22 -j ACCEPT\n")

output_file.close()
