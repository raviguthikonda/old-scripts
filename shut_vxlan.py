# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from arstCliLib import capiCmd
switch = sys.argv[1]
switch1 = sys.argv[2]
no_of_flaps = int(sys.argv[3])
t = int(sys.argv[4])
#shut_list1 = ["enable","configure","interface ethernet 3/1/1-4,3/13/1-4,4/2/1-4,4/14/1-4,5/3/1-4,5/15/1-4,6/4/1-4,7/5/1-4,8/6/1-4,9/7/1-4,10/8/1-4,11/9/1-4,12/10/1-4,13/11/1-4,14/12/1-4","shutdown"]
#noshut_list1 = ["enable","configure","interface ethernet 3/1/1-4,3/13/1-4,4/2/1-4,4/14/1-4,5/3/1-4,5/15/1-4,6/4/1-4,7/5/1-4,8/6/1-4,9/7/1-4,10/8/1-4,11/9/1-4,12/10/1-4,13/11/1-4,14/12/1-4","no shutdown"]
#shut_list1 = ["enable","configure","interface port-channel 1-64","shutdown"]
#noshut_list1 =  ["enable","configure","interface port-channel 1-64","no shutdown"]
speed_list1 = ["enable","configure","interface ethernet 1-40,50/1-53/1","speed forced 10gfull"]
speed_list2 =  ["enable","configure","interface ethernet 1-40,50/1-53/1","speed forced 25gfull"]
speed_list3 =  ["enable","configure","interface ethernet 50/1,51/1,52/1,53/1","speed forced 100gfull"]
shut_list2 = ["enable","configure","interface ethernet 1-46,50/1-53/1","shutdown"]
noshut_list2 = ["enable","configure","interface ethernet 1-46,50/1-53/1","no shutdown"]
shut_list3 = ["enable","configure","interface ethernet 8/2/1-8/35/1","speed forced 40gfull"]
noshut_list3 = ["enable","configure","interface ethernet 8/2/1-8/35/1","speed forced 100gfull"]
shut_list4 = ["enable","configure","interface port-channel 13","shutdown"]
noshut_list4 = ["enable","configure","interface port-channel 13","no shutdown"]
shut_list5 = ["enable","configure","interface vlan 453","shutdown"]
noshut_list5 = ["enable","configure","interface vlan 453","no shutdown"]
terminate_list1 = ["enable","configure","agent SandL3Unicast terminate"]
terminate_list2 = ["enable","configure","agent SandFap-Linecard4 terminate"]
terminate_list3 = ["enable","configure","agent SandAcl terminate"]
terminate_list4 = ["enable","configure","agent SandTcam terminate"]
shut_list6 = ["enable","configure","interface vxlan 1","shutdown"]
noshut_list6 = ["enable","configure","interface vxlan 1","no shutdown"]
for i in range (0,no_of_flaps):
   print 'iteration' + str(i)
   capiCmd(switch,shut_list6)
   time.sleep(t)
   capiCmd(switch,noshut_list6)
   time.sleep(t)
   '''capiCmd(switch,speed_list1)
   time.sleep(t)
   capiCmd(switch,speed_list2)
   time.sleep(t)
   capiCmd(switch,speed_list3)
   time.sleep(t)'''
   '''capiCmd(switch,shut_list5)
   capiCmd(switch,shut_list6)'''
   '''time.sleep(t)
   capiCmd(switch,shut_list3)
   time.sleep(t)
   capiCmd(switch,noshut_list3)
   time.sleep(t)'''
   '''capiCmd(switch,noshut_list3)
   capiCmd(switch,noshut_list4)
   capiCmd(switch,noshut_list5)
   capiCmd(switch,noshut_list6)
   time.sleep(t)'''
   '''capiCmd(switch,terminate_list3)
   time.sleep(t)
   capiCmd(switch,terminate_list4)
   time.sleep(t)'''
   #capiCmd(switch,terminate_list1)
   #capiCmd(switch,shut_list2)
