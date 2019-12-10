# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

ip_address = raw_input('enter an ip address')
ip_address = ip_address.split('.')[0:3]
ip_address.append('0')
print ip_address
network_number  = '.'.join(ip_address)

print '%30s %30s %30s' % ('Network Number','First_Octet_Binary', 'First_Octet_Hex')
print '%30s %30s %30s' % (ip_address,bin(int(ip_address[0])),hex(int(ip_address[0])))
