# Copyright (c) 2017 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

import sys
from arstCliLib import capiCmd
switches = sys.argv[1:]
print len(switches)
clear_counters = ['enable','configure','clear counters','clear platform fap counters','clear hardware counter drop']
for each in switches:
   print each
   capiCmd(each,clear_counters)
