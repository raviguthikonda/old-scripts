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
               ip_list.append("no switchport")
   j = 2
   l = 0
   k = 0
   #print ip_list
   for i in range(0,(len(ip_list)),2):
      if k >=256:
         k = 0
         l = l+1
      interface_self_ip_address = "ip address 11." + str(n) + "." + str(l) + "." + str(k) + "/31"
      ip_list.insert(i+j,interface_self_ip_address)  #insert the ip address in the i+j th position of the list
      j = j+1
      k = k+1
   ip_list.insert(0,"enable")
   ip_list.insert(1,"configure")
   #print ip_list
   capiCmd(switch,ip_list)
