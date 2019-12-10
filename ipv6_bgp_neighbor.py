# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
'''import json
import stDutConnectUtils
import stConfigCommands
from jsonrpclib import Server
from pprint import pprint

switch = Server ("http://admin:@%s/command-api" %(switch))
'''
ip_list = []
ip_list_neighbor = []
ipv6_list = []
ipv6_list_neighbor = []
lldp_ne = ["enable","show lldp neighbors | grep bn202"]
bgp = ["enable","configure","router bgp 100"]
bgp_ne = ["enable","configure","router bgp 200"]
address_family = ['enable','configure','router bgp 100','address-family ipv6']
address_family_neighbor = ['enable','configure','router bgp 200','address-family ipv6']
sh_lldp_raw = capiCmd(switch,lldp_ne,capiFormat='text')
#sh_lldp_raw = switch.runCmds(1,["enable","show lldp neighbors | grep ol515"],"text")  # output of show commands is a list of dictionaries
for each in sh_lldp_raw:
   if each['output'] != "":
      lldp_raw =  each['output']
      lldp_raw_wo_white_spaces =  lldp_raw.replace(" ","")
      lldp_raw_wo_ttl =  lldp_raw_wo_white_spaces.replace("120","")
      lldp_raw_wo_newline = lldp_raw_wo_ttl.split("\n")
      for each in lldp_raw_wo_newline:
         lldp_interfaces =  each.split("bn202.sjc.aristanetworks.com")
         if len(lldp_interfaces) > 1:
            self_interfaces = lldp_interfaces[0]
            neighbor_interface = lldp_interfaces[1]
            interface_self =  "interface " + self_interfaces
            ipv6_list.append(interface_self)
            ipv6_list.append("no switchport")
            '''interface_self_ip_address = "ip address 11.0.0." + str(i) + "/31"
            ipv6_list.append(interface_self_ip_address)
            '''
            interface_neighbor = "interface " + neighbor_interface
            ipv6_list_neighbor.append(interface_neighbor)
            ipv6_list_neighbor.append("no switchport")
            '''
            interface_neighbor_ip_address = "ip address 11.0.0." +str(i+1) + "/31"
            ipv6_list_neighbor.append(interface_neighbor_ip_address)
            '''
j = 2
for i in range(0,(len(ipv6_list)),2):
   ipv6 = "1000::" + str(i)
   interface_self_ip_address = "ipv6 address" + " " + ipv6 + "/127"
   #ipv6_list.insert(i+3,"no switchport")
   ipv6_list.insert(i+j,interface_self_ip_address)
   ipv6_neighbor = "1000::" + str(i+1)
   interface_neighbor_ip_address = "ipv6 address" + " " + ipv6_neighbor + "/127"
   #ipv6_list_neighbor.insert(i+3,"no switchport")
   ipv6_list_neighbor.insert(i+j,interface_neighbor_ip_address)
   bgp_neighbor_string = "neighbor " + ipv6_neighbor + " " + "remote-as 200"
   max_routes_zero = "neighbor " + ipv6_neighbor + " " + "maximum-routes 0"
   bgp_activate = "neighbor " + ipv6_neighbor + " " + "activate"
   bgp.append(bgp_neighbor_string)
   bgp.append(max_routes_zero)
   address_family.append(bgp_activate)
   bgp_neighbor_neighbor_string = "neighbor " + ipv6 + " " + "remote-as 100"
   max_routes_zero = "neighbor " + ipv6 + " " + "maximum-routes 0"
   bgp_neighbor_activate = "neighbor " + ipv6 + " " + "activate"
   bgp_ne.append(bgp_neighbor_neighbor_string)
   bgp_ne.append(max_routes_zero)
   address_family_neighbor.append(bgp_neighbor_activate)
   j = j+1
ipv6_list.insert(0,"enable")
ipv6_list.insert(1,"configure")

ipv6_list_neighbor.insert(0,"enable")
ipv6_list_neighbor.insert(1,"configure")
#print ipv6_list
#print ("-------------")
#print ipv6_list_neighbor
print bgp
print address_family
print bgp_ne
print address_family_neighbor
capiCmd(switch,ipv6_list)
capiCmd('bn202',ipv6_list_neighbor)
capiCmd(switch,bgp)
capiCmd('bn202',bgp_ne)
capiCmd(switch,address_family)
capiCmd('bn202',address_family_neighbor)
