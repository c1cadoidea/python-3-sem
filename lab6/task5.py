command1 = "switchport trunk allowed vlan 1,2,3,5,8"
command2 = "switchport trunk allowed vlan 1,3,8,9"

vlans1 = command1.split("allowed vlan ")[1].split(",")
vlans2 = command2.split("allowed vlan ")[1].split(",")

vlans_set1 = set(vlans1)
vlans_set2 = set(vlans2)
intersection = vlans_set1 & vlans_set2

result = list(intersection)

print(result)
