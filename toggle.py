# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
n = int(sys.argv[2])
t = int(sys.argv[3])
shut_list1 = ["enable","configure","interface vlan 2","no ip access-group acl-3k in"]
noshut_list1 = ["enable","configure","interface vlan 2","ip access-group acl-3k in"]
shut_list2 = ["enable","configure","interface Ethernet 3/7/1.1,4/7/1.1,5/7/1.1,6/7/1.1,7/7/1.1,8/7/1.1,9/7/1.1","no ip access-group acl-3k in"]
noshut_list2 = ["enable","configure","interface Ethernet 3/7/1.1,4/7/1.1,5/7/1.1,6/7/1.1,7/7/1.1,8/7/1.1,9/7/1.1","ip access-group acl-3k in"]
shut_list3 = ["enable","configure","interface Ethernet 3/13/1,4/13/1,5/13/1,6/13/1,7/9/1,8/13/1,9/13/1","no ip access-group acl-3k in"]
noshut_list3 = ["enable","configure","interface Ethernet 3/13/1,4/13/1,5/13/1,6/13/1,7/9/1,8/13/1,9/13/1","ip access-group acl-3k in"]
shut_list4 = ["enable","configure","interface port-channel 2","no ip access-group acl-3k in"]
noshut_list4 = ["enable","configure","interface port-channel 2","ip access-group acl-3k in"]
shut_list5 = ["enable","configure","interface port-channel 3.1","no ip access-group acl-3k in"]
noshut_list5 = ["enable","configure","interface port-channel 3.1","ip access-group acl-3k in"]
shut_list6 = ["enable","configure","interface ethernet 6/1/1,7/1/1","no switchport mode trunk"]
noshut_list6 = ["enable","configure","interface ethernet 6/1/1,7/1/1","switchport mode trunk"]
shut_list7 = ["enable","configure","interface ethernet 3/1/1,4/1/1,5/1/1,8/1/1,9/1/1","no switchport mode trunk"]
noshut_list7 = ["enable","configure","interface ethernet 3/1/1,4/1/1,5/1/1,8/1/1,9/1/1","switchport mode trunk"]



for i in range (n):
   '''capiCmd(switch,shut_list1)
   capiCmd(switch,shut_list2)
   capiCmd(switch,shut_list3)
   capiCmd(switch,shut_list4)
   capiCmd(switch,shut_list5)
   time.sleep(3)'''
   capiCmd(switch,shut_list6)
   time.sleep(t)
   capiCmd(switch,noshut_list6)
   '''capiCmd(switch,noshut_list1)
   capiCmd(switch,noshut_list2)
   capiCmd(switch,noshut_list3)
   capiCmd(switch,noshut_list4)
   capiCmd(switch,noshut_list5)'''
   capiCmd(switch,shut_list7)
   time.sleep(t)
   capiCmd(switch,noshut_list7)
