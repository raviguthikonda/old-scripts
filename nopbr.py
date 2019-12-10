# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.





import sys
import json
import stDutConnectUtils
import stConfigCommands
from jsonrpclib import Server
from pprint import pprint

#pbr configuration

switch_name = sys.argv[1]
switch = Server ("http://admin:@%s/command-api" %(switch_name))
pbr_name = "pbr-0"
no_of_classmaps = int(sys.argv[2])
def pbr_config(class_name,acl_name):
   #switch.runCmds (1,["enable","configure","no policy-map type pbr pbr-script"],"json")
   switch.runCmds(1,["enable","configure","no class-map type pbr match-any " + class_name],"json")
   
   #switch.runCmds(1,["enable","configure","no ip access-list " + acl_name],"json")
for i in range(no_of_classmaps):
   class_name = "class_" + str(i)
   #acl_name = "acl_" + str(i)
   pbr_config(class_name,acl_name)
