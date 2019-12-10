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
sh_lldp_raw = capiCmd(switch,lldp_ne,capiFormat='text')
#sh_lldp_raw = switch.runCmds(1,["enable","show lldp neighbors | grep ol515"],"text")  # output of show commands is a list of dictionaries
po = 1
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
            ipv6_list.append("no ipv6 address")
            ipv6_list.append("channel-group" + " " + str(po) + " " + "mode on")
            '''interface_self_ip_address = "ip address 11.0.0." + str(i) + "/31"
            ipv6_list.append(interface_self_ip_address)
            '''
            interface_neighbor = "interface " + neighbor_interface
            ipv6_list_neighbor.append(interface_neighbor)
            ipv6_list_neighbor.append("no switchport")
            ipv6_list_neighbor.append("no ipv6 address")
            ipv6_list_neighbor.append("channel-group" + " " + str(po) + " " + "mode on")
            '''
            interface_neighbor_ip_address = "ip address 11.0.0." +str(i+1) + "/31"
            ipv6_list_neighbor.append(interface_neighbor_ip_address)
            '''
            po = po+1
j = 1
po = po-1
k = 0
for i in range(0,po):
   interface_self_ip_address = "ipv6 address 1000::" + str(k) + "/127"
   #ipv6_list.insert(i+3,"no switchport")
   ipv6_list.append("interface port-channel" + " " + str(j))
   ipv6_list.append(interface_self_ip_address)
   interface_neighbor_ip_address = "ipv6 address 1000::" + str(k+1) + "/127"
   #ipv6_list_neighbor.insert(i+3,"no switchport")
   ipv6_list_neighbor.append("interface port-channel" + " " + str(j))
   ipv6_list_neighbor.append(interface_neighbor_ip_address)
   j = j+1
   k = k+2
ipv6_list.insert(0,"enable")
ipv6_list.insert(1,"configure")

ipv6_list_neighbor.insert(0,"enable")
ipv6_list_neighbor.insert(1,"configure")
print ipv6_list
print ("-------------")
print ipv6_list_neighbor
capiCmd(switch,ipv6_list)
capiCmd('bn202',ipv6_list_neighbor)
