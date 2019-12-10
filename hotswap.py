# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
import time
from cliLib import capiCmd
switch = sys.argv[1]
no_of_swaps = int(sys.argv[2])
t = int(sys.argv[3])
swap_list3 = ["enable","configure","platform module Fabric5 remove"]
noswap_list3 = ["enable","configure","platform module Fabric5 insert"]
swap_list4 = ["enable","configure","platform module Linecard4 remove"]
noswap_list4 = ["enable","configure","platform module Linecard4 insert"]
swap_list5 = ["enable","configure","platform module Linecard5 remove"]
noswap_list5 = ["enable","configure","platform module Linecard5 insert"]
swap_list6 = ["enable","configure","platform module Linecard6 remove"]
noswap_list6 = ["enable","configure","platform module Linecard6 insert"]
swap_list7 = ["enable","configure","platform module Linecard7 remove"]
noswap_list7 = ["enable","configure","platform module Linecard7 insert"]
swap_list8 = ["enable","configure","platform module Linecard8 remove"]
noswap_list8 = ["enable","configure","platform module Linecard8 insert"]
swap_list9 = ["enable","configure","platform module Linecard9 remove"]
noswap_list9 = ["enable","configure","platform module Linecard9 insert"]
swap_list10 = ["enable","configure","platform module Linecard10 remove"]
noswap_list10 = ["enable","configure","platform module Linecard10 insert"]
for i in range (0,no_of_swaps):
   capiCmd(switch,swap_list6)
   capiCmd(switch,swap_list7)
   time.sleep(t)
   capiCmd(switch,noswap_list6)
   capiCmd(switch,noswap_list7)
   time.sleep(t)
