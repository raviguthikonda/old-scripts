#!/usr/bin python
import argparse
import sys
import jsonrpclib
import socket
import time
from pprint import pprint
from jsonrpclib import Server
import json
import base64
import cjson
import time
import urllib2


# Variables

a= 'abc'
b=1
output = ''
#v=101

#dutName = ['bern', 'belfast', 'dublin', 'berlin', 'bonn', 'ankara', 'prague', 'budapest', 'minsk', 'bucharest', 'athens', 'bratislava', 'kiev', 'geneva', 'opportunity', 'cairo', 'doha', 'beagle', 'cali', 'salvador']
#Connecting to the Dut
#codename = {'': '', '7050T-64': 'Trident+', '7260CX3-64': 'Tomahawk2', '7050SX2-128': 'Trident2+', '7280CR-48': 'Jericho ', '7500R2-36CQ-LC': 'Jericho+', '7280CR2-60': 'Jericho+', '7050S-48': 'Trident+', '7304': 'Trident2', '7308': 'Trident2', '7500E-72S-LC': 'Arad', '7050SX-96': 'Trident2', 'DCS-7508-FM': 'M8', '7050T-36 HwRev4': 'Trident+', '7280QR-C36': 'Qumran', 'DCS-7300X-64S-LC': 'Trident2', 'LY6': 'Trident2 56850', 'Product Name': 'Chipset', 'LY8': 'Trident2 56854', '7160-48YC6': 'XP80\n', '7140T-8S': 'Bali', 'DCS-7504-FM': 'M4', '7060CX2-32S': 'Tomahawk+', 'Redstone-XP D2060': 'Trident2 56854', '7160S-32CQ': 'XP80', '7050TX-48': 'Trident2', '7050S-52': 'Trident+', 'DCS-7504R-FM': 'M4', '7050SX2-72Q': 'Trident2+', 'Smallstone D4040': 'Trident2 56850', '7280TR-48C6': 'Qumran', '7316': 'Trident2', '7250QX-64': 'Trident2', '7020TRA-48': 'Qumran-Ax', 'DCS-7500-SUP2': '', '7150S-24': 'Alta', '7504N': 'Arad/Jericho', '7280CRA-48': 'Jericho ', '7050TX-72': 'Trident2', '7050QX-32S': 'Trident2', '7500R-48S2CQ-LC': 'Jericho', '7500R-36Q-LC': 'Jericho', 'None (fan spinner / test card)': 'M4', '7050T-64 HwRev4': 'Trident+', '7050QX2-32S': 'Trident2+', '7260CX-64': 'Tomahawk', '7280QRA-C36': 'Jericho ', '7160-64YC16': 'XP80', '7124SX': 'Bali', '7120T-4S': 'Bali', '7124S': 'Bali', '7500E\xc2\xad-48T-\xc2\xadLC': 'Arad+', '7150S-52': 'Alta', '7050TX-64': 'Trident2', '7500RM-36CQ-LC': 'Jericho', '7280SR-48C6': 'Qumran', '7020TR-48': 'Qumran-Ax', '7548S-LC': 'PetraA', 'DCS-7504E-FM': 'M4', '7148S': 'Bali', '7500RA-36CQ-LC': 'Jericho', 'DCS-7300X-64T-LC': 'Trident2', 'DCS-7300-SUP': '', '7048T-A': 'Petra', '7050QX-32': '', '7280SRA-40CX2': 'Qumran-Mx', '7010-T-DC': 'Helix4', '7050TX-96': 'Trident2', '7048T': 'Petra', '7280TRA-48C6-M': 'Qumran-MX', '7050SX-72Q': 'Trident2', 'DCS-7308X-FM': 'S8', 'Not a FRU': '', 'DCS-7328X-FM-F': '', 'DCS-7508R-FM': 'M8', 'DCS-7510R-FM': 'M12', 'Model Number': 'System', '7060CX-32S': 'Tomahawk', '7050T-36': 'Trident+', 'DCS-7316X-FM': 'S16', '7050T-52': 'Trident+', '7280QR-C72': 'Jericho ', '7050SX-128': 'Trident2', '7280QRA-C72': 'Jericho ', '7280SRA-48C6-M': 'Qumran-MX', '7050SX-64': 'Trident2', '7500E-6CFPX-LC': 'Arad+', 'DCS-7300X-32Q-LC': 'Trident2', '7280SRA-48C6': 'Qumran-MX', '7500R-24CQX-LC': 'Jericho', '7500E-36Q-LC': 'Arad', '7320X-32C-LC': 'Tomahawk', '7500E-6C2-LC': 'Arad', '7150S-64': 'Alta', '7500E-12CM-LC': 'Arad', 'Product cancelled': 'Trident2', '7512N': 'Arad/Jericho', '7280SE-64': 'Arad+', '7050SX-72': 'Trident2', '7280SE-68': 'Arad+', 'DCS-7500-SUP': '', 'AG-8032PL-I1-R': 'Trident2 56854', '7010T': 'Helix4', '7508N': 'Arad/Jericho', 'HP Altoline 5712': 'Trident2 56854', '7050S-64': 'Trident+', '7050Q-16': 'Trident+', 'DCS-7324X-FM': 'S4', 'N/A - SIMULATION': 'Alta', '7500R-8CFPX-LC': 'Jericho', 'DCS-7508E-FM': 'M8', '7148SX': 'Bali', '7280TRA-48C6': 'Qumran-MX', '7124FX': 'Bali', '7050T-52 HwRev4': 'Trident+', 'DCS-7328X-FM': 'S8', '7500RA-48S-LC': 'Jericho', '7500RA-36Q-LC': 'Jericho', '7050TX-128': 'Trident2', '7280SE-72': 'Arad+', '7050TX2-128': 'Trident2+', '7280SR2-48YC6': 'Jericho+', 'DCS-7304X-FM': 'S4', '7280CR2A-60': 'Jericho+', 'DCS-7500E-SUP': '', '7500E-48S-LC': 'Arad', '7260QX-64': 'Tomahawk', '7050TX-72Q': 'Trident2', '7504': 'Petra/Arad/Jericho', '7160-48TC6': 'XP80', '7508': 'Petra/Arad/Jericho', '7500E-12CQ-LC': 'Arad'}

