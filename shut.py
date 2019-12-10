# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from arstCliLib import capiCmd
switch = sys.argv[1]
no_of_flaps = int(sys.argv[2])
t = int(sys.argv[3])
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
shut_list4 = ["enable","configure","interface tunnel 1-6","shutdown"]
noshut_list4 = ["enable","configure","interface tunnel 1-6","no shutdown"]
shut_list5 = ["enable","configure","interface ethernet 3/11/1-4,3/12/1-4,3/21/1,4/11/1-4,4/13/1-4,4/21/1,5/3/1,5/29/1","shutdown"]
noshut_list5 = ["enable","configure","interface ethernet 3/11/1-4,3/12/1-4,3/21/1,4/11/1-4,4/13/1-4,4/21/1,5/3/1,5/29/1","no shutdown"]
terminate_list1 = ["enable","configure","agent SandL3Unicast terminate"]
terminate_list2 = ["enable","configure","agent SandFap-Linecard4 terminate"]
terminate_list3 = ["enable","configure","agent SandAcl terminate"]
terminate_list4 = ["enable","configure","agent SandTcam terminate"]
shut_list6 = ["enable","configure","interface ethernet 3/2/1-3/36/1,5/1/1-5/36/1,6/2/1-6/36/1,7/2/1-7/36/1,8/2/1-8/36/1,9/2/1-9/36/1,10/2/1-10/36/1,11/2/1-11/36/1,12/2/1-12/36/1,13/2/1-13/36/1,14/2/1-14/36/1,15/2/1-15/36/1,16/2/1-16/36/1,17/1/1-18/36/1","shutdown"]
noshut_list6 = ["enable","configure","interface ethernet 3/2/1-3/36/1,5/1/1-5/36/1,6/2/1-6/36/1,7/2/1-7/36/1,8/2/1-8/36/1,9/2/1-9/36/1,10/2/1-10/36/1,11/2/1-11/36/1,12/2/1-12/36/1,13/2/1-13/36/1,14/2/1-14/36/1,15/2/1-15/36/1,16/2/1-16/36/1,17/1/1-18/36/1","no shutdown"]
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
