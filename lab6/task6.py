ospf_route = " 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

parts = ospf_route.split()

prefix = parts[0]
ad_metric = parts[1].strip("[]")
next_hop = parts[3].strip(",")
last_update = parts[4].strip(",")
outbound_interface = parts[5]

output = f"""
Prefix                {prefix}
AD/Metric             {ad_metric}
Next-Hop              {next_hop}
Last update           {last_update}
Outbound Interface    {outbound_interface}
"""

print(output)
