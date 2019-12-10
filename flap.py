# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from arstCliLib import capiCmd
switch = sys.argv[1]
no_of_flaps = int(sys.argv[2])
t = int(sys.argv[3])
speed_list1 = ["enable","configure","interface ethernet 1-40,50/1-53/1","speed forced 10gfull"]
speed_list2 =  ["enable","configure","interface ethernet 1-40,50/1-53/1","speed forced 25gfull"]
speed_list3 =  ["enable","configure","interface ethernet 50/1,51/1,52/1,53/1","speed forced 100gfull"]
shut_list2 = ["enable","configure","interface ethernet 1-46,50/1-53/1","shutdown"]
noshut_list2 = ["enable","configure","interface ethernet 1-46,50/1-53/1","no shutdown"]
shut_list3 = ["enable","configure","interface ethernet 8/2/1-8/35/1","speed forced 40gfull"]
noshut_list3 = ["enable","configure","interface ethernet 8/2/1-8/35/1","speed forced 100gfull"]
shut_list4 = ["enable","configure","no monitor session default encapsulation gre timestamp"]
noshut_list4 = ["enable","configure","monitor session default encapsulation gre timestamp"]
shut_list5 = ["enable","configure","interface ethernet 3/11/1-4,3/12/1-4,3/21/1,4/11/1-4,4/13/1-4,4/21/1,5/3/1,5/29/1","shutdown"]
noshut_list5 = ["enable","configure","interface ethernet 3/11/1-4,3/12/1-4,3/21/1,4/11/1-4,4/13/1-4,4/21/1,5/3/1,5/29/1","no shutdown"]
terminate_list1 = ["enable","configure","agent SandL3Unicast terminate"]
terminate_list2 = ["enable","configure","agent SandFap-Linecard4 terminate"]
terminate_list3 = ["enable","configure","agent SandAcl terminate"]
terminate_list4 = ["enable","configure","agent SandTcam terminate"]
for i in range (0,no_of_flaps):
   print 'iteration' + str(i)
   capiCmd(switch,shut_list4)
   time.sleep(t)
   capiCmd(switch,noshut_list4)
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
