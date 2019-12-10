# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
import itertools #package to join list of lists
from cliLib import capiCmd

switch = sys.argv[1]
no_of_linecards = int(sys.argv[2])
lldp_list = []
lldp_list1= []
for n in range(3,no_of_linecards):
   ip_list = []
   lldp_ne = ["enable","show lldp neighbors | grep "+ switch]
   sh_lldp_raw = capiCmd(switch,lldp_ne,capiFormat='text')  #output of sh_lldp_raw is of type list
   #print sh_lldp_raw
   #print type(sh_lldp_raw)
   #print len(sh_lldp_raw)
   for each in sh_lldp_raw:
      if each['output'] != "":
         lldp_raw =  each['output']
         #print lldp_raw
         #print type(lldp_raw)
         lldp_raw_wo_white_spaces =  lldp_raw.replace(" ","")
         #print lldp_raw_wo_white_spaces
         lldp_raw_wo_ttl =  lldp_raw_wo_white_spaces.replace("120","")
         lldp_raw_wo_newline = lldp_raw_wo_ttl.split("\n")
         #print lldp_raw_wo_newline
         #print type(lldp_raw_wo_newline)
         #print len(lldp_raw_wo_newline)
         for each in lldp_raw_wo_newline:
            lldp_interfaces =  each.split(switch+".sjc.aristanetworks.com")
            #print lldp_interfaces
            lldp_list.append(lldp_interfaces)  #

   lldp_list.pop(-1)
   #print lldp_list
   for i in range(0,len(lldp_list)/2): #lldp output gives two cli outputs for each intf, one from one side(Et1-Et2) and the other from other side(Et2-Et1). This loop deletes one of them.
      lldp_list.pop(i+1)  #this list of lists contains all the intf's from lldp output that need to configured for snake
   #print lldp_list
   lldp_single_list = list(itertools.chain.from_iterable(lldp_list)) #combine list of lists into single list
  # print lldp_single_list
   lldp_single_list.insert(0,'Et8/1/1')
   lldp_single_list.append('Et8/36/1')
   #print lldp_single_list
   vlan = 2
   snake_config_list = ['enable','configure']
   if len(lldp_single_list)%4 == 0:
      for i in range(0,len(lldp_single_list),4):
         print i
         snake_config_list.append('interface' + " " + lldp_single_list[i] + ',' + lldp_single_list[i+2])
         snake_config_list.append('switchport access vlan %d' %vlan)
         snake_config_list.append('interface' + " " + lldp_single_list[i+1] + ',' + lldp_single_list[i+3])
         snake_config_list.append('switchport access vlan %d' %(vlan+1))
         vlan = vlan+2
      #print snake_config_list
   else:
      for i in range(0,len(lldp_single_list),2):
         print 'interface' + " " + lldp_single_list[i] + ',' +  lldp_single_list[i+1]
         print 'switchport access vlan 2'
   print snake_config_list
   capiCmd(switch,snake_config_list)
