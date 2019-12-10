# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from cliLib import capiCmd

#pbr configuration

switch = sys.argv[1]
print switch
pbr_name = sys.argv[4]
no_of_classmaps = int(sys.argv[2])
i = 0
j = 0
k = sys.argv[3]
pbr_list = ['enable','configure','policy-map type pbr '+ pbr_name]
def pbr_config(count,pbr_name,class_name,acl_name,dest_ip):
   if "51.0" in dest_ip:
      if count < 3073:
         cmd2 = "match ip any "+ dest_ip + " set nexthop  11.0.0.1 11.0.0.3 11.0.0.5 11.0.0.7 11.0.0.9 11.0.0.11 11.0.0.13 11.0.0.16"
         pbr_list.append(cmd2)
      else:
         class_name = class_name + "_Mixed"
         acl_name = acl_name + "_Mixed"
         cmd1 = "policy-map type pbr " + pbr_name
         pbr_list.append(cmd1)
         cmd2 = "class " + class_name
         pbr_list.append(cmd2)
         cmd3 = "set nexthop 11.0.0.21"
         pbr_list.append(cmd3)
         cmd4 = "class-map type pbr match-any " + class_name
         pbr_list.append(cmd4)
         cmd5 = "match ip access-group " + acl_name
         pbr_list.append(cmd5)
         cmd6 = "ip access-list " + acl_name
         pbr_list.append(cmd6)
         cmd7 = "permit ip any " + dest_ip
         pbr_list.append(cmd7)
for n in range(no_of_classmaps):   
   class_name = "class_" + str(n)
   acl_name = "acl_" + str(n)
   if i > 255:
      j = j+1
      i = 0
   dest_ip = "%s.0.%s.%s" %(str(k),str(j), str(i)) + "/32"
   pbr_config(n,pbr_name,class_name,acl_name,dest_ip)
   i = i+1
capiCmd(switch,pbr_list)
