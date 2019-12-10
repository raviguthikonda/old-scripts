#!/usr/bin/env python

# Copyright (c) 2014 Arista Networks, Inc.  All rights reserved.
# Arista Networks, Inc. Confidential and Proprietary.

############################################################
# Import Modules and initialize ixiangpf
# Defaul Header
############################################################

from pprint import pprint
import os, sys
import time

import json
import stDutConnectUtils
import stConfigCommands
from jsonrpclib import Server
from pprint import pprint

from ixiatcl import IxiaTcl
from ixiahlt import IxiaHlt
from ixiangpf import IxiaNgpf
from ixiaerror import IxiaError

ixiatcl = IxiaTcl()
ixiahlt = IxiaHlt( ixiatcl )
ixiangpf = IxiaNgpf( ixiahlt )
try:
   ErrorHandler('', {})
except (NameError,):
   def ErrorHandler(cmd, retval):
      global ixiatcl
      err = ixiatcl.tcl_error_info()
      log = retval['log']
      additional_info = '> command: %s\n> tcl errorInfo: %s\n> log: %s' % (cmd, err, log)
      raise IxiaError(IxiaError.COMMAND_FAIL, additional_info)

############################################################
# IXIA connection details
############################################################

chassis_ip = "r160-rack74-ixia1" ## IXIA chassis IP address
tcl_server = "r160-rack74-ixia1" ## IXIA chassis tcl server IP address
ixnetwork_tcl_server = 'ixs149'  ## IXIA VM running IxNetwork IP address
port_list = ['1/11', '1/12']   ## IXIA port list on Ixia chassis
cfgErrors = 0

print "\nPrinting connection variables ... "
print 'chassis_ip =  %s' % chassis_ip
print "tcl_server = %s " % tcl_server
print "ixnetwork_tcl_server = %s" % ixnetwork_tcl_server
print "port_list = %s " % port_list

############################################################
# DUT Configuration
############################################################

if len(sys.argv) == 2:
   switchName = sys.argv.pop()
else:
   print "Error"
   sys.exit(0)
print "Connecting to %s..." % (switchName)
switch = Server ("http://admin:@%s/command-api" % (switchName)) #print switch
print "Checking for base config file and loading it..."
try:
   switch.runCmds (1, ["enable","dir flash:class_baseline.config"],"json")
   switch.runCmds (1, ["enable","configure replace flash:class_baseline.config force"],"json")
except:
   switch.runCmds(1,["enable", "copy running-config class_baseline.config"], "json")

print "Changing the routed port to switchport..."

switch.runCmds (1,["enable","configure terminal", "interface ethernet 16/1","no ip address","switchport","switchport mode trunk","switchport trunk allowed vlan 101-105"], "json")
v = 5
start = 101

print "Configuring the vlans"
def createVlan(iv):
      switch.runCmds(1,["enable","configure terminal","vlan "+ str(iv),"interface vlan "+ str(iv),"ip address 200.1."+ str(iv)+".100/24"],"json")

for i in xrange(1,v+1):
   createVlan(start)
   start  = start+1
   


############################################################
# 1. Connect to Ixia and print connection result
############################################################

connect_result = ixiangpf.connect(
      ixnetwork_tcl_server      = ixnetwork_tcl_server,
      tcl_server                = tcl_server,
      device                    = chassis_ip,
      port_list                 = port_list,
      break_locks               = 1,
      reset                     = 1,
   )
if connect_result['status'] != '1':
   ErrorHandler( 'connect', connect_result )

print " Printing connection result ..."
pprint( connect_result )

ports = connect_result['vport_list'].split()

print "\nIxia Ports:", ports


############################################################
# 2. Create topologies on the assigned ports
# 3. Create device groups in the topologies
# 4. Add protocol stacks under each device group
############################################################

## Topology_1

topology_1 = ixiangpf.topology_config(
      topology_name             = "{Topology 1}",
      port_handle               = ports[0],
   )
if topology_1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'topology_config', topology_1 )

topology_1_handle = topology_1['topology_handle']


