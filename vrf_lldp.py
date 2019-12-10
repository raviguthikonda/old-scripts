# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
no_of_linecards = int(sys.argv[2])

for n in range(3,no_of_linecards):
   ip_list = []
   lldp_ne = ["enable","show lldp neighbors | grep Et" + str(n) + "/"]
   sh_lldp_raw = capiCmd(switch,lldp_ne,capiFormat='text')
   for each in sh_lldp_raw:
      if each['output'] != "":
         lldp_raw =  each['output']
         lldp_raw_wo_white_spaces =  lldp_raw.replace(" ","")
         lldp_raw_wo_ttl =  lldp_raw_wo_white_spaces.replace("120","")
         lldp_raw_wo_newline = lldp_raw_wo_ttl.split("\n")
         for each in lldp_raw_wo_newline:
            lldp_interfaces =  each.split("bn201.sjc.aristanetworks.com")
            if len(lldp_interfaces) > 1:
               self_interfaces = lldp_interfaces[0]
               neighbor_interface = lldp_interfaces[1]
               interface_self =  "interface " + self_interfaces
               ip_list.append(interface_self)
   del ip_list[0]
   #print ip_list
   j = 1
   k = 2
   for i in range(0,(len(ip_list)/2)):
      vrf_config_string = "vrf forwarding vrf-" + str(k)
      ip_list.insert(j,vrf_config_string)
      j = j+2
      ip_list.insert(j,vrf_config_string)
      j = j+2
      k = k+1
   print ip_list
   ip_list.insert(0,"enable")
   ip_list.insert(1,"configure")
   capiCmd(switch,ip_list)
