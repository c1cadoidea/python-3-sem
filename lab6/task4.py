config = "switchport trunk allowed vlan 1,3,10,20,30,100"
vlans_str = config.split("allowed vlan ")[1]
vlans_list = vlans_str.split(",")
print(vlans_list)
