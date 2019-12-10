#!/usr/bin/env python
# Copyright (c) 2015 Arista Networks, Inc.  All rights reserved.
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


from ixiatcl import IxiaTcl
from ixiahlt import IxiaHlt
from ixiangpf import IxiaNgpf
from ixiaerror import IxiaError


ixiatcl = IxiaTcl()
ixiahlt = IxiaHlt( ixiatcl )
ixiangpf = IxiaNgpf( ixiahlt )


############################################################
# IXIA connection details
############################################################

chassis_ip = "r160-rack74-ixia15" ## IXIA chassis IP address
tcl_server = "r160-rack74-ixia15" ## IXIA chassis tcl server IP address
ixnetwork_tcl_server = 'ixs151'  ## IXIA VM running IxNetwork IP address
port_list = ['8/15', '8/16']   ## IXIA port list on Ixia chassis
cfgErrors = 0


print "\nPrinting connection variables ... "
print 'chassis_ip =  %s' % chassis_ip
print "tcl_server = %s " % tcl_server
print "ixnetwork_tcl_server = %s" % ixnetwork_tcl_server
print "port_list = %s " % port_list


############################################################
# 1. Connect to Ixia and print connection result
############################################################

connect_result = ixiangpf.connect(
            ixnetwork_tcl_server      =  ixnetwork_tcl_server,
            tcl_server                =  tcl_server,
            device                    =  chassis_ip,
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
            vlan                      = "1",
            vlan_id                   = "60",
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
       gateway                           = "60.0.0.1",
       gateway_step                      = "0.0.0.0",
       intf_ip_addr                      = "60.0.1.0",
       intf_ip_addr_step                 = "0.0.0.1",
       netmask                           = "255.255.255.255",
                                                                     )
if ipv4_1['status'] != IxiaHlt.SUCCESS:
            ErrorHandler( 'interface_config', ipv4_1 )

ipv4_1_handle = ipv4_1['ipv4_handle']



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
            counter_start             = "00.00.02.00.11.01",
            counter_step              = "00.00.00.00.00.01",
            counter_direction         = "increment",
            nest_step                 = "00.00.00.00.00.01",
            nest_owner                = "topology_2_handle",
            nest_enabled              = "0",
            )
if mv2['status'] != IxiaHlt.SUCCESS:
      ErrorHandler( 'multivalue_config', mv2)

multivalue_2_handle = mv2['multivalue_handle']
interface_2 = ixiangpf.interface_config(
            protocol_name             = "{Ethernet 1}",
            protocol_handle           = deviceGroup_2_handle,
            mtu                       = "1500",
            src_mac_addr              = multivalue_2_handle,
            vlan                      = "1",
            vlan_id                   = "60",
            vlan_id_step              = "0",
            vlan_id_count             = "1",
            vlan_tpid                 = "0x8100",
            vlan_user_priority        = "0",
            vlan_user_priority_step   = "0",
            use_vpn_parameters        = "0",
            site_id                   = "0",
            )
if interface_2['status'] != IxiaHlt.SUCCESS:
            ErrorHandler( 'interface_config', interface_2 )

ethernet_2_handle = interface_2['ethernet_handle']


ipv4_2 = ixiangpf.interface_config(
       protocol_name                     = "{IPv4 2}",
       protocol_handle                   = ethernet_2_handle,
       ipv4_resolve_gateway              = "1",
       ipv4_manual_gateway_mac           = "00.00.00.00.00.01",
       ipv4_manual_gateway_mac_step      = "00.00.00.00.00.00",
       gateway                           = "60.0.0.1",
       gateway_step                      = "0.0.0.0",
       intf_ip_addr                      = "60.1.1.0",
       intf_ip_addr_step                 = "0.0.0.1",
       netmask                           = "255.255.255.255",
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


print "\nStarting traffic ..."

traffic_items_start = ixiangpf.traffic_control(
      action                    = "run",
   )
if traffic_items_start['status'] != IxiaHlt.SUCCESS:
   ErrorHandler( 'traffic_start', traffic_items_start )

print "Sleep for 30 seconds ..."
time.sleep( 30 )

