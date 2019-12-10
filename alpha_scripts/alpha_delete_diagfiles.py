# Copyright (c) 2019 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.


import sys
import pexpect
import time
dut_list = []
#prompt = '[>#]$'
scpChild = pexpect.spawn("ssh root@veos1-cva \n", timeout = 30)
time.sleep(10)
"""
retVal = scpChild.expect(['.*(yes/no)','.*>'])
if retVal == 0:
   scpChild.send('yes \n')
elif retVal == 1:
   pass
time.sleep(2)
"""
retVal = scpChild.expect(['.*Password: '])
print retVal
scpChild.send('arastra \n')
time.sleep(2)
scpChild.send("FastCli \n")
time.sleep(2)
scpChild.expect(['.*Password: '])
scpChild.send('arastra \n')
time.sleep(2)

scpChild.expect(['.*>'])
print scpChild.before
print scpChild.after
'''f = open("alpha_duts.txt",'r')
dut_list = f.read().split()
child = pexpect.spawn('ssh root@veos1-cva \n')
#print child
print child
print child.before
print child.after
child.sendline("arastra")
time.sleep(5)
enable = child.sendline("enable")

#print child.before
#print child.after
child.expect('.*')
#print enable
child.sendline("bash sudo rm /mnt/flash/delhi-final")
child.expect('.*')
#print type(version)
#print child.before
#print child.after
#print len(dut_list)
#print(dut_list)'''
