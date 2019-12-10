# Copyright (c) 2016 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd

switch = sys.argv[1]
flaps = int(sys.argv[2])
t = int(sys.argv[3])
start = ['enable','configure']
interface = "interface ethernet"
x = 2
y = 36
for i in range (x,y):
   if i == y-1:
      interface += " 5/" + str(i) + "/1"
   else:
      interface += " 5/" + str(i) + "/1" + ","
start.append(interface)
speed_1 = ['enable','configure']
speed_2 = ['enable','configure']
speed_3 = ['enable','configure']
speed_4 = ['enable','configure']
speed_1.append(interface)
speed_1.append('speed forced 10gfull')
speed_2.append(interface)
speed_2.append('speed forced 100gfull')
speed_3.append(interface)
speed_3.append('speed forced 40gfull')
speed_4.append(interface)
speed_4.append('speed forced 100gfull')
for n in range(0,flaps):
   capiCmd(switch,speed_1)
   time.sleep(t)
   capiCmd(switch,speed_2)
   time.sleep(t)
   capiCmd(switch,speed_3)
   time.sleep(t)
   capiCmd(switch,speed_4)
   time.sleep(t)
