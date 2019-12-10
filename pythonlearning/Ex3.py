# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
import sys

ip_address = sys.argv.pop()
ip_address = ip_address.split('.')[0:3]
ip_address.append('0')
print ip_address
network_number  = '.'.join(ip_address)

print '%30s %30s %30s' % ('Network Number','First_Octet_Binary_Old','First_Octet_Binary_New')
bin_old = bin(int(ip_address[0]))
bin_new = bin_old.replace('0b','')
for i in range(8 - len(bin_new)):
   bin_new = bin_new + '0'
print '%30s %30s %30s' % (ip_address,bin_old, bin_new)
