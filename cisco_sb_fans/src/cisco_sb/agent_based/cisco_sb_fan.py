#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# (c) Robert Oschwald 2019             
# 2024 refactored to use .agent_based_api.v2 by Daniel Paul

# Check for Cisco Small Business Switch FANs.
#
# We probe:
# 1. sysDescr.0 (default, probably already cached) for "switch" (case insensitive)
# 2. existance of CISCOSB-Physicaldescription-MIB::rlPhdUnitGenParamManufacturer.1 (SNMPv2-SMI::enterprises.9.6.1.101.53.14.1.10.1),
#    as this MIB is available on SB Switches (like SG300 Series) only
# 3. SNMPv2-SMI::enterprises.9.6.1.101.53.14.1.10.1 for "cisco" as well (case insensitive)
#
# The fans itself are on the following OIDs:
# rlEnvMonFanStatusDescr.67109249  : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.2.67109249 = STRING: fan1_unit1
# rlEnvMonFanStatusDescr.67109250  : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.2.67109250 = STRING: fan2_unit1
# rlEnvMonFanStatusDescr.67109251  : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.2.67109251 = STRING: fan3_unit1
# rlEnvMonFanStatusDescr.67109252  : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.2.67109252 = STRING: fan4_unit1
# rlEnvMonFanState.67109249        : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.3.67109249 = INTEGER: normal(1)
# rlEnvMonFanState.67109250        : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.3.67109250 = INTEGER: notFunctioning(6)
# rlEnvMonFanState.67109251        : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.3.67109251 = INTEGER: normal(1)
# rlEnvMonFanState.67109252        : .1.3.6.1.4.1.9.6.1.101.83.1.1.1.3.67109252 = INTEGER: notPresent(5)
#
# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  This file is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file LICENSE.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

from cmk.agent_based.v2 import Result, Service, matches, all_of, exists, SNMPTree, State
from cmk.agent_based.v2 import SNMPSection, SimpleSNMPSection, CheckPlugin

def parse_cisco_sb_fans(string_table):
    return string_table

def discover_cisco_sb_fans(section):
    # Sample Data section:
    # ['fan1_unit1', '1'] <-- OK
    # ['fan2_unit1', '1'] <-- OK
    # ['fan3_unit1', '5'] <-- notPresent
    # ['fan4_unit1', '5'] <-- notPresent

    for line in section:
        if line[1] != '5': # ignore Fans with state notPresent
            yield Service(item=line[0])

def check_cisco_sb_fans(item, section):
    cisco_fan_state_mapping = {
        "1": (State.OK, "normal"),
        "2": (State.WARN, "warning"),
        "3": (State.CRIT, "critical"),
        "4": (State.CRIT, "shutdown"),
        "5": (State.UNKNOWN, "notPresent"),
        "6": (State.CRIT, "notFunctioning"),
    }

    for line in section:
        if line[0] == item:
            fan_state, fan_state_readable = cisco_fan_state_mapping.get(
                line[1], (State.UNKNOWN, "unknown state [%s]" % line[1])
            )
            yield Result(state=fan_state, summary=f"Status: {fan_state_readable}")

snmp_section_cisco_sb_fan = SimpleSNMPSection(
    name = "cisco_sb_fans",
    parse_function = parse_cisco_sb_fans,
    detect = all_of(
        matches(".1.3.6.1.2.1.1.1.0", "(?i).*switch"),
        exists(".1.3.6.1.4.1.9.6.1.101.53.14.1.10.1"),
        matches(".1.3.6.1.4.1.9.6.1.101.53.14.1.10.1", "(?i).*cisco")
    ),
    fetch = SNMPTree(
        base='.1.3.6.1.4.1.9.6.1.101.83.1.1.1', 
        oids=[
            '2', 
            '3'
        ]
    ),
)

check_plugin_cisco_sb_fan = CheckPlugin(
    name = "cisco_sb_fan",
    sections = ["cisco_sb_fans"],
    service_name = "Fan %s",
    discovery_function = discover_cisco_sb_fans,
    check_function = check_cisco_sb_fans,
)
