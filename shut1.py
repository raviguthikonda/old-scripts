# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
flaps = int(sys.argv[2])
t = int(sys.argv[3])
err_disable = ['enable','configure','errdisable test interface port-channel1']
shut_list1 = ['enable','configure','interface port-channel1']
shut_list1.append('shutdown')
shut_list1.append('no shutdown')
for i in range(0,flaps):
   #shut_list1.append('shutdown')
   #shut_list1.append('no shutdown')
#print shut_list1
   time.sleep(t)
   capiCmd(switch,err_disable)
   capiCmd(switch,shut_list1)
   time.sleep(t)
