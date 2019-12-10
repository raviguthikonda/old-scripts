# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd
import ipaddr
#pbr configuration

switch = sys.argv[1]
print switch
pbr_name = sys.argv[4]
no_of_classmaps = int(sys.argv[2])
i = 0
j = 0
k = sys.argv[3]
pbr_list = ['enable','configure']
pmap = "policy-map type pbr " + pbr_name
pbr_list.append(pmap)
def pbr_config(count,pbr_name,class_name,acl_name,dest_ip):
   if "5100" in dest_ip:
      if count < 10000:
         #cmd1 = "policy-map type pbr " + pbr_name 
         #pbr_list.append(cmd1)
         cmd2 = str(count+1) + " " + "match ipv6 any " + dest_ip + " " + "set nexthop-group mpls"+ str(count) 
         pbr_list.append(cmd2)
      else:
         class_name = class_name + "_Mixed"
         acl_name = acl_name + "_Mixed"
         cmd2 = str(count+1) + " " + "class " + class_name
         pbr_list.append(cmd2)
         cmd3 = "set nexthop-group gre" + str(count)
         pbr_list.append(cmd3)
def class_acl_config(count,pbr_name,class_name,acl_name,dest_ip):
   class_name = class_name + "_Mixed"
   acl_name = acl_name + "_Mixed"
   cmd4 = "class-map type pbr match-any " + class_name
   pbr_list.append(cmd4)
   cmd5 = "match ip access-group " + acl_name
   pbr_list.append(cmd5)
   cmd6 = "ip access-list " + acl_name
   pbr_list.append(cmd6)
   cmd7 = "permit ip any " + dest_ip
   pbr_list.append(cmd7)
for n in range(0,no_of_classmaps):   
   print n
   class_name = "class_" + str(n)
   acl_name = "acl_" + str(n)
   ipv6_addr = ipaddr.IPv6Address(k+"::"+"0") + i
   print ipv6_addr
   dest_ip = str(ipv6_addr) + "/128"
   print dest_ip
   pbr_config(n,pbr_name,class_name,acl_name,dest_ip)
   i = i+1
i = 0
j = 0
k = sys.argv[3]
'''for n in range(0,2047):
   class_name = "class_" + str(n)
   acl_name = "acl_" + str(n)
   if i > 255:
      j = j+1
      i = 0
   dest_ip = "%s.0.%s.%s" %(str(k),str(j), str(i)) + "/32"
   class_acl_config(n,pbr_name,class_name,acl_name,dest_ip)
   i = i+1'''
#print pbr_list
capiCmd(switch,pbr_list)
