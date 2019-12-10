# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
flaps = int(sys.argv[2])
t = int(sys.argv[3])
interface_list1 = ['enable','configure','interface ethernet 3/11/1','speed forced 10gfull']
interface_list2 = ['enable','configure','interface ethernet 3/11/1','speed forced 40gfull']
interface_list3 = ['enable','configure','interface ethernet 3/11/1','speed auto 40gfull']
interface_list4 = ['enable','configure','interface ethernet 3/11/1','speed auto 100gfull']
interface_list5 = ['enable','configure','interface ethernet 3/11/1,3/25/1,3/26/1','no error-correction encoding']
interface_list6 = ['enable','configure','interface ethernet 3/11/1,3/25/1,3/26/1','error-correction encoding reed-solomon']
interface_list7 = ['enable','configure','interface ethernet 3/11/1','speed forced 100gfull']
for i in range(0,flaps):
   capiCmd(switch,interface_list1)
   time.sleep(t)
   capiCmd(switch,interface_list2)
   time.sleep(t)
   capiCmd(switch,interface_list3)
   time.sleep(t)
   capiCmd(switch,interface_list4)
   time.sleep(t)
   capiCmd(switch,interface_list7)
   time.sleep(t)
