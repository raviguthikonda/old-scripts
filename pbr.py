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
pbr_list = ['enable','configure','policy-map type pbr ' + pbr_name]
classmap_list = ['enable','configure']
def pbr_config(pbr_name,class_name,acl_name,dest_ip):
   if "50.0" in dest_ip:
      class_name = class_name + "_Dest1"
      acl_name = acl_name + "_Dest1"
      cmd2 = "class " + class_name 
      pbr_list.append(cmd2)
      #cmd3 = "set nexthop 11.0.2.5 11.0.2.7"
      cmd3 = "set nexthop 11.0.0.1 11.0.0.3 11.0.0.5 11.0.0.7 11.0.0.9 11.0.0.11 11.0.0.13 11.0.0.15 11.0.0.17 11.0.0.19 11.0.0.21 11.0.0.23 11.0.0.25 11.0.0.27 11.0.0.29 11.0.0.31 11.0.0.33 11.0.0.35 11.0.0.37 11.0.0.39 11.0.0.41 11.0.0.43 11.0.0.45 11.0.0.47 11.0.0.49 11.0.0.51 11.0.0.53 11.0.0.55 11.0.0.57 11.0.0.59 11.0.0.61 11.0.0.63 11.0.0.65 11.0.0.67 11.0.0.69 11.0.0.71 11.0.0.73 11.0.0.75 11.0.0.77 11.0.0.79 11.0.0.81 11.0.0.83 11.0.0.85 11.0.0.87 11.0.0.89 11.0.0.91 11.0.0.93 11.0.0.95 11.0.0.97 11.0.0.99 11.0.0.101 11.0.0.103 11.0.0.105 11.0.0.107 11.0.0.109 11.0.0.111 11.0.0.113 11.0.0.115 11.0.0.117 11.0.0.119 11.0.0.121 11.0.0.123 11.0.0.125 11.0.0.127 11.0.0.129 11.0.0.131 11.0.0.133 11.0.0.135 11.0.0.137 11.0.0.139 11.0.0.141 11.0.0.143 11.0.0.145 11.0.0.147 11.0.0.149 11.0.0.151 11.0.0.153 11.0.0.155 11.0.0.157 11.0.0.159 11.0.0.161 11.0.0.163 11.0.0.165 11.0.0.167 11.0.0.169 11.0.0.171 11.0.0.173 11.0.0.175 11.0.0.177 11.0.0.179 11.0.0.181 11.0.0.183 11.0.0.185 11.0.0.187 11.0.0.189 11.0.0.191 11.0.0.193 11.0.0.195 11.0.0.197 11.0.0.199 11.0.0.201 11.0.0.203 11.0.0.205 11.0.0.207 11.0.0.209 11.0.0.211 11.0.0.213 11.0.0.215 11.0.0.217 11.0.0.219 11.0.0.221 11.0.0.223 11.0.0.225 11.0.0.227 11.0.0.229 11.0.0.231 11.0.0.233 11.0.0.235 11.0.0.237 11.0.0.239 11.0.0.241 11.0.0.243 11.0.0.245 11.0.0.247 11.0.0.249 11.0.0.251 11.0.0.253 11.0.0.255"
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      classmap_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      classmap_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      classmap_list.append(cmd6)
      cmd7 = "permit ip any " + dest_ip
      classmap_list.append(cmd7)
   if "51.0" in dest_ip:
      class_name = class_name + "_Dest2"
      acl_name = acl_name + "_Dest2"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      #cmd3 = "set nexthop recursive 11.0.3.1 11.0.3.3"
      #cmd3 = "set nexthop 11.0.0.1 11.0.0.3 11.0.0.5 11.0.0.7 11.0.0.9 11.0.0.13 11.0.0.11 11.0.0.15"
      cmd3 = "set nexthop 11.0.0.1 11.0.0.3 11.0.0.5 11.0.0.7 11.0.0.9 11.0.0.11 11.0.0.13 11.0.0.15 11.0.0.17 11.0.0.19 11.0.0.21 11.0.0.23 11.0.0.25 11.0.0.27 11.0.0.29 11.0.0.31 11.0.0.33 11.0.0.35 11.0.0.37 11.0.0.39 11.0.0.41 11.0.0.43 11.0.0.45 11.0.0.47 11.0.0.49 11.0.0.51 11.0.0.53 11.0.0.55 11.0.0.57 11.0.0.59 11.0.0.61 11.0.0.63 11.0.0.65 11.0.0.67 11.0.0.69 11.0.0.71 11.0.0.73 11.0.0.75 11.0.0.77 11.0.0.79 11.0.0.81 11.0.0.83 11.0.0.85 11.0.0.87 11.0.0.89 11.0.0.91 11.0.0.93 11.0.0.95 11.0.0.97 11.0.0.99 11.0.0.101 11.0.0.103 11.0.0.105 11.0.0.107 11.0.0.109 11.0.0.111 11.0.0.113 11.0.0.115 11.0.0.117 11.0.0.119 11.0.0.121 11.0.0.123 11.0.0.125 11.0.0.127 11.0.0.129 11.0.0.131 11.0.0.133 11.0.0.135 11.0.0.137 11.0.0.139 11.0.0.141 11.0.0.143 11.0.0.145 11.0.0.147 11.0.0.149 11.0.0.151 11.0.0.153 11.0.0.155 11.0.0.157 11.0.0.159 11.0.0.161 11.0.0.163 11.0.0.165 11.0.0.167 11.0.0.169 11.0.0.171 11.0.0.173 11.0.0.175 11.0.0.177 11.0.0.179 11.0.0.181 11.0.0.183 11.0.0.185 11.0.0.187 11.0.0.189 11.0.0.191 11.0.0.193 11.0.0.195 11.0.0.197 11.0.0.199 11.0.0.201 11.0.0.203 11.0.0.205 11.0.0.207 11.0.0.209 11.0.0.211 11.0.0.213 11.0.0.215 11.0.0.217 11.0.0.219 11.0.0.221 11.0.0.223 11.0.0.225 11.0.0.227 11.0.0.229 11.0.0.231 11.0.0.233 11.0.0.235 11.0.0.237 11.0.0.239 11.0.0.241 11.0.0.243 11.0.0.245 11.0.0.247 11.0.0.249 11.0.0.251 11.0.0.253 11.0.0.255"
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      classmap_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      cmd5 = "10 match ip access-group " + acl_name 
      classmap_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      classmap_list.append(cmd6)
      cmd7 = "10 permit ip any " + dest_ip
      classmap_list.append(cmd7)
   if "60.0" in dest_ip:
      class_name = class_name + "_Dest3"
      acl_name = acl_name + "_Dest3"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      cmd3 = "set nexthop 11.0.2.9 11.0.2.11"
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      pbr_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      pbr_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      pbr_list.append(cmd6)
      cmd7 = "permit ip any " + dest_ip
      pbr_list.append(cmd7)
   if "61.0" in dest_ip:
      class_name = class_name + "_Dest4"
      acl_name = acl_name + "_Dest4"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      cmd3 = "set nexthop 11.0.2.13 11.0.2.15 "
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      pbr_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      pbr_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      pbr_list.append(cmd6)
      cmd7 = "permit ip any " + dest_ip
      pbr_list.append(cmd7)   
   if "52.0" in dest_ip:
      class_name = class_name + "_Dest5"
      acl_name = acl_name + "_Dest5"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      cmd3 = "set nexthop  15.0.0.5"
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      pbr_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      pbr_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      pbr_list.append(cmd6)
      cmd7 = "permit ip any " + dest_ip
      pbr_list.append(cmd7)
   if "53.0" in dest_ip:
      class_name = class_name + "_Dest7"
      acl_name = acl_name + "_Dest7"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      cmd3 = "set nexthop 11.0.1.0"
      pbr_list.append(cmd3)
      cmd4 = "class-map type pbr match-any " + class_name
      pbr_list.append(cmd4)
      cmd5 = "match ip access-group " + acl_name
      pbr_list.append(cmd5)
      cmd6 = "ip access-list " + acl_name
      pbr_list.append(cmd6)
      cmd7 = "permit ip any " + dest_ip
      pbr_list.append(cmd7)
   if "54.0" in dest_ip:
      class_name = class_name + "_Dest8"
      acl_name = acl_name + "_Dest8"
      cmd2 = "class " + class_name
      pbr_list.append(cmd2)
      cmd3 = "set nexthop 11.0.1.0"
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
   pbr_config(pbr_name,class_name,acl_name,dest_ip)
   i = i+1
#capiCmd(switch,classmap_list)
capiCmd(switch,pbr_list)