deviceGroup_1 = ixiangpf.topology_config(
      topology_handle           = topology_1_handle,
      device_group_name         = "{Device Group 1}",
      device_group_multiplier   = "10",
      device_group_enabled      = "1",
   )
if deviceGroup_1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'topology_config', deviceGroup_1 )

deviceGroup_1_handle = deviceGroup_1['device_group_handle']

mv1 = ixiangpf.multivalue_config(
      pattern                   = "counter",
      counter_start             = "00.00.01.00.11.01",
      counter_step              = "00.00.00.00.00.01",
      counter_direction         = "increment",
      nest_step                 = "00.00.00.00.00.01",
      nest_owner                = "topology_1_handle",
      nest_enabled              = "0",
   )
if mv1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', mv1 )

multivalue_1_handle = mv1['multivalue_handle']

interface_1 = ixiangpf.interface_config(
      protocol_name             = "{Ethernet 1}",
      protocol_handle           = deviceGroup_1_handle,
      mtu                       = "1500",
      src_mac_addr              = multivalue_1_handle,
      vlan                      = "0",
      vlan_id                   = "1",
      vlan_id_step              = "0",
      vlan_id_count             = "1",
      vlan_tpid                 = "0x8100",
      vlan_user_priority        = "0",
      vlan_user_priority_step   = "0",
      use_vpn_parameters        = "0",
      site_id                   = "0",
   )
if interface_1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'interface_config', interface_1 )

ethernet_1_handle = interface_1['ethernet_handle']


ipv4_1 = ixiangpf.interface_config(
      protocol_name                     = "{IPv4 1}",
      protocol_handle                   = ethernet_1_handle,
      ipv4_resolve_gateway              = "1",
      ipv4_manual_gateway_mac           = "00.00.00.00.00.01",
      ipv4_manual_gateway_mac_step      = "00.00.00.00.00.00",
      gateway                           = "100.1.1.100",
      intf_ip_addr                      = "100.1.1.1",
      intf_ip_addr_step                 = "0.0.0.1",
      netmask                           = "255.255.255.0",
   )
if ipv4_1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'interface_config', ipv4_1 )

ipv4_1_handle = ipv4_1['ipv4_handle']


############################################################

## Topology_2

topology_2 = ixiangpf.topology_config(
      topology_name             = "{Topology 2}",
      port_handle               = ports[1],
   )
if topology_2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'topology_config', topology_2 )

topology_2_handle = topology_2['topology_handle']


deviceGroup_2 = ixiangpf.topology_config(
      topology_handle           = topology_2_handle,
      device_group_name         = "{Device Group 2}",
      device_group_multiplier   = "10",
      device_group_enabled      = "1",
   )
if deviceGroup_2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'topology_config', deviceGroup_2 )

deviceGroup_2_handle = deviceGroup_2['device_group_handle']

mv2 = ixiangpf.multivalue_config(
      pattern                   = "counter",
      counter_start             = "00.00.01.00.22.01",
      counter_step              = "00.00.00.00.00.01",
      counter_direction         = "increment",
      nest_step                 = "00.00.00.00.00.01",
      nest_owner                = "topology_2_handle",
      nest_enabled              = "0",
   )
if mv2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', mv2 )

multivalue_2_handle = mv2['multivalue_handle']

mv3 = ixiangpf.multivalue_config(
      pattern           = "custom",
      nest_step         = "1",
      nest_owner        = topology_2_handle,
      nest_enabled      = "0",
   )

if mv3['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', mv3 )

multivalue_3_handle = mv3['multivalue_handle']

custom1 = ixiangpf.multivalue_config(
      multivalue_handle      = multivalue_3_handle,
      custom_start           = "101",
      custom_step            = "1",
   )

if custom1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', custom1 )

custom_1_handle = custom1['custom_handle']

increment1 = ixiangpf.multivalue_config(
      custom_handle               = custom_1_handle,
      custom_increment_value      = "0",
      custom_increment_count      = "2",
   )

if increment1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', increment1 )

increment_1_handle = increment1['increment_handle']

interface_2 = ixiangpf.interface_config(
      protocol_name             = "{Ethernet 2}",
      protocol_handle           = deviceGroup_2_handle,
      mtu                       = "1500",
      src_mac_addr              = multivalue_2_handle,
      vlan                      = "1",
      vlan_id                   = multivalue_3_handle,
      vlan_tpid                 = "0x8100",
      vlan_user_priority        = "0",
      vlan_user_priority_step   = "0",
      use_vpn_parameters        = "0",
      site_id                   = "0",
   )
if interface_2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'interface_config', interface_2 )

ethernet_2_handle = interface_2['ethernet_handle']

mv4 = ixiangpf.multivalue_config(
      pattern           = "custom",
      nest_step         = "1",
      nest_owner        = topology_2_handle,
      nest_enabled      = "0",
   )

if mv4['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', mv4 )

multivalue_4_handle = mv4['multivalue_handle']

custom2 = ixiangpf.multivalue_config(
      multivalue_handle      = multivalue_4_handle,
      custom_start           = "200.1.101.100",
      custom_step            = "0.0.1.0",
   )

if custom2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', custom2 )

custom_2_handle = custom2['custom_handle']

increment2 = ixiangpf.multivalue_config(
      custom_handle               = custom_2_handle,
      custom_increment_value      = "0.0.0.0",
      custom_increment_count      = "2",
   )

if increment2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', increment2 )

increment_2_handle = increment2['increment_handle']

mv5 = ixiangpf.multivalue_config(
      pattern           = "custom",
      nest_step         = "1",
      nest_owner        = topology_2_handle,
      nest_enabled      = "0",
   )

if mv5['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', mv5 )

multivalue_5_handle = mv5['multivalue_handle']

custom3 = ixiangpf.multivalue_config(
      multivalue_handle      = multivalue_5_handle,
      custom_start           = "200.1.101.1",
      custom_step            = "0.0.1.0",
   )

if custom3['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', custom3 )

custom_3_handle = custom3['custom_handle']

increment3 = ixiangpf.multivalue_config(
      custom_handle               = custom_3_handle,
      custom_increment_value      = "0.0.0.1",
      custom_increment_count      = "2",
   )

