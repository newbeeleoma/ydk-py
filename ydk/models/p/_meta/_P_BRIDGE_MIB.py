


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EnabledStatus_Enum' : _MetaInfoEnum('EnabledStatus_Enum', 'ydk.models.p.P_BRIDGE_MIB',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'P-BRIDGE-MIB', _yang_ns._namespaces['P-BRIDGE-MIB']),
    'PBRIDGEMIB.Dot1dExtBase' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dExtBase',
            False, 
            [
            _MetaInfoClassMember('dot1dDeviceCapabilities', REFERENCE_BITS, 'Dot1dDeviceCapabilities_Bits' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dExtBase.Dot1dDeviceCapabilities_Bits', 
                [], [], 
                '''                Indicates the optional parts of IEEE 802.1D and 802.1Q
                that are implemented by this device and are manageable
                through this MIB.  Capabilities that are allowed on a
                per-port basis are indicated in dot1dPortCapabilities.
                
                dot1dExtendedFilteringServices(0),
                                      -- can perform filtering of
                                      -- individual multicast addresses
                                      -- controlled by GMRP.
                dot1dTrafficClasses(1),
                                      -- can map user priority to
                                      -- multiple traffic classes.
                dot1qStaticEntryIndividualPort(2),
                                      -- dot1qStaticUnicastReceivePort &
                                      -- dot1qStaticMulticastReceivePort
                                      -- can represent non-zero entries.
                dot1qIVLCapable(3),   -- Independent VLAN Learning (IVL).
                dot1qSVLCapable(4),   -- Shared VLAN Learning (SVL).
                dot1qHybridCapable(5),
                                      -- both IVL & SVL simultaneously.
                dot1qConfigurablePvidTagging(6),
                                      -- whether the implementation
                                      -- supports the ability to
                                      -- override the default PVID
                                      -- setting and its egress status
                                      -- (VLAN-Tagged or Untagged) on
                                      -- each port.
                dot1dLocalVlanCapable(7)
                                      -- can support multiple local
                                      -- bridges, outside of the scope
                                      -- of 802.1Q defined VLANs.
                ''',
                'dot1ddevicecapabilities',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dGmrpStatus', REFERENCE_ENUM_CLASS, 'EnabledStatus_Enum' , 'ydk.models.p.P_BRIDGE_MIB', 'EnabledStatus_Enum', 
                [], [], 
                '''                The administrative status requested by management for
                GMRP.  The value enabled(1) indicates that GMRP should
                be enabled on this device, in all VLANs, on all ports
                for which it has not been specifically disabled.  When
                disabled(2), GMRP is disabled, in all VLANs and on all
                ports, and all GMRP packets will be forwarded
                transparently.  This object affects both Applicant and
                Registrar state machines.  A transition from disabled(2)
                to enabled(1) will cause a reset of all GMRP state
                machines on all ports.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dgmrpstatus',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTrafficClassesEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The value true(1) indicates that Traffic Classes are
                enabled on this bridge.  When false(2), the bridge
                operates with a single priority level for all traffic.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dtrafficclassesenabled',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dExtBase',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable.Dot1dPortOutboundAccessPriorityEntry' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable.Dot1dPortOutboundAccessPriorityEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dRegenUserPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                ''',
                'dot1dregenuserpriority',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dPortOutboundAccessPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Outbound Access Priority the received frame is
                mapped to.
                ''',
                'dot1dportoutboundaccesspriority',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dPortOutboundAccessPriorityEntry',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable',
            False, 
            [
            _MetaInfoClassMember('dot1dPortOutboundAccessPriorityEntry', REFERENCE_LIST, 'Dot1dPortOutboundAccessPriorityEntry' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable.Dot1dPortOutboundAccessPriorityEntry', 
                [], [], 
                '''                Regenerated User Priority to Outbound Access Priority
                mapping.
                ''',
                'dot1dportoutboundaccesspriorityentry',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dPortOutboundAccessPriorityTable',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTpHCPortTable.Dot1dTpHCPortEntry' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTpHCPortTable.Dot1dTpHCPortEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dTpPort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dtpport',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTpHCPortInDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Count of valid frames that have been received by this
                port from its segment that were discarded (i.e.,
                filtered) by the Forwarding Process.
                ''',
                'dot1dtphcportindiscards',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpHCPortInFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of frames that have been received by this
                port from its segment.  Note that a frame received on
                the interface corresponding to this port is only counted
                by this object if and only if it is for a protocol being
                processed by the local bridging function, including
                bridge management frames.
                ''',
                'dot1dtphcportinframes',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpHCPortOutFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of frames that have been transmitted by this
                port to its segment.  Note that a frame transmitted on
                the interface corresponding to this port is only counted
                by this object if and only if it is for a protocol being
                processed by the local bridging function, including
                bridge management frames.
                ''',
                'dot1dtphcportoutframes',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTpHCPortEntry',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTpHCPortTable' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTpHCPortTable',
            False, 
            [
            _MetaInfoClassMember('dot1dTpHCPortEntry', REFERENCE_LIST, 'Dot1dTpHCPortEntry' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTpHCPortTable.Dot1dTpHCPortEntry', 
                [], [], 
                '''                Statistics information for each high-capacity port of a
                transparent bridge.
                ''',
                'dot1dtphcportentry',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTpHCPortTable',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTpPortOverflowTable.Dot1dTpPortOverflowEntry' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTpPortOverflowTable.Dot1dTpPortOverflowEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dTpPort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dtpport',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTpPortInOverflowDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated
                dot1dTpPortInDiscards counter has overflowed.
                ''',
                'dot1dtpportinoverflowdiscards',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortInOverflowFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated dot1dTpPortInFrames
                counter has overflowed.
                ''',
                'dot1dtpportinoverflowframes',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortOutOverflowFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated dot1dTpPortOutFrames
                counter has overflowed.
                ''',
                'dot1dtpportoutoverflowframes',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTpPortOverflowEntry',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTpPortOverflowTable' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTpPortOverflowTable',
            False, 
            [
            _MetaInfoClassMember('dot1dTpPortOverflowEntry', REFERENCE_LIST, 'Dot1dTpPortOverflowEntry' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTpPortOverflowTable.Dot1dTpPortOverflowEntry', 
                [], [], 
                '''                The most significant bits of statistics counters for a high-
                capacity interface of a transparent bridge.  Each object is
                associated with a corresponding object in dot1dTpPortTable
                that indicates the least significant bits of the counter.
                ''',
                'dot1dtpportoverflowentry',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTpPortOverflowTable',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTrafficClassTable.Dot1dTrafficClassEntry' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTrafficClassTable.Dot1dTrafficClassEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTrafficClassPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Priority value determined for the received frame.
                This value is equivalent to the priority indicated in
                the tagged frame received, or one of the evaluated
                priorities, determined according to the media-type.
                
                For untagged frames received from Ethernet media, this
                value is equal to the dot1dPortDefaultUserPriority value
                for the ingress port.
                
                For untagged frames received from non-Ethernet media,
                this value is equal to the dot1dRegenUserPriority value
                for the ingress port and media-specific user priority.
                ''',
                'dot1dtrafficclasspriority',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dTrafficClass', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Traffic Class the received frame is mapped to.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dtrafficclass',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTrafficClassEntry',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dTrafficClassTable' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dTrafficClassTable',
            False, 
            [
            _MetaInfoClassMember('dot1dTrafficClassEntry', REFERENCE_LIST, 'Dot1dTrafficClassEntry' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTrafficClassTable.Dot1dTrafficClassEntry', 
                [], [], 
                '''                User Priority to Traffic Class mapping.
                ''',
                'dot1dtrafficclassentry',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dTrafficClassTable',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dUserPriorityRegenTable.Dot1dUserPriorityRegenEntry' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dUserPriorityRegenTable.Dot1dUserPriorityRegenEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dUserPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The User Priority for a frame received on this port.
                ''',
                'dot1duserpriority',
                'P-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1dRegenUserPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                The Regenerated User Priority that the incoming User
                
                Priority is mapped to for this port.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1dregenuserpriority',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dUserPriorityRegenEntry',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB.Dot1dUserPriorityRegenTable' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB.Dot1dUserPriorityRegenTable',
            False, 
            [
            _MetaInfoClassMember('dot1dUserPriorityRegenEntry', REFERENCE_LIST, 'Dot1dUserPriorityRegenEntry' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dUserPriorityRegenTable.Dot1dUserPriorityRegenEntry', 
                [], [], 
                '''                A mapping of incoming User Priority to a Regenerated
                User Priority.
                ''',
                'dot1duserpriorityregenentry',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'dot1dUserPriorityRegenTable',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
    'PBRIDGEMIB' : {
        'meta_info' : _MetaInfoClass('PBRIDGEMIB',
            False, 
            [
            _MetaInfoClassMember('dot1dExtBase', REFERENCE_CLASS, 'Dot1dExtBase' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dExtBase', 
                [], [], 
                '''                ''',
                'dot1dextbase',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dPortOutboundAccessPriorityTable', REFERENCE_CLASS, 'Dot1dPortOutboundAccessPriorityTable' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable', 
                [], [], 
                '''                A table mapping Regenerated User Priority to Outbound
                Access Priority.  This is a fixed mapping for all port
                types, with two options for 802.5 Token Ring.
                ''',
                'dot1dportoutboundaccessprioritytable',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpHCPortTable', REFERENCE_CLASS, 'Dot1dTpHCPortTable' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTpHCPortTable', 
                [], [], 
                '''                A table that contains information about every high-
                capacity port that is associated with this transparent
                bridge.
                ''',
                'dot1dtphcporttable',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTpPortOverflowTable', REFERENCE_CLASS, 'Dot1dTpPortOverflowTable' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTpPortOverflowTable', 
                [], [], 
                '''                A table that contains the most-significant bits of
                statistics counters for ports that are associated with this
                transparent bridge that are on high-capacity interfaces, as
                defined in the conformance clauses for this table.  This table
                is provided as a way to read 64-bit counters for agents that
                support only SNMPv1.
                
                Note that the reporting of most-significant and
                least-significant counter bits separately runs the risk of
                missing an overflow of the lower bits in the interval between
                sampling.  The manager must be aware of this possibility, even
                within the same varbindlist, when interpreting the results of
                a request or asynchronous notification.
                ''',
                'dot1dtpportoverflowtable',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dTrafficClassTable', REFERENCE_CLASS, 'Dot1dTrafficClassTable' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dTrafficClassTable', 
                [], [], 
                '''                A table mapping evaluated User Priority to Traffic
                Class, for forwarding by the bridge.  Traffic class is a
                number in the range (0..(dot1dPortNumTrafficClasses-1)).
                ''',
                'dot1dtrafficclasstable',
                'P-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1dUserPriorityRegenTable', REFERENCE_CLASS, 'Dot1dUserPriorityRegenTable' , 'ydk.models.p.P_BRIDGE_MIB', 'PBRIDGEMIB.Dot1dUserPriorityRegenTable', 
                [], [], 
                '''                A list of Regenerated User Priorities for each received
                User Priority on each port of a bridge.  The Regenerated
                User Priority value may be used to index the Traffic
                Class Table for each input port.  This only has effect
                on media that support native User Priority.  The default
                values for Regenerated User Priorities are the same as
                the User Priorities.
                ''',
                'dot1duserpriorityregentable',
                'P-BRIDGE-MIB', False),
            ],
            'P-BRIDGE-MIB',
            'P-BRIDGE-MIB',
            _yang_ns._namespaces['P-BRIDGE-MIB'],
        'ydk.models.p.P_BRIDGE_MIB'
        ),
    },
}
_meta_table['PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable.Dot1dPortOutboundAccessPriorityEntry']['meta_info'].parent =_meta_table['PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTpHCPortTable.Dot1dTpHCPortEntry']['meta_info'].parent =_meta_table['PBRIDGEMIB.Dot1dTpHCPortTable']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTpPortOverflowTable.Dot1dTpPortOverflowEntry']['meta_info'].parent =_meta_table['PBRIDGEMIB.Dot1dTpPortOverflowTable']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTrafficClassTable.Dot1dTrafficClassEntry']['meta_info'].parent =_meta_table['PBRIDGEMIB.Dot1dTrafficClassTable']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dUserPriorityRegenTable.Dot1dUserPriorityRegenEntry']['meta_info'].parent =_meta_table['PBRIDGEMIB.Dot1dUserPriorityRegenTable']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dExtBase']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dPortOutboundAccessPriorityTable']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTpHCPortTable']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTpPortOverflowTable']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dTrafficClassTable']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']
_meta_table['PBRIDGEMIB.Dot1dUserPriorityRegenTable']['meta_info'].parent =_meta_table['PBRIDGEMIB']['meta_info']