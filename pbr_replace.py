# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
no_of_flaps = int(sys.argv[2])
t = int(sys.argv[3])
#shut_list1 = ["enable","configure","interface ethernet 4/2/1-4/9/1,4/25/1,4/26/1,4/28/1-4/35/1","speed forced 40gfull"]
#noshut_list1 =  ["enable","configure","interface ethernet 4/2/1-4/9/1,4/25/1,4/26/1,4/28/1-4/35/1","speed auto 40gfull"]
shut_list2 = ["enable","configure","interface vlan 201","service-policy type pbr input pbr-6100"]
noshut_list2 =  ["enable","configure","interface vlan 201","service-policy type pbr input pbr-61000"]
shut_list1 = ["enable","configure","interface ethernet 4/24/1.1","service-policy type pbr input pbr-7100"]
noshut_list1 =  ["enable","configure","interface ethernet 4/24/1.1","service-policy type pbr input pbr-71000"]
shut_list3 = ["enable","configure","interface vlan 203","service-policy type pbr input pbr-8100"]
noshut_list3 =  ["enable","configure","interface vlan 203","service-policy type pbr input pbr-81000"]
shut_list5 = ["enable","configure","interface ethernet 4/10/1","service-policy type pbr input pbr-5100"]
noshut_list5 =  ["enable","configure","interface ethernet 4/10/1","service-policy type pbr input pbr-51000"]
shut_list6 = ["enable","configure","interface port-channel 1","no service-policy type pbr input pbr-82000"]
noshut_list6 =  ["enable","configure","interface port-channel 1","service-policy type pbr input pbr-82000"]
for i in range (0,no_of_flaps):
   capiCmd(switch,shut_list2)
   capiCmd(switch,shut_list3)
   capiCmd(switch,shut_list5)
   capiCmd(switch,shut_list6)
   time.sleep(t)
   capiCmd(switch,noshut_list2)
   capiCmd(switch,noshut_list3)
   capiCmd(switch,noshut_list5)
   capiCmd(switch,noshut_list6)
   time.sleep(t)