if increment3['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'multivalue_config', increment3 )

increment_3_handle = increment3['increment_handle']

ipv4_2 = ixiangpf.interface_config(
      protocol_name                     = "{IPv4 2}",
      protocol_handle                   = ethernet_2_handle,
      ipv4_resolve_gateway              = "1",
      ipv4_manual_gateway_mac           = "00.00.00.00.00.01",
      ipv4_manual_gateway_mac_step      = "00.00.00.00.00.00",
      gateway                           = multivalue_4_handle,
      intf_ip_addr                      = multivalue_5_handle,
      netmask                           = "255.255.255.0",
   )
if ipv4_2['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'interface_config', ipv4_2 )

ipv4_2_handle = ipv4_2['ipv4_handle']


############################################################
# 6. Start all protocols
############################################################

print "\nStarting all protocols ..."
protocols_start = ixiangpf.test_control(
      action                            = "start_all_protocols"
   )
if protocols_start['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'test_control', protocols_start )

print "\nSleep for 10 seconds ..."
time.sleep( 10 )


print ""


############################################################
# 5. Create traffic items using the NGPF endpoints
############################################################

traffic_item_1 = ixiangpf.traffic_config(
      name                      = "bidir",
      mode                      = "create",
      endpointset_count         = "1",
      emulation_src_handle      = topology_1_handle,
      emulation_dst_handle      = topology_2_handle,
      src_dest_mesh             = "one_to_one",
      route_mesh                = "one_to_one",
      bidirectional             = "1",
      circuit_endpoint_type     = "ipv4",
      track_by                  = "endpoint_pair",
      frame_size                = "1000",
      length_mode               = "fixed",  
   )

if traffic_item_1['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'traffic_config', traffic_item_1)

traffic_item_name = traffic_item_1['stream_id']
print "\nCreated traffic item", traffic_item_name



############################################################
# 8. Start traffic items
############################################################

print "\nClearing the counters..."
switch.runCmds(1,["enable", "clear counters"], "json")

print "\nStarting traffic ..."

traffic_items_start = ixiangpf.traffic_control(
      action                    = "run",
   )
if traffic_items_start['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'traffic_start', traffic_items_start )

print "Sleep for 30 seconds ..."
time.sleep( 30 )

print "\nCollecting initial traffic stats to find out diff due to initial loss ..."

#traffic_items_stop = ixiangpf.traffic_control(
#      action                    = "stop",
#   )
#if traffic_items_stop['status'] != IxiaHlt.SUCCESS:
#   ErrorHandler( 'traffic_stop', traffic_items_stop )
#
#time.sleep( 10 )


############################################################
# 10. Collect traffic statistics
############################################################

traffic_items_stats = ixiangpf.traffic_stats(
      mode                      = "traffic_item",
   )

traffic_items = traffic_items_stats['traffic_item']
#pprint(traffic_items_stats)
print "\nTraffic Item Statistics:"
#pprint( traffic_items )
TrafficItem1LostPkts = traffic_items['TI0-bidir']['rx']['loss_pkts']
#print "before stopping tx: ",traffic_items['TI0-bidir']['tx']['total_pkts']
#print "\n\n"

print "Traffic Item 1 loss packets: ", TrafficItem1LostPkts
time.sleep(30)
print "\nLetting traffic run for 30 seconds..."

print "\nStopping Traffic....."
traffic_items_stop = ixiangpf.traffic_control(
      action                    = "stop",
   )
if traffic_items_stop['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'traffic_stop', traffic_items_stop )
print "Sleeping for 20 seconds......"
time.sleep( 20 )

traffic_items_stats = ixiangpf.traffic_stats(
      mode                      = "traffic_item",
   )
print "Collecting traffic stats after traffic stopped"

traffic_items = traffic_items_stats['traffic_item']
TrafficItem1TxTotalPkts = traffic_items['TI0-bidir']['tx']['total_pkts']
TrafficItem1RxTotalPkts = traffic_items['TI0-bidir']['rx']['total_pkts']
print "--------------------------Test 1---------------------------"
print "Traffic Item 1 Tx total packets:", TrafficItem1TxTotalPkts
print "Traffic Item 1 Rx total packets:", TrafficItem1RxTotalPkts

#TrafficItem1LostPkts = traffic_items['TI0-bidir']['rx']['loss_pkts']


if (int(TrafficItem1TxTotalPkts) == (int(TrafficItem1RxTotalPkts) + int(TrafficItem1LostPkts))):
   print "Test 1 - Pass: Traffic Item 1: Transmitted and Recevied packets matched"
else:
   print "Delta between Tx and Rx Packets:", (int(TrafficItem1TxTotalPkts) - int(TrafficItem1RxTotalPkts))

print "\nCollecting traffic counter bins from DUT..... "
rxCount = switch.runCmds(1,["enable", "show interfaces counters bins"], "json")
print "--------------------------Test 2-----------------------------"
#pprint(rxCount)
print "Dut Rx: ", (int(rxCount[1]['interfaces']['Ethernet16/1']['outBinsCounters']['frames512To1023Octet']))
print "Ixia Tx: ", (int(traffic_items['TI0-bidir']['tx']['total_pkts']))
if ((int(rxCount[1]['interfaces']['Ethernet16/1']['outBinsCounters']['frames512To1023Octet'])*2)+int(TrafficItem1LostPkts)) == int(traffic_items['TI0-bidir']['tx']['total_pkts']):
   print "Test 2 - Pass: Ixia Tx matches DUT Rx as Ixia Tx is exactly double of DUT Rx"
else:
   print "Fail: Ixia Tx and DUT Rx don't match"

############################################################
# 11. Cleanup and release
############################################################

print "\nStopping all protocols ..."
protocols_stop = ixiangpf.test_control(
      action                            = "stop_all_protocols"
   )
if protocols_stop['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'test_control', protocols_stop )

print "\nSleep for 10 seconds ..."
time.sleep( 10 )

print "\n\nScript executed successfully."

############################################################


