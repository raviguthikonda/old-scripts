# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

## split given ipv6 address into 4 octets##

a = 'FE80:0000:0000:0000:0101:A3EF:EE1E:1719'
b = a.split(':')
print b

##join the split octets

c = ':'.join(b)
print c
