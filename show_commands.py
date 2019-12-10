# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd
switches = sys.argv[1:]
print len(switches)
for switch in switches:   
   show_commands = ['enable','configure','mkdir flash:' + switch,'show bfd neighbors vrf all > flash:' + switch + '/' + 'show_bfd_neighbors_vrf_all','show interfaces counters rates | nz > flash:' + switch + '/' + 'show_interfaces_counters_rates__nz','show ip bgp summary vrf all > flash:show_ip_bgp_summary_vrf_all','show ip ospf neighbor vrf all > flash:show_ip_ospf_neighbor_vrf_all','show ip rip neighbors vrf all > flash:show_ip_rip_neighbors_vrf_all','show ip route vrf default sum > flash:show_ip_route_vrf_default_summary','show vrrp all > flash:show_vrrp_all','show bfd neighbors vrf all detail > flash:show_bfd_neighbors_vrf_all_detail','show ip bgp detail vrf all > flash:show_ip_bgp_detail_vrf_all','show ip ospf database vrf all > flash:show_ip_ospf_database_vrf_all','show ip rip database vrf all > flash:show_ip_rip_database_vrf_all','show ip route vrf all > flash:show_ip_route_vrf_all','show platform sand l3 summary > flash:show_platform_sand_l3_summary','show vrrp vrf all brief all > flash:show_vrrp_vrf_all_brief_all']
   print show_commands
   '''capiCmd(each,clear_counters)'''
