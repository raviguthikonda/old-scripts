# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.
import sys
result = 'invalid'
while result =='invalid':
   ip = raw_input('enter valid ip address')
   print "input ip is %s" %(ip)
   ip_list = ip.split('.')
   if len(ip_list) == 4:
      if (int(ip_list[0]) >= 1 and int(ip_list[0]) <=223 and int(ip_list[0])!= 127):
         if ( int(ip_list[0]) != 169 and int(ip_list[1]) !=254  and int(ip_list[1]) >=0 and int(ip_list[1]) <=255 ):
            for i in range(2,4):
               if (int(ip_list[i]) >=0 and int(ip_list[i]) <= 255 ) :
                  result = 'valid'
               else:
                  result = 'invalid'
         else:
            result = 'invalid'
      else:
         result = 'invalid'
   else:
      result = 'invalid'
print result
