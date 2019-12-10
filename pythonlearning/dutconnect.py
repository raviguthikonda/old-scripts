# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
import sys
import json
import stDutConnectUtils
import stConfigCommands
from jsonrpclib import Server
from pprint import pprint
############################################################
# DUT Configuration
############################################################

if len(sys.argv) > 1:
   switch_list = sys.argv[1:]
else:
   print "Error due to not having enough input arguments"
   sys.exit(0)
switch_name = switch_list[0]


def config_interfaces(switch_name,each):  
   switch = Server ("http://admin:@%s/command-api" % (switch_name))
   if switch_name == 'ol515':
      print "Connecting to %s..." % (switch_name)
      if each == '5/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.2.2/31"],"json")
      elif each == '6/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.2.0/31"],"json")
      elif each == '32/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.0.0/31"],"json")
      elif each == '64/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.0.2/31"],"json")
   elif switch_name == 'ol514':
      print "Connecting to %s..." % (switch_name)
      if each == '5/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.2.3/31"],"json")
      elif each == '6/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.2.1/31"],"json")
      elif each == '32/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.1.0/31"],"json")
      elif each == '31/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.1.2/31"],"json")
   elif switch_name == 'bh208':
      print "Connecting to %s..." % (switch_name)
      if each == '7/52/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.0.1/31"],"json")
      elif each == '8/52/1':
         switch.runCmds (1, ["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.0.3/31"],"json")
      elif each == '5/50/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.1.1/31"],"json")
      elif each == '5/49/1':
         switch.runCmds (1,["enable","configure","interface ethernet" + each ,"no switchport","ip address 11.0.1.3/31"],"json")


interfaces = {switch_list[0] : {'interface 1' : '5/1', 'interface 2' : '6/1', 'interface 3' : '32/1', 'interface 4' : '64/1'}, switch_list[1] : {'interface 1' : '5/1', 'interface 2' : '6/1', 'interface 3' : '31/1', 'interface 4' : '64/1'},switch_list[2] : {'interface 1' : '7/52/1', 'interface 2' : '8/52/1', 'interface 3' : '5/50/1', 'interface 4' : '5/49/1'}}

for key,value in interfaces.iteritems():
   for internal_key in value:
      interface_no =  interfaces[key][internal_key]
      config_interfaces(key,interface_no)