#dutName = ['Helsinki', 'Oslo', 'dublin', 'berlin', 'bonn', 'ankara', 'london', 'prague', 'budapest', 'bucharest', 'athens', 'glasgow', 'bratislava', 'belfast', 'seoul', 'tokyo', 'agra', 'bangkok', 'singapore', 'cali', 'salvador', 'calama','accra', 'astana', 'beagle', 'curiosity', 'opportunity', 'spirit', 'cairo', 'doha','mumbai','luna','mars','mercury','neptune','venus','jupiter','stockholm','gothenburg','belem','mendoza','lunokhod']

dutName = ['Helsinki', 'Oslo', 'dublin', 'berlin', 'bonn', 'ankara', 'london', 'prague', 'budapest', 'bucharest', 'athens', 'glasgow', 'bratislava', 'belfast', 'seoul', 'tokyo', 'agra', 'bangkok', 'singapore', 'salvador','accra', 'astana', 'beagle', 'curiosity', 'opportunity', 'spirit', 'cairo', 'doha','mumbai','luna','mars','mercury','neptune','venus','jupiter','stockholm','gothenburg','lunokhod']

for a in dutName:
   b = b+1
   #print "=====================Connecting to Switch %s===================" %a
   dut = Server( "http://cvpadmin:arista123@%s/command-api" %a )
   #cmd = ["show ip interface brief | grep 'Management0\|Management1' | awk '{print $2}'"]
   #response = dut.runCmds(1,cmd,'text')
   #output =  response[0]['output']
   #print '%s:%s' %(a,output.split('/')[0])
   cmd = ['enable','configure','prompt %H.%D{%H:%M:%S}%P']
   response = dut.runCmds(1,cmd,'text')
   cmd = ['write memory']
   response = dut.runCmds(1,cmd,'text')
   '''
   #print 'Trying to configure bfd on all interface in ospfv3'
   #print 'show version of dut : %s' %a
   cmd = [ 'enable', "show version | grep 'Software image version' |awk {'print $4'}"]
   response = dut.runCmds(1, [ 'enable', "show version | grep 'Software image version' |awk {'print $4'}"], 'text')
   print 'Running image on %s is :                        %s' %(a, response[1]['output'])
   #response = dut.runCmds(1, ['enable','show version detail| grep -i epoch'], 'text')
   #print response[1]['output']
   response = dut.runCmds(1, [ 'enable', 'show boot-config | grep "Software image:"'], 'text')
   print "Boot-config is           :                          %s" %response[1]['output']
   print 'Running cmd: "show system coredump"'
   response = dut.runCmds(1, [ 'enable', 'bash timeout 30 ls -ltr /var/core/' ], 'text')
   print "Core                     :                          %s" %response[1]['output']
   cmd = ['enable','show agent agent logs crash | grep "Unix"']
   try:
    cmd = ['enable','show running-config interfaces vxlan 1']
    response = dut.runCmds(1, cmd ,'text')
    print response[1]['output']
   except Exception as e:
       print a
   #response = dut.runCmds(1, [ "enable","write  memory"], 'text')
   #print response[1]
   #response = dut.runCmds(1, [ "enable", "show mlag detail | grep -m 1 'state' | awk {'print $3'}"], "text")
   #response = dut.runCmds(1, [ "enable", "configure", "queue-monitor length", "queue-monitor streaming", "no shutdown", "exit"], "text")
   #print 'Configured managment api as https'
   #print "Mlag Status             :                          %s" %response[1]['output']
   #response = dut.runCmds(1, [ 'enable', 'show tech-support >> earlville-Jan27' ], 'text')
   #print response[1]
   
   response = dut.runCmds(1, ['enable', 'show inventory'], 'json')
   #output = json.loads(response[1])
   modelNumber = response[1]['systemInformation']['name']
   print 'Model name of the device %s is:               %s' %(a, modelNumber[4:])
   try:
       #
       print 'Platform type of the device %s is :           %s\n' %(a, codename[modelNumber[4:]])
   except:
       print 'Platform type of the device %s is :           N/A\n' %(a)
    '''
