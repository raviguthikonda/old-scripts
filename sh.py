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
for i in range(3,11):
   Linecard = "Linecard" + str(i)
   if (i == 3 or i == 10):
      NoOfEntries =  switch.runCmds(1,["enable","show platform trident tcam pbr detail | grep Linecard" + str(i) + "/0 -wc"],"text")  # output of show commands is a list of dictionaries
      print Linecard + "/0" + "    " + NoOfEntries[1]['output'].strip()
      NoOfEntries =  switch.runCmds(1,["enable","show platform trident tcam pbr detail | grep Linecard" + str(i) + "/1 -wc"],"text")  # output of show commands is a list of dictionaries
      print Linecard + "/1" + "    " + NoOfEntries[1]['output'].strip()
   else:
      NoOfEntries =  switch.runCmds(1,["enable","show platform trident tcam pbr detail | grep Linecard" + str(i) + "/0 -wc"],"text")  # output of show commands is a list of dictionaries
      print Linecard + "      " +  NoOfEntries[1]['output'].strip() 
   
