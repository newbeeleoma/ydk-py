""" MPLS_LDP_STD_MIB 

Copyright (C) The Internet Society (2004). The
initial version of this MIB module was published


in RFC 3815. For full legal notices see the RFC
itself or see\:
http\://www.ietf.org/copyrights/ianamib.html

This MIB contains managed object definitions for the
'Multiprotocol Label Switching, Label Distribution
Protocol, LDP' document.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class MPLSLDPSTDMIB(Entity):
    """
    
    
    .. attribute:: mplsldplsrobjects
    
    	
    	**type**\:  :py:class:`MplsLdpLsrObjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLsrObjects>`
    
    	**config**\: False
    
    .. attribute:: mplsldpentityobjects
    
    	
    	**type**\:  :py:class:`MplsLdpEntityObjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityObjects>`
    
    	**config**\: False
    
    .. attribute:: mplsldpsessionobjects
    
    	
    	**type**\:  :py:class:`MplsLdpSessionObjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionObjects>`
    
    	**config**\: False
    
    .. attribute:: mplsfecobjects
    
    	
    	**type**\:  :py:class:`MplsFecObjects <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecObjects>`
    
    	**config**\: False
    
    .. attribute:: mplsldpentitytable
    
    	This table contains information about the MPLS Label Distribution Protocol Entities which exist on this Label Switching Router (LSR) or Label Edge Router (LER)
    	**type**\:  :py:class:`MplsLdpEntityTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable>`
    
    	**config**\: False
    
    .. attribute:: mplsldppeertable
    
    	Information about LDP peers known by Entities in the mplsLdpEntityTable.  The information in this table is based on information from the Entity\-Peer interaction during session initialization but is not appropriate for the mplsLdpSessionTable, because objects in this table may or may not be used in session establishment
    	**type**\:  :py:class:`MplsLdpPeerTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable>`
    
    	**config**\: False
    
    .. attribute:: mplsldphelloadjacencytable
    
    	A table of Hello Adjacencies for Sessions
    	**type**\:  :py:class:`MplsLdpHelloAdjacencyTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable>`
    
    	**config**\: False
    
    .. attribute:: mplsinsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsInSegmentTable in the MPLS\-LSR\-STD\-MIB module
    	**type**\:  :py:class:`MplsInSegmentLdpLspTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsInSegmentLdpLspTable>`
    
    	**config**\: False
    
    .. attribute:: mplsoutsegmentldplsptable
    
    	A table of LDP LSP's which map to the mplsOutSegmentTable in the MPLS\-LSR\-STD\-MIB
    	**type**\:  :py:class:`MplsOutSegmentLdpLspTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable>`
    
    	**config**\: False
    
    .. attribute:: mplsfectable
    
    	This table represents the FEC (Forwarding Equivalence Class) Information associated with an LSP
    	**type**\:  :py:class:`MplsFecTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable>`
    
    	**config**\: False
    
    .. attribute:: mplsldplspfectable
    
    	A table which shows the relationship between LDP LSPs and FECs.  Each row represents a single LDP LSP to FEC association
    	**type**\:  :py:class:`MplsLdpLspFecTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable>`
    
    	**config**\: False
    
    .. attribute:: mplsldpsessionpeeraddrtable
    
    	This table 'extends' the mplsLdpSessionTable. This table is used to store Label Address Information from Label Address Messages received by this LSR from Peers.  This table is read\-only and should be updated   when Label Withdraw Address Messages are received, i.e., Rows should be deleted as appropriate.  NOTE\:  since more than one address may be contained in a Label Address Message, this table 'sparse augments', the mplsLdpSessionTable's information
    	**type**\:  :py:class:`MplsLdpSessionPeerAddrTable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'MPLS-LDP-STD-MIB'
    _revision = '2004-06-03'

    def __init__(self):
        super(MPLSLDPSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "MPLS-LDP-STD-MIB"
        self.yang_parent_name = "MPLS-LDP-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("mplsLdpLsrObjects", ("mplsldplsrobjects", MPLSLDPSTDMIB.MplsLdpLsrObjects)), ("mplsLdpEntityObjects", ("mplsldpentityobjects", MPLSLDPSTDMIB.MplsLdpEntityObjects)), ("mplsLdpSessionObjects", ("mplsldpsessionobjects", MPLSLDPSTDMIB.MplsLdpSessionObjects)), ("mplsFecObjects", ("mplsfecobjects", MPLSLDPSTDMIB.MplsFecObjects)), ("mplsLdpEntityTable", ("mplsldpentitytable", MPLSLDPSTDMIB.MplsLdpEntityTable)), ("mplsLdpPeerTable", ("mplsldppeertable", MPLSLDPSTDMIB.MplsLdpPeerTable)), ("mplsLdpHelloAdjacencyTable", ("mplsldphelloadjacencytable", MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable)), ("mplsInSegmentLdpLspTable", ("mplsinsegmentldplsptable", MPLSLDPSTDMIB.MplsInSegmentLdpLspTable)), ("mplsOutSegmentLdpLspTable", ("mplsoutsegmentldplsptable", MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable)), ("mplsFecTable", ("mplsfectable", MPLSLDPSTDMIB.MplsFecTable)), ("mplsLdpLspFecTable", ("mplsldplspfectable", MPLSLDPSTDMIB.MplsLdpLspFecTable)), ("mplsLdpSessionPeerAddrTable", ("mplsldpsessionpeeraddrtable", MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable))])
        self._leafs = OrderedDict()

        self.mplsldplsrobjects = MPLSLDPSTDMIB.MplsLdpLsrObjects()
        self.mplsldplsrobjects.parent = self
        self._children_name_map["mplsldplsrobjects"] = "mplsLdpLsrObjects"

        self.mplsldpentityobjects = MPLSLDPSTDMIB.MplsLdpEntityObjects()
        self.mplsldpentityobjects.parent = self
        self._children_name_map["mplsldpentityobjects"] = "mplsLdpEntityObjects"

        self.mplsldpsessionobjects = MPLSLDPSTDMIB.MplsLdpSessionObjects()
        self.mplsldpsessionobjects.parent = self
        self._children_name_map["mplsldpsessionobjects"] = "mplsLdpSessionObjects"

        self.mplsfecobjects = MPLSLDPSTDMIB.MplsFecObjects()
        self.mplsfecobjects.parent = self
        self._children_name_map["mplsfecobjects"] = "mplsFecObjects"

        self.mplsldpentitytable = MPLSLDPSTDMIB.MplsLdpEntityTable()
        self.mplsldpentitytable.parent = self
        self._children_name_map["mplsldpentitytable"] = "mplsLdpEntityTable"

        self.mplsldppeertable = MPLSLDPSTDMIB.MplsLdpPeerTable()
        self.mplsldppeertable.parent = self
        self._children_name_map["mplsldppeertable"] = "mplsLdpPeerTable"

        self.mplsldphelloadjacencytable = MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable()
        self.mplsldphelloadjacencytable.parent = self
        self._children_name_map["mplsldphelloadjacencytable"] = "mplsLdpHelloAdjacencyTable"

        self.mplsinsegmentldplsptable = MPLSLDPSTDMIB.MplsInSegmentLdpLspTable()
        self.mplsinsegmentldplsptable.parent = self
        self._children_name_map["mplsinsegmentldplsptable"] = "mplsInSegmentLdpLspTable"

        self.mplsoutsegmentldplsptable = MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable()
        self.mplsoutsegmentldplsptable.parent = self
        self._children_name_map["mplsoutsegmentldplsptable"] = "mplsOutSegmentLdpLspTable"

        self.mplsfectable = MPLSLDPSTDMIB.MplsFecTable()
        self.mplsfectable.parent = self
        self._children_name_map["mplsfectable"] = "mplsFecTable"

        self.mplsldplspfectable = MPLSLDPSTDMIB.MplsLdpLspFecTable()
        self.mplsldplspfectable.parent = self
        self._children_name_map["mplsldplspfectable"] = "mplsLdpLspFecTable"

        self.mplsldpsessionpeeraddrtable = MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable()
        self.mplsldpsessionpeeraddrtable.parent = self
        self._children_name_map["mplsldpsessionpeeraddrtable"] = "mplsLdpSessionPeerAddrTable"
        self._segment_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(MPLSLDPSTDMIB, [], name, value)


    class MplsLdpLsrObjects(Entity):
        """
        
        
        .. attribute:: mplsldplsrid
        
        	The Label Switching Router's Identifier
        	**type**\: str
        
        	**length:** 4..4
        
        	**config**\: False
        
        .. attribute:: mplsldplsrloopdetectioncapable
        
        	A indication of whether this Label Switching Router supports loop detection.  none(1) \-\- Loop Detection is not supported            on this LSR.  other(2) \-\- Loop Detection is supported but             by a method other than those             listed below.  hopCount(3) \-\- Loop Detection is supported by                Hop Count only.  pathVector(4) \-\- Loop Detection is supported by                  Path Vector only.  hopCountAndPathVector(5) \-\- Loop Detection is                      supported by both Hop Count                      And Path Vector.  Since Loop Detection is determined during Session Initialization, an individual session may not be running with loop detection.  This object simply gives an indication of whether or not the LSR has the ability to support Loop Detection and which types
        	**type**\:  :py:class:`MplsLdpLsrLoopDetectionCapable <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLsrObjects.MplsLdpLsrLoopDetectionCapable>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpLsrObjects, self).__init__()

            self.yang_name = "mplsLdpLsrObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsldplsrid', (YLeaf(YType.str, 'mplsLdpLsrId'), ['str'])),
                ('mplsldplsrloopdetectioncapable', (YLeaf(YType.enumeration, 'mplsLdpLsrLoopDetectionCapable'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpLsrObjects.MplsLdpLsrLoopDetectionCapable')])),
            ])
            self.mplsldplsrid = None
            self.mplsldplsrloopdetectioncapable = None
            self._segment_path = lambda: "mplsLdpLsrObjects"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpLsrObjects, ['mplsldplsrid', 'mplsldplsrloopdetectioncapable'], name, value)

        class MplsLdpLsrLoopDetectionCapable(Enum):
            """
            MplsLdpLsrLoopDetectionCapable (Enum Class)

            A indication of whether this

            Label Switching Router supports

            loop detection.

            none(1) \-\- Loop Detection is not supported

                       on this LSR.

            other(2) \-\- Loop Detection is supported but

                        by a method other than those

                        listed below.

            hopCount(3) \-\- Loop Detection is supported by

                           Hop Count only.

            pathVector(4) \-\- Loop Detection is supported by

                             Path Vector only.

            hopCountAndPathVector(5) \-\- Loop Detection is

                                 supported by both Hop Count

                                 And Path Vector.

            Since Loop Detection is determined during

            Session Initialization, an individual session

            may not be running with loop detection.  This

            object simply gives an indication of whether or not the

            LSR has the ability to support Loop Detection and

            which types.

            .. data:: none = 1

            .. data:: other = 2

            .. data:: hopCount = 3

            .. data:: pathVector = 4

            .. data:: hopCountAndPathVector = 5

            """

            none = Enum.YLeaf(1, "none")

            other = Enum.YLeaf(2, "other")

            hopCount = Enum.YLeaf(3, "hopCount")

            pathVector = Enum.YLeaf(4, "pathVector")

            hopCountAndPathVector = Enum.YLeaf(5, "hopCountAndPathVector")




    class MplsLdpEntityObjects(Entity):
        """
        
        
        .. attribute:: mplsldpentitylastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion of an entry to/from the mplsLdpEntityTable/mplsLdpEntityStatsTable, or the most recent change in value of any objects in the mplsLdpEntityTable.   If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: mplsldpentityindexnext
        
        	This object contains an appropriate value to be used for mplsLdpEntityIndex when creating entries in the mplsLdpEntityTable. The value 0 indicates that no unassigned entries are available
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpEntityObjects, self).__init__()

            self.yang_name = "mplsLdpEntityObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsldpentitylastchange', (YLeaf(YType.uint32, 'mplsLdpEntityLastChange'), ['int'])),
                ('mplsldpentityindexnext', (YLeaf(YType.uint32, 'mplsLdpEntityIndexNext'), ['int'])),
            ])
            self.mplsldpentitylastchange = None
            self.mplsldpentityindexnext = None
            self._segment_path = lambda: "mplsLdpEntityObjects"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpEntityObjects, ['mplsldpentitylastchange', 'mplsldpentityindexnext'], name, value)



    class MplsLdpSessionObjects(Entity):
        """
        
        
        .. attribute:: mplsldppeerlastchange
        
        	The value of sysUpTime at the time of the most recent addition or deletion to/from the mplsLdpPeerTable/mplsLdpSessionTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: mplsldplspfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpLspFecTable or the most recent change in values to any objects in the mplsLdpLspFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpSessionObjects, self).__init__()

            self.yang_name = "mplsLdpSessionObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsldppeerlastchange', (YLeaf(YType.uint32, 'mplsLdpPeerLastChange'), ['int'])),
                ('mplsldplspfeclastchange', (YLeaf(YType.uint32, 'mplsLdpLspFecLastChange'), ['int'])),
            ])
            self.mplsldppeerlastchange = None
            self.mplsldplspfeclastchange = None
            self._segment_path = lambda: "mplsLdpSessionObjects"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpSessionObjects, ['mplsldppeerlastchange', 'mplsldplspfeclastchange'], name, value)



    class MplsFecObjects(Entity):
        """
        
        
        .. attribute:: mplsfeclastchange
        
        	The value of sysUpTime at the time of the most recent addition/deletion of an entry to/from the mplsLdpFectTable or the most recent change in values to any objects in the mplsLdpFecTable.  If no such changes have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: mplsfecindexnext
        
        	This object contains an appropriate value to be used for mplsFecIndex when creating entries in the mplsFecTable. The value 0 indicates that no unassigned entries are available
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsFecObjects, self).__init__()

            self.yang_name = "mplsFecObjects"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('mplsfeclastchange', (YLeaf(YType.uint32, 'mplsFecLastChange'), ['int'])),
                ('mplsfecindexnext', (YLeaf(YType.uint32, 'mplsFecIndexNext'), ['int'])),
            ])
            self.mplsfeclastchange = None
            self.mplsfecindexnext = None
            self._segment_path = lambda: "mplsFecObjects"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsFecObjects, ['mplsfeclastchange', 'mplsfecindexnext'], name, value)



    class MplsLdpEntityTable(Entity):
        """
        This table contains information about the
        MPLS Label Distribution Protocol Entities which
        exist on this Label Switching Router (LSR)
        or Label Edge Router (LER).
        
        .. attribute:: mplsldpentityentry
        
        	An entry in this table represents an LDP entity. An entry can be created by a network administrator or by an SNMP agent as instructed by LDP
        	**type**\: list of  		 :py:class:`MplsLdpEntityEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpEntityTable, self).__init__()

            self.yang_name = "mplsLdpEntityTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLdpEntityEntry", ("mplsldpentityentry", MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry))])
            self._leafs = OrderedDict()

            self.mplsldpentityentry = YList(self)
            self._segment_path = lambda: "mplsLdpEntityTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpEntityTable, [], name, value)


        class MplsLdpEntityEntry(Entity):
            """
            An entry in this table represents an LDP entity.
            An entry can be created by a network administrator
            or by an SNMP agent as instructed by LDP.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	The LDP identifier
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	This index is used as a secondary index to uniquely identify this row.  Before creating a row in this table, the 'mplsLdpEntityIndexNext' object should be retrieved. That value should be used for the value of this index when creating a row in this table.  NOTE\:  if a value of zero (0) is retrieved, that indicates that no rows can be created in this table at this time.  A secondary index (this object) is meaningful to some but not all, LDP implementations.  For example an LDP implementation which uses PPP would use this index to differentiate PPP sub\-links.  Another way to use this index is to give this the value of ifIndex.  However, this is dependant   on the implementation
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentityprotocolversion
            
            	The version number of the LDP protocol which will be used in the session initialization message.  Section 3.5.3 in the LDP Specification specifies that the version of the LDP protocol is negotiated during session establishment. The value of this object represents the value that is sent in the initialization message
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: mplsldpentityadminstatus
            
            	The administrative status of this LDP Entity. If this object is changed from 'enable' to 'disable' and this entity has already attempted to establish contact with a Peer, then all contact with that Peer is lost and all information from that Peer needs to be removed from the MIB. (This implies that the network management subsystem should clean up any related entry in the mplsLdpPeerTable.  This further implies that a 'tear\-down' for that session is issued and the session and all information related to that session cease to exist).  At this point the operator is able to change values which are related to this entity.  When the admin status is set back to 'enable', then this Entity will attempt to establish a new session with the Peer
            	**type**\:  :py:class:`MplsLdpEntityAdminStatus <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityoperstatus
            
            	The operational status of this LDP Entity.  The value of unknown(1) indicates that the operational status cannot be determined at this time.  The value of unknown should be a transient condition before changing to enabled(2) or disabled(3)
            	**type**\:  :py:class:`MplsLdpEntityOperStatus <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityOperStatus>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitytcpport
            
            	The TCP Port for LDP.  The default value is the well\-known value of this port
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: mplsldpentityudpdscport
            
            	The UDP Discovery Port for LDP.  The default value is the well\-known value for this port
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: mplsldpentitymaxpdulength
            
            	The maximum PDU Length that is sent in the Common Session Parameters of an Initialization Message. According to the LDP Specification [RFC3036] a value of 255 or less specifies the default maximum length of 4096 octets, this is why the value of this object starts at 256.  The operator should explicitly choose the default value (i.e., 4096), or some other value.  The receiving LSR MUST calculate the maximum PDU length for the session by using the smaller of its and its peer's proposals for Max PDU Length
            	**type**\: int
            
            	**range:** 256..65535
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: mplsldpentitykeepaliveholdtimer
            
            	The 16\-bit integer value which is the proposed keep alive hold timer for this LDP Entity
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: mplsldpentityhelloholdtimer
            
            	The 16\-bit integer value which is the proposed Hello hold timer for this LDP Entity. The Hello Hold time in seconds.   An LSR maintains a record of Hellos received from potential peers.  This object represents the Hold Time in the Common Hello Parameters TLV of the Hello Message.  A value of 0 is a default value and should be interpretted in conjunction with the mplsLdpEntityTargetPeer object.  If the value of this object is 0\: if the value of the mplsLdpEntityTargetPeer object is false(2), then this specifies that the Hold Time's actual default value is 15 seconds (i.e., the default Hold time for Link Hellos is 15 seconds).  Otherwise if the value of the mplsLdpEntityTargetPeer object is true(1), then this specifies that the Hold Time's actual default value is 45 seconds (i.e., the default Hold time for Targeted Hellos is 45 seconds).  A value of 65535 means infinite (i.e., wait forever).  All other values represent the amount of time in seconds to wait for a Hello Message.  Setting the hold time to a value smaller than 15 is not recommended, although not forbidden according to RFC3036
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: mplsldpentityinitsessionthreshold
            
            	When attempting to establish a session with a given Peer, the given LDP Entity should send out the SNMP notification, 'mplsLdpInitSessionThresholdExceeded', when the number of Session Initialization messages sent exceeds this threshold.  The notification is used to notify an operator when this Entity and its Peer are possibly engaged in an endless sequence of messages as each NAKs the other's   Initialization messages with Error Notification messages.  Setting this threshold which triggers the notification is one way to notify the operator.  The notification should be generated each time this threshold is exceeded and for every subsequent Initialization message which is NAK'd with an Error Notification message after this threshold is exceeded.  A value of 0 (zero) for this object indicates that the threshold is infinity, thus the SNMP notification will never be generated
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: mplsldpentitylabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\:  :py:class:`MplsLabelDistributionMethod <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLabelDistributionMethod>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitylabelretentionmode
            
            	The LDP Entity can be configured to use either conservative or liberal label retention mode.  If the value of this object is conservative(1) then advertized label mappings are retained only if they will be used to forward packets, i.e., if label came from a valid next hop.  If the value of this object is liberal(2) then all advertized label mappings are retained whether they are from a valid next hop or not
            	**type**\:  :py:class:`MplsRetentionMode <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsRetentionMode>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitypathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Detection for Path Vectors is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path Vectors is enabled, and the Path Vector Limit is this value. Also, the value of the object, 'mplsLdpLsrLoopDetectionCapable', must be set to either 'pathVector(4)' or 'hopCountAndPathVector(5)', if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsldpentityhopcountlimit
            
            	If the value of this object is 0 (zero), then Loop Detection using Hop Counters is disabled.  If the value of this object is greater than 0 (zero) then Loop Detection using Hop Counters is enabled, and this object specifies this Entity's maximum allowable value for the Hop Count. Also, the value of the object mplsLdpLsrLoopDetectionCapable must be set to either 'hopCount(3)' or 'hopCountAndPathVector(5)' if this object has a value greater than 0 (zero), otherwise it is ignored
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsldpentitytransportaddrkind
            
            	This specifies whether the loopback or interface address is to be used as the transport address in the transport address TLV of the hello message.  If the value is interface(1), then the IP address of the interface from which hello messages are sent is used as the transport address in the hello message.  Otherwise, if the value is loopback(2), then the IP address of the loopback interface is used as the transport address in the hello message
            	**type**\:  :py:class:`MplsLdpEntityTransportAddrKind <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityTransportAddrKind>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitytargetpeer
            
            	If this LDP entity uses targeted peer then set this to true
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: mplsldpentitytargetpeeraddrtype
            
            	The type of the internetwork layer address used for the Extended Discovery.  This object indicates how the value of mplsLdpEntityTargetPeerAddr is to be interpreted
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitytargetpeeraddr
            
            	The value of the internetwork layer address used for the Extended Discovery.  The value of mplsLdpEntityTargetPeerAddrType specifies how this address is to be interpreted
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsldpentitylabeltype
            
            	Specifies the optional parameters for the LDP Initialization Message.  If the value is generic(1) then no optional parameters will be sent in the LDP Initialization message associated with this Entity.  If the value is atmParameters(2) then a row must be created in the mplsLdpEntityAtmTable, which corresponds to this entry.  If the value is frameRelayParameters(3) then a row must be created in the mplsLdpEntityFrameRelayTable, which corresponds to this entry
            	**type**\:  :py:class:`MplsLdpLabelType <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLdpLabelType>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitydiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entity's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this entity of any Counter32 object contained in the 'mplsLdpEntityStatsTable'.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityrowstatus
            
            	The status of this conceptual row.  All writable objects in this row may be modified at any time, however, as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object, if a session has been initiated with a Peer, changing objects in this table will wreak havoc with the session and interrupt traffic.  To repeat again\: the recommended procedure is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. Then, change objects in this entry, then set the mplsLdpEntityAdminStatus to enable, which enables a new session to be initiated
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatssessionattempts
            
            	A count of the Session Initialization messages which were sent or received by this LDP Entity and were NAK'd.   In other words, this counter counts the number of session initializations that failed.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatssessionrejectednohelloerrors
            
            	A count of the Session Rejected/No Hello Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatssessionrejectedaderrors
            
            	A count of the Session Rejected/Parameters Advertisement Mode Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatssessionrejectedmaxpduerrors
            
            	A count of the Session Rejected/Parameters  Max Pdu Length Error Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatssessionrejectedlrerrors
            
            	A count of the Session Rejected/Parameters Label Range Notification Messages sent or received by this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsbadldpidentifiererrors
            
            	This object counts the number of Bad LDP Identifier Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsbadpdulengtherrors
            
            	This object counts the number of Bad PDU Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsbadmessagelengtherrors
            
            	This object counts the number of Bad Message Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsbadtlvlengtherrors
            
            	This object counts the number of Bad TLV Length Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsmalformedtlvvalueerrors
            
            	This object counts the number of Malformed TLV Value Fatal Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatskeepalivetimerexperrors
            
            	This object counts the number of Session Keep Alive Timer Expired Errors detected by the session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsshutdownreceivednotifications
            
            	This object counts the number of Shutdown Notifications received related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpentitystatsshutdownsentnotifications
            
            	This object counts the number of Shutdown Notfications sent related to session(s) (past and present) associated with this LDP Entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   mplsLdpEntityDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry, self).__init__()

                self.yang_name = "mplsLdpEntityEntry"
                self.yang_parent_name = "mplsLdpEntityTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.uint32, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldpentityprotocolversion', (YLeaf(YType.uint32, 'mplsLdpEntityProtocolVersion'), ['int'])),
                    ('mplsldpentityadminstatus', (YLeaf(YType.enumeration, 'mplsLdpEntityAdminStatus'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityAdminStatus')])),
                    ('mplsldpentityoperstatus', (YLeaf(YType.enumeration, 'mplsLdpEntityOperStatus'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityOperStatus')])),
                    ('mplsldpentitytcpport', (YLeaf(YType.uint16, 'mplsLdpEntityTcpPort'), ['int'])),
                    ('mplsldpentityudpdscport', (YLeaf(YType.uint16, 'mplsLdpEntityUdpDscPort'), ['int'])),
                    ('mplsldpentitymaxpdulength', (YLeaf(YType.uint32, 'mplsLdpEntityMaxPduLength'), ['int'])),
                    ('mplsldpentitykeepaliveholdtimer', (YLeaf(YType.uint32, 'mplsLdpEntityKeepAliveHoldTimer'), ['int'])),
                    ('mplsldpentityhelloholdtimer', (YLeaf(YType.uint32, 'mplsLdpEntityHelloHoldTimer'), ['int'])),
                    ('mplsldpentityinitsessionthreshold', (YLeaf(YType.int32, 'mplsLdpEntityInitSessionThreshold'), ['int'])),
                    ('mplsldpentitylabeldistmethod', (YLeaf(YType.enumeration, 'mplsLdpEntityLabelDistMethod'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLabelDistributionMethod', '')])),
                    ('mplsldpentitylabelretentionmode', (YLeaf(YType.enumeration, 'mplsLdpEntityLabelRetentionMode'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsRetentionMode', '')])),
                    ('mplsldpentitypathvectorlimit', (YLeaf(YType.int32, 'mplsLdpEntityPathVectorLimit'), ['int'])),
                    ('mplsldpentityhopcountlimit', (YLeaf(YType.int32, 'mplsLdpEntityHopCountLimit'), ['int'])),
                    ('mplsldpentitytransportaddrkind', (YLeaf(YType.enumeration, 'mplsLdpEntityTransportAddrKind'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpEntityTable.MplsLdpEntityEntry.MplsLdpEntityTransportAddrKind')])),
                    ('mplsldpentitytargetpeer', (YLeaf(YType.boolean, 'mplsLdpEntityTargetPeer'), ['bool'])),
                    ('mplsldpentitytargetpeeraddrtype', (YLeaf(YType.enumeration, 'mplsLdpEntityTargetPeerAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('mplsldpentitytargetpeeraddr', (YLeaf(YType.str, 'mplsLdpEntityTargetPeerAddr'), ['str'])),
                    ('mplsldpentitylabeltype', (YLeaf(YType.enumeration, 'mplsLdpEntityLabelType'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLdpLabelType', '')])),
                    ('mplsldpentitydiscontinuitytime', (YLeaf(YType.uint32, 'mplsLdpEntityDiscontinuityTime'), ['int'])),
                    ('mplsldpentitystoragetype', (YLeaf(YType.enumeration, 'mplsLdpEntityStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsldpentityrowstatus', (YLeaf(YType.enumeration, 'mplsLdpEntityRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('mplsldpentitystatssessionattempts', (YLeaf(YType.uint32, 'mplsLdpEntityStatsSessionAttempts'), ['int'])),
                    ('mplsldpentitystatssessionrejectednohelloerrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsSessionRejectedNoHelloErrors'), ['int'])),
                    ('mplsldpentitystatssessionrejectedaderrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsSessionRejectedAdErrors'), ['int'])),
                    ('mplsldpentitystatssessionrejectedmaxpduerrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsSessionRejectedMaxPduErrors'), ['int'])),
                    ('mplsldpentitystatssessionrejectedlrerrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsSessionRejectedLRErrors'), ['int'])),
                    ('mplsldpentitystatsbadldpidentifiererrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsBadLdpIdentifierErrors'), ['int'])),
                    ('mplsldpentitystatsbadpdulengtherrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsBadPduLengthErrors'), ['int'])),
                    ('mplsldpentitystatsbadmessagelengtherrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsBadMessageLengthErrors'), ['int'])),
                    ('mplsldpentitystatsbadtlvlengtherrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsBadTlvLengthErrors'), ['int'])),
                    ('mplsldpentitystatsmalformedtlvvalueerrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsMalformedTlvValueErrors'), ['int'])),
                    ('mplsldpentitystatskeepalivetimerexperrors', (YLeaf(YType.uint32, 'mplsLdpEntityStatsKeepAliveTimerExpErrors'), ['int'])),
                    ('mplsldpentitystatsshutdownreceivednotifications', (YLeaf(YType.uint32, 'mplsLdpEntityStatsShutdownReceivedNotifications'), ['int'])),
                    ('mplsldpentitystatsshutdownsentnotifications', (YLeaf(YType.uint32, 'mplsLdpEntityStatsShutdownSentNotifications'), ['int'])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldpentityprotocolversion = None
                self.mplsldpentityadminstatus = None
                self.mplsldpentityoperstatus = None
                self.mplsldpentitytcpport = None
                self.mplsldpentityudpdscport = None
                self.mplsldpentitymaxpdulength = None
                self.mplsldpentitykeepaliveholdtimer = None
                self.mplsldpentityhelloholdtimer = None
                self.mplsldpentityinitsessionthreshold = None
                self.mplsldpentitylabeldistmethod = None
                self.mplsldpentitylabelretentionmode = None
                self.mplsldpentitypathvectorlimit = None
                self.mplsldpentityhopcountlimit = None
                self.mplsldpentitytransportaddrkind = None
                self.mplsldpentitytargetpeer = None
                self.mplsldpentitytargetpeeraddrtype = None
                self.mplsldpentitytargetpeeraddr = None
                self.mplsldpentitylabeltype = None
                self.mplsldpentitydiscontinuitytime = None
                self.mplsldpentitystoragetype = None
                self.mplsldpentityrowstatus = None
                self.mplsldpentitystatssessionattempts = None
                self.mplsldpentitystatssessionrejectednohelloerrors = None
                self.mplsldpentitystatssessionrejectedaderrors = None
                self.mplsldpentitystatssessionrejectedmaxpduerrors = None
                self.mplsldpentitystatssessionrejectedlrerrors = None
                self.mplsldpentitystatsbadldpidentifiererrors = None
                self.mplsldpentitystatsbadpdulengtherrors = None
                self.mplsldpentitystatsbadmessagelengtherrors = None
                self.mplsldpentitystatsbadtlvlengtherrors = None
                self.mplsldpentitystatsmalformedtlvvalueerrors = None
                self.mplsldpentitystatskeepalivetimerexperrors = None
                self.mplsldpentitystatsshutdownreceivednotifications = None
                self.mplsldpentitystatsshutdownsentnotifications = None
                self._segment_path = lambda: "mplsLdpEntityEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpEntityTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldpentityprotocolversion', 'mplsldpentityadminstatus', 'mplsldpentityoperstatus', 'mplsldpentitytcpport', 'mplsldpentityudpdscport', 'mplsldpentitymaxpdulength', 'mplsldpentitykeepaliveholdtimer', 'mplsldpentityhelloholdtimer', 'mplsldpentityinitsessionthreshold', 'mplsldpentitylabeldistmethod', 'mplsldpentitylabelretentionmode', 'mplsldpentitypathvectorlimit', 'mplsldpentityhopcountlimit', 'mplsldpentitytransportaddrkind', 'mplsldpentitytargetpeer', 'mplsldpentitytargetpeeraddrtype', 'mplsldpentitytargetpeeraddr', 'mplsldpentitylabeltype', 'mplsldpentitydiscontinuitytime', 'mplsldpentitystoragetype', 'mplsldpentityrowstatus', 'mplsldpentitystatssessionattempts', 'mplsldpentitystatssessionrejectednohelloerrors', 'mplsldpentitystatssessionrejectedaderrors', 'mplsldpentitystatssessionrejectedmaxpduerrors', 'mplsldpentitystatssessionrejectedlrerrors', 'mplsldpentitystatsbadldpidentifiererrors', 'mplsldpentitystatsbadpdulengtherrors', 'mplsldpentitystatsbadmessagelengtherrors', 'mplsldpentitystatsbadtlvlengtherrors', 'mplsldpentitystatsmalformedtlvvalueerrors', 'mplsldpentitystatskeepalivetimerexperrors', 'mplsldpentitystatsshutdownreceivednotifications', 'mplsldpentitystatsshutdownsentnotifications'], name, value)

            class MplsLdpEntityAdminStatus(Enum):
                """
                MplsLdpEntityAdminStatus (Enum Class)

                The administrative status of this LDP Entity.

                If this object is changed from 'enable' to 'disable'

                and this entity has already attempted to establish

                contact with a Peer, then all contact with that

                Peer is lost and all information from that Peer

                needs to be removed from the MIB. (This implies

                that the network management subsystem should clean

                up any related entry in the mplsLdpPeerTable.  This

                further implies that a 'tear\-down' for that session

                is issued and the session and all information related

                to that session cease to exist).

                At this point the operator is able to change values

                which are related to this entity.

                When the admin status is set back to 'enable', then

                this Entity will attempt to establish a new session

                with the Peer.

                .. data:: enable = 1

                .. data:: disable = 2

                """

                enable = Enum.YLeaf(1, "enable")

                disable = Enum.YLeaf(2, "disable")


            class MplsLdpEntityOperStatus(Enum):
                """
                MplsLdpEntityOperStatus (Enum Class)

                The operational status of this LDP Entity.

                The value of unknown(1) indicates that the

                operational status cannot be determined at

                this time.  The value of unknown should be

                a transient condition before changing

                to enabled(2) or disabled(3).

                .. data:: unknown = 1

                .. data:: enabled = 2

                .. data:: disabled = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                enabled = Enum.YLeaf(2, "enabled")

                disabled = Enum.YLeaf(3, "disabled")


            class MplsLdpEntityTransportAddrKind(Enum):
                """
                MplsLdpEntityTransportAddrKind (Enum Class)

                This specifies whether the loopback or interface

                address is to be used as the transport address

                in the transport address TLV of the

                hello message.

                If the value is interface(1), then the IP

                address of the interface from which hello

                messages are sent is used as the transport

                address in the hello message.

                Otherwise, if the value is loopback(2), then the IP

                address of the loopback interface is used as the

                transport address in the hello message.

                .. data:: interface = 1

                .. data:: loopback = 2

                """

                interface = Enum.YLeaf(1, "interface")

                loopback = Enum.YLeaf(2, "loopback")





    class MplsLdpPeerTable(Entity):
        """
        Information about LDP peers known by Entities in
        the mplsLdpEntityTable.  The information in this table
        is based on information from the Entity\-Peer interaction
        during session initialization but is not appropriate
        for the mplsLdpSessionTable, because objects in this
        table may or may not be used in session establishment.
        
        .. attribute:: mplsldppeerentry
        
        	Information about a single Peer which is related to a Session.  This table is augmented by the mplsLdpSessionTable
        	**type**\: list of  		 :py:class:`MplsLdpPeerEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpPeerTable, self).__init__()

            self.yang_name = "mplsLdpPeerTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLdpPeerEntry", ("mplsldppeerentry", MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry))])
            self._leafs = OrderedDict()

            self.mplsldppeerentry = YList(self)
            self._segment_path = lambda: "mplsLdpPeerTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpPeerTable, [], name, value)


        class MplsLdpPeerEntry(Entity):
            """
            Information about a single Peer which is related
            to a Session.  This table is augmented by
            the mplsLdpSessionTable.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	The LDP identifier of this LDP Peer
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: mplsldppeerlabeldistmethod
            
            	For any given LDP session, the method of label distribution must be specified
            	**type**\:  :py:class:`MplsLabelDistributionMethod <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLabelDistributionMethod>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerpathvectorlimit
            
            	If the value of this object is 0 (zero) then Loop Dection for Path Vectors for this Peer is disabled.  Otherwise, if this object has a value greater than zero, then Loop Dection for Path  Vectors for this Peer is enabled and the Path Vector Limit is this value
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsldppeertransportaddrtype
            
            	The type of the Internet address for the mplsLdpPeerTransportAddr object.  The LDP specification describes this as being either an IPv4 Transport Address or IPv6 Transport   Address which is used in opening the LDP session's TCP connection, or if the optional TLV is not present, then this is the IPv4/IPv6 source address for the UPD packet carrying the Hellos.  This object specifies how the value of the mplsLdpPeerTransportAddr object should be interpreted
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeertransportaddr
            
            	The Internet address advertised by the peer in the Hello Message or the Hello source address.  The type of this address is specified by the value of the mplsLdpPeerTransportAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionstatelastchange
            
            	The value of sysUpTime at the time this Session entered its current state as denoted by the mplsLdpSessionState object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionstate
            
            	The current state of the session, all of the states 1 to 5 are based on the state machine for session negotiation behavior
            	**type**\:  :py:class:`MplsLdpSessionState <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionState>`
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionrole
            
            	During session establishment the LSR/LER takes either the active role or the passive role based on address comparisons.  This object indicates whether this LSR/LER was behaving in an active role or passive role during this session's establishment.  The value of unknown(1), indicates that the role is not able to be determined at the present time
            	**type**\:  :py:class:`MplsLdpSessionRole <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionRole>`
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionprotocolversion
            
            	The version of the LDP Protocol which this session is using.  This is the version of   the LDP protocol which has been negotiated during session initialization
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionkeepaliveholdtimerem
            
            	The keep alive hold time remaining for this session
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionkeepalivetime
            
            	The negotiated KeepAlive Time which represents the amount of seconds between keep alive messages.  The mplsLdpEntityKeepAliveHoldTimer related to this Session is the value that was proposed as the KeepAlive Time for this session.  This value is negotiated during session initialization between the entity's proposed value (i.e., the value configured in mplsLdpEntityKeepAliveHoldTimer) and the peer's proposed KeepAlive Hold Timer value. This value is the smaller of the two proposed values
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: mplsldpsessionmaxpdulength
            
            	The value of maximum allowable length for LDP PDUs for this session.  This value may have been negotiated during the Session Initialization.  This object is related to the mplsLdpEntityMaxPduLength object.  The mplsLdpEntityMaxPduLength object specifies the requested LDP PDU length, and this object reflects the negotiated LDP PDU length between the Entity and the Peer
            	**type**\: int
            
            	**range:** 1..65535
            
            	**config**\: False
            
            	**units**\: octets
            
            .. attribute:: mplsldpsessiondiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this session's counters suffered a discontinuity.  The relevant counters are the specific instances associated with this session of any Counter32 object contained in the mplsLdpSessionStatsTable.  The initial value of this object is the value of sysUpTime when the entry was created in this table.  Also, a command generator can distinguish when a session between a given Entity and Peer goes away and a new session is established.  This value would change and thus indicate to the command generator that this is a different session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionstatsunknownmestypeerrors
            
            	This object counts the number of Unknown Message Type Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionstatsunknowntlverrors
            
            	This object counts the number of Unknown TLV Errors detected by this LSR/LER during this session.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of mplsLdpSessionDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry, self).__init__()

                self.yang_name = "mplsLdpPeerEntry"
                self.yang_parent_name = "mplsLdpPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsldppeerlabeldistmethod', (YLeaf(YType.enumeration, 'mplsLdpPeerLabelDistMethod'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLabelDistributionMethod', '')])),
                    ('mplsldppeerpathvectorlimit', (YLeaf(YType.int32, 'mplsLdpPeerPathVectorLimit'), ['int'])),
                    ('mplsldppeertransportaddrtype', (YLeaf(YType.enumeration, 'mplsLdpPeerTransportAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('mplsldppeertransportaddr', (YLeaf(YType.str, 'mplsLdpPeerTransportAddr'), ['str'])),
                    ('mplsldpsessionstatelastchange', (YLeaf(YType.uint32, 'mplsLdpSessionStateLastChange'), ['int'])),
                    ('mplsldpsessionstate', (YLeaf(YType.enumeration, 'mplsLdpSessionState'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionState')])),
                    ('mplsldpsessionrole', (YLeaf(YType.enumeration, 'mplsLdpSessionRole'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpPeerTable.MplsLdpPeerEntry.MplsLdpSessionRole')])),
                    ('mplsldpsessionprotocolversion', (YLeaf(YType.uint32, 'mplsLdpSessionProtocolVersion'), ['int'])),
                    ('mplsldpsessionkeepaliveholdtimerem', (YLeaf(YType.int32, 'mplsLdpSessionKeepAliveHoldTimeRem'), ['int'])),
                    ('mplsldpsessionkeepalivetime', (YLeaf(YType.uint32, 'mplsLdpSessionKeepAliveTime'), ['int'])),
                    ('mplsldpsessionmaxpdulength', (YLeaf(YType.uint32, 'mplsLdpSessionMaxPduLength'), ['int'])),
                    ('mplsldpsessiondiscontinuitytime', (YLeaf(YType.uint32, 'mplsLdpSessionDiscontinuityTime'), ['int'])),
                    ('mplsldpsessionstatsunknownmestypeerrors', (YLeaf(YType.uint32, 'mplsLdpSessionStatsUnknownMesTypeErrors'), ['int'])),
                    ('mplsldpsessionstatsunknowntlverrors', (YLeaf(YType.uint32, 'mplsLdpSessionStatsUnknownTlvErrors'), ['int'])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsldppeerlabeldistmethod = None
                self.mplsldppeerpathvectorlimit = None
                self.mplsldppeertransportaddrtype = None
                self.mplsldppeertransportaddr = None
                self.mplsldpsessionstatelastchange = None
                self.mplsldpsessionstate = None
                self.mplsldpsessionrole = None
                self.mplsldpsessionprotocolversion = None
                self.mplsldpsessionkeepaliveholdtimerem = None
                self.mplsldpsessionkeepalivetime = None
                self.mplsldpsessionmaxpdulength = None
                self.mplsldpsessiondiscontinuitytime = None
                self.mplsldpsessionstatsunknownmestypeerrors = None
                self.mplsldpsessionstatsunknowntlverrors = None
                self._segment_path = lambda: "mplsLdpPeerEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpPeerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsldppeerlabeldistmethod', 'mplsldppeerpathvectorlimit', 'mplsldppeertransportaddrtype', 'mplsldppeertransportaddr', 'mplsldpsessionstatelastchange', 'mplsldpsessionstate', 'mplsldpsessionrole', 'mplsldpsessionprotocolversion', 'mplsldpsessionkeepaliveholdtimerem', 'mplsldpsessionkeepalivetime', 'mplsldpsessionmaxpdulength', 'mplsldpsessiondiscontinuitytime', 'mplsldpsessionstatsunknownmestypeerrors', 'mplsldpsessionstatsunknowntlverrors'], name, value)

            class MplsLdpSessionRole(Enum):
                """
                MplsLdpSessionRole (Enum Class)

                During session establishment the LSR/LER takes either

                the active role or the passive role based on address

                comparisons.  This object indicates whether this LSR/LER

                was behaving in an active role or passive role during

                this session's establishment.

                The value of unknown(1), indicates that the role is not

                able to be determined at the present time.

                .. data:: unknown = 1

                .. data:: active = 2

                .. data:: passive = 3

                """

                unknown = Enum.YLeaf(1, "unknown")

                active = Enum.YLeaf(2, "active")

                passive = Enum.YLeaf(3, "passive")


            class MplsLdpSessionState(Enum):
                """
                MplsLdpSessionState (Enum Class)

                The current state of the session, all of the

                states 1 to 5 are based on the state machine

                for session negotiation behavior.

                .. data:: nonexistent = 1

                .. data:: initialized = 2

                .. data:: openrec = 3

                .. data:: opensent = 4

                .. data:: operational = 5

                """

                nonexistent = Enum.YLeaf(1, "nonexistent")

                initialized = Enum.YLeaf(2, "initialized")

                openrec = Enum.YLeaf(3, "openrec")

                opensent = Enum.YLeaf(4, "opensent")

                operational = Enum.YLeaf(5, "operational")





    class MplsLdpHelloAdjacencyTable(Entity):
        """
        A table of Hello Adjacencies for Sessions.
        
        .. attribute:: mplsldphelloadjacencyentry
        
        	Each row represents a single LDP Hello Adjacency. An LDP Session can have one or more Hello Adjacencies
        	**type**\: list of  		 :py:class:`MplsLdpHelloAdjacencyEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable, self).__init__()

            self.yang_name = "mplsLdpHelloAdjacencyTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLdpHelloAdjacencyEntry", ("mplsldphelloadjacencyentry", MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry))])
            self._leafs = OrderedDict()

            self.mplsldphelloadjacencyentry = YList(self)
            self._segment_path = lambda: "mplsLdpHelloAdjacencyTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable, [], name, value)


        class MplsLdpHelloAdjacencyEntry(Entity):
            """
            Each row represents a single LDP Hello Adjacency.
            An LDP Session can have one or more Hello
            Adjacencies.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldphelloadjacencyindex  (key)
            
            	An identifier for this specific adjacency
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldphelloadjacencyholdtimerem
            
            	If the value of this object is 65535, this means that the hold time is infinite (i.e., wait forever).  Otherwise, the time remaining for this Hello Adjacency to receive its next Hello Message.  This interval will change when the 'next' Hello Message which corresponds to this Hello Adjacency is received unless it is infinite
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: mplsldphelloadjacencyholdtime
            
            	The Hello hold time which is negotiated between the Entity and the Peer.  The entity associated with this Hello Adjacency issues a proposed Hello Hold Time value in the mplsLdpEntityHelloHoldTimer object.  The peer also proposes a value and this object represents the negotiated value.  A value of 0 means the default, which is 15 seconds for Link Hellos and 45 seconds for Targeted Hellos. A value of 65535 indicates an infinite hold time
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: mplsldphelloadjacencytype
            
            	This adjacency is the result of a 'link' hello if the value of this object is link(1).   Otherwise, it is a result of a 'targeted' hello, targeted(2)
            	**type**\:  :py:class:`MplsLdpHelloAdjacencyType <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry.MplsLdpHelloAdjacencyType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry, self).__init__()

                self.yang_name = "mplsLdpHelloAdjacencyEntry"
                self.yang_parent_name = "mplsLdpHelloAdjacencyTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid','mplsldphelloadjacencyindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsldphelloadjacencyindex', (YLeaf(YType.uint32, 'mplsLdpHelloAdjacencyIndex'), ['int'])),
                    ('mplsldphelloadjacencyholdtimerem', (YLeaf(YType.int32, 'mplsLdpHelloAdjacencyHoldTimeRem'), ['int'])),
                    ('mplsldphelloadjacencyholdtime', (YLeaf(YType.uint32, 'mplsLdpHelloAdjacencyHoldTime'), ['int'])),
                    ('mplsldphelloadjacencytype', (YLeaf(YType.enumeration, 'mplsLdpHelloAdjacencyType'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry.MplsLdpHelloAdjacencyType')])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsldphelloadjacencyindex = None
                self.mplsldphelloadjacencyholdtimerem = None
                self.mplsldphelloadjacencyholdtime = None
                self.mplsldphelloadjacencytype = None
                self._segment_path = lambda: "mplsLdpHelloAdjacencyEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']" + "[mplsLdpHelloAdjacencyIndex='" + str(self.mplsldphelloadjacencyindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpHelloAdjacencyTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsLdpHelloAdjacencyTable.MplsLdpHelloAdjacencyEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsldphelloadjacencyindex', 'mplsldphelloadjacencyholdtimerem', 'mplsldphelloadjacencyholdtime', 'mplsldphelloadjacencytype'], name, value)

            class MplsLdpHelloAdjacencyType(Enum):
                """
                MplsLdpHelloAdjacencyType (Enum Class)

                This adjacency is the result of a 'link'

                hello if the value of this object is link(1).

                Otherwise, it is a result of a 'targeted'

                hello, targeted(2).

                .. data:: link = 1

                .. data:: targeted = 2

                """

                link = Enum.YLeaf(1, "link")

                targeted = Enum.YLeaf(2, "targeted")





    class MplsInSegmentLdpLspTable(Entity):
        """
        A table of LDP LSP's which
        map to the mplsInSegmentTable in the
        MPLS\-LSR\-STD\-MIB module.
        
        .. attribute:: mplsinsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index for the mplsInSegmentTable (mplsInSegmentLdpLspLabelIndex) from the MPLS\-LSR\-STD\-MIB.  The information contained in a row is read\-only
        	**type**\: list of  		 :py:class:`MplsInSegmentLdpLspEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsInSegmentLdpLspTable, self).__init__()

            self.yang_name = "mplsInSegmentLdpLspTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsInSegmentLdpLspEntry", ("mplsinsegmentldplspentry", MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry))])
            self._leafs = OrderedDict()

            self.mplsinsegmentldplspentry = YList(self)
            self._segment_path = lambda: "mplsInSegmentLdpLspTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsInSegmentLdpLspTable, [], name, value)


        class MplsInSegmentLdpLspEntry(Entity):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index for the mplsInSegmentTable
            (mplsInSegmentLdpLspLabelIndex) from the
            MPLS\-LSR\-STD\-MIB.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsinsegmentldplspindex  (key)
            
            	This contains the same value as the mplsInSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsInSegmentTable
            	**type**\: str
            
            	**length:** 1..24
            
            	**config**\: False
            
            .. attribute:: mplsinsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\:  :py:class:`MplsLdpLabelType <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLdpLabelType>`
            
            	**config**\: False
            
            .. attribute:: mplsinsegmentldplsptype
            
            	The type of LSP connection
            	**type**\:  :py:class:`MplsLspType <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLspType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry, self).__init__()

                self.yang_name = "mplsInSegmentLdpLspEntry"
                self.yang_parent_name = "mplsInSegmentLdpLspTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid','mplsinsegmentldplspindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsinsegmentldplspindex', (YLeaf(YType.str, 'mplsInSegmentLdpLspIndex'), ['str'])),
                    ('mplsinsegmentldplsplabeltype', (YLeaf(YType.enumeration, 'mplsInSegmentLdpLspLabelType'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLdpLabelType', '')])),
                    ('mplsinsegmentldplsptype', (YLeaf(YType.enumeration, 'mplsInSegmentLdpLspType'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLspType', '')])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsinsegmentldplspindex = None
                self.mplsinsegmentldplsplabeltype = None
                self.mplsinsegmentldplsptype = None
                self._segment_path = lambda: "mplsInSegmentLdpLspEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']" + "[mplsInSegmentLdpLspIndex='" + str(self.mplsinsegmentldplspindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsInSegmentLdpLspTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsInSegmentLdpLspTable.MplsInSegmentLdpLspEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsinsegmentldplspindex', 'mplsinsegmentldplsplabeltype', 'mplsinsegmentldplsptype'], name, value)




    class MplsOutSegmentLdpLspTable(Entity):
        """
        A table of LDP LSP's which
        map to the mplsOutSegmentTable in the
        MPLS\-LSR\-STD\-MIB.
        
        .. attribute:: mplsoutsegmentldplspentry
        
        	An entry in this table represents information on a single LDP LSP which is represented by a session's index triple (mplsLdpEntityLdpId, mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the index (mplsOutSegmentLdpLspIndex) for the mplsOutSegmentTable.  The information contained in a row is read\-only
        	**type**\: list of  		 :py:class:`MplsOutSegmentLdpLspEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable, self).__init__()

            self.yang_name = "mplsOutSegmentLdpLspTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsOutSegmentLdpLspEntry", ("mplsoutsegmentldplspentry", MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry))])
            self._leafs = OrderedDict()

            self.mplsoutsegmentldplspentry = YList(self)
            self._segment_path = lambda: "mplsOutSegmentLdpLspTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable, [], name, value)


        class MplsOutSegmentLdpLspEntry(Entity):
            """
            An entry in this table represents information
            on a single LDP LSP which is represented by
            a session's index triple (mplsLdpEntityLdpId,
            mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
            index (mplsOutSegmentLdpLspIndex)
            for the mplsOutSegmentTable.
            
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsoutsegmentldplspindex  (key)
            
            	This contains the same value as the mplsOutSegmentIndex in the MPLS\-LSR\-STD\-MIB's mplsOutSegmentTable
            	**type**\: str
            
            	**length:** 1..24
            
            	**config**\: False
            
            .. attribute:: mplsoutsegmentldplsplabeltype
            
            	The Layer 2 Label Type
            	**type**\:  :py:class:`MplsLdpLabelType <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLdpLabelType>`
            
            	**config**\: False
            
            .. attribute:: mplsoutsegmentldplsptype
            
            	The type of LSP connection
            	**type**\:  :py:class:`MplsLspType <ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB.MplsLspType>`
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry, self).__init__()

                self.yang_name = "mplsOutSegmentLdpLspEntry"
                self.yang_parent_name = "mplsOutSegmentLdpLspTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid','mplsoutsegmentldplspindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsoutsegmentldplspindex', (YLeaf(YType.str, 'mplsOutSegmentLdpLspIndex'), ['str'])),
                    ('mplsoutsegmentldplsplabeltype', (YLeaf(YType.enumeration, 'mplsOutSegmentLdpLspLabelType'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLdpLabelType', '')])),
                    ('mplsoutsegmentldplsptype', (YLeaf(YType.enumeration, 'mplsOutSegmentLdpLspType'), [('ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsLspType', '')])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsoutsegmentldplspindex = None
                self.mplsoutsegmentldplsplabeltype = None
                self.mplsoutsegmentldplsptype = None
                self._segment_path = lambda: "mplsOutSegmentLdpLspEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']" + "[mplsOutSegmentLdpLspIndex='" + str(self.mplsoutsegmentldplspindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsOutSegmentLdpLspTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsOutSegmentLdpLspTable.MplsOutSegmentLdpLspEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsoutsegmentldplspindex', 'mplsoutsegmentldplsplabeltype', 'mplsoutsegmentldplsptype'], name, value)




    class MplsFecTable(Entity):
        """
        This table represents the FEC
        (Forwarding Equivalence Class)
        Information associated with an LSP.
        
        .. attribute:: mplsfecentry
        
        	Each row represents a single FEC Element
        	**type**\: list of  		 :py:class:`MplsFecEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsFecTable, self).__init__()

            self.yang_name = "mplsFecTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsFecEntry", ("mplsfecentry", MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry))])
            self._leafs = OrderedDict()

            self.mplsfecentry = YList(self)
            self._segment_path = lambda: "mplsFecTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsFecTable, [], name, value)


        class MplsFecEntry(Entity):
            """
            Each row represents a single FEC Element.
            
            .. attribute:: mplsfecindex  (key)
            
            	The index which uniquely identifies this entry
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsfectype
            
            	The type of the FEC.  If the value of this object is 'prefix(1)' then the FEC type described by this row is an address prefix.  If the value of this object is 'hostAddress(2)' then the FEC type described by this row is a host address
            	**type**\:  :py:class:`MplsFecType <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry.MplsFecType>`
            
            	**config**\: False
            
            .. attribute:: mplsfecaddrprefixlength
            
            	If the value of the 'mplsFecType' is 'hostAddress(2)' then this object is undefined.  If the value of 'mplsFecType' is 'prefix(1)' then the value of this object is the length in bits of the address prefix represented by 'mplsFecAddr', or zero.  If the value of this object is zero, this indicates that the prefix matches all addresses.  In this case the address prefix MUST also be zero (i.e., 'mplsFecAddr' should have the value of zero.)
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: mplsfecaddrtype
            
            	The value of this object is the type of the Internet address.  The value of this object, decides how the value of the mplsFecAddr object is interpreted
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: mplsfecaddr
            
            	The value of this object is interpreted based on the value of the 'mplsFecAddrType' object.  This address is then further interpretted as an being used with the address prefix, or as the host address.  This further interpretation is indicated by the 'mplsFecType' object. In other words, the FEC element is populated according to the Prefix FEC Element value encoding, or the Host Address FEC Element encoding
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: mplsfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: mplsfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified, except to set this object to 'destroy(6)'.  NOTE\: if this row is being referenced by any entry in the mplsLdpLspFecTable, then a request to destroy this row, will result in an inconsistentValue error
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry, self).__init__()

                self.yang_name = "mplsFecEntry"
                self.yang_parent_name = "mplsFecTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsfecindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsfecindex', (YLeaf(YType.uint32, 'mplsFecIndex'), ['int'])),
                    ('mplsfectype', (YLeaf(YType.enumeration, 'mplsFecType'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsFecTable.MplsFecEntry.MplsFecType')])),
                    ('mplsfecaddrprefixlength', (YLeaf(YType.uint32, 'mplsFecAddrPrefixLength'), ['int'])),
                    ('mplsfecaddrtype', (YLeaf(YType.enumeration, 'mplsFecAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('mplsfecaddr', (YLeaf(YType.str, 'mplsFecAddr'), ['str'])),
                    ('mplsfecstoragetype', (YLeaf(YType.enumeration, 'mplsFecStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsfecrowstatus', (YLeaf(YType.enumeration, 'mplsFecRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.mplsfecindex = None
                self.mplsfectype = None
                self.mplsfecaddrprefixlength = None
                self.mplsfecaddrtype = None
                self.mplsfecaddr = None
                self.mplsfecstoragetype = None
                self.mplsfecrowstatus = None
                self._segment_path = lambda: "mplsFecEntry" + "[mplsFecIndex='" + str(self.mplsfecindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsFecTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsFecTable.MplsFecEntry, ['mplsfecindex', 'mplsfectype', 'mplsfecaddrprefixlength', 'mplsfecaddrtype', 'mplsfecaddr', 'mplsfecstoragetype', 'mplsfecrowstatus'], name, value)

            class MplsFecType(Enum):
                """
                MplsFecType (Enum Class)

                The type of the FEC.  If the value of this object

                is 'prefix(1)' then the FEC type described by this

                row is an address prefix.

                If the value of this object is 'hostAddress(2)' then

                the FEC type described by this row is a host address.

                .. data:: prefix = 1

                .. data:: hostAddress = 2

                """

                prefix = Enum.YLeaf(1, "prefix")

                hostAddress = Enum.YLeaf(2, "hostAddress")





    class MplsLdpLspFecTable(Entity):
        """
        A table which shows the relationship between
        LDP LSPs and FECs.  Each row represents
        a single LDP LSP to FEC association.
        
        .. attribute:: mplsldplspfecentry
        
        	An entry represents a LDP LSP to FEC association
        	**type**\: list of  		 :py:class:`MplsLdpLspFecEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpLspFecTable, self).__init__()

            self.yang_name = "mplsLdpLspFecTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLdpLspFecEntry", ("mplsldplspfecentry", MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry))])
            self._leafs = OrderedDict()

            self.mplsldplspfecentry = YList(self)
            self._segment_path = lambda: "mplsLdpLspFecTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpLspFecTable, [], name, value)


        class MplsLdpLspFecEntry(Entity):
            """
            An entry represents a LDP LSP
            to FEC association.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldplspfecsegment  (key)
            
            	If the value is inSegment(1), then this indicates that the following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsInSegmentLdpLspIndex.  Otherwise, if the value of this object is   outSegment(2),  then this indicates that following index, mplsLdpLspFecSegmentIndex, contains the same value as the mplsOutSegmentLdpLspIndex
            	**type**\:  :py:class:`MplsLdpLspFecSegment <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry.MplsLdpLspFecSegment>`
            
            	**config**\: False
            
            .. attribute:: mplsldplspfecsegmentindex  (key)
            
            	This index is interpretted by using the value of the mplsLdpLspFecSegment.  If the mplsLdpLspFecSegment is inSegment(1), then this index has the same value as mplsInSegmentLdpLspIndex.  If the mplsLdpLspFecSegment is outSegment(2), then this index has the same value as mplsOutSegmentLdpLspIndex
            	**type**\: str
            
            	**length:** 1..24
            
            	**config**\: False
            
            .. attribute:: mplsldplspfecindex  (key)
            
            	This index identifies the FEC entry in the mplsFecTable associated with this session. In other words, the value of this index is the same as the value of the mplsFecIndex that denotes the FEC associated with this Session
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldplspfecstoragetype
            
            	The storage type for this conceptual row. Conceptual rows having the value 'permanent(4)' need not allow write\-access to any columnar objects in the row
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: mplsldplspfecrowstatus
            
            	The status of this conceptual row.  If the value of this object is 'active(1)', then none of the writable objects of this entry can be modified.  The Agent should delete this row when the session ceases to exist.  If an operator wants to associate the session with a different FEC, the recommended procedure is (as described in detail in the section entitled, 'Changing Values After Session Establishment', and again described in the DESCRIPTION clause of the mplsLdpEntityAdminStatus object) is to set the mplsLdpEntityAdminStatus to down, thereby explicitly causing a session to be torn down. This will also cause this entry to be deleted.  Then, set the mplsLdpEntityAdminStatus to enable which enables a new session to be initiated. Once the session is initiated, an entry may be added to this table to associate the new session with a FEC
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry, self).__init__()

                self.yang_name = "mplsLdpLspFecEntry"
                self.yang_parent_name = "mplsLdpLspFecTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid','mplsldplspfecsegment','mplsldplspfecsegmentindex','mplsldplspfecindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsldplspfecsegment', (YLeaf(YType.enumeration, 'mplsLdpLspFecSegment'), [('ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MPLSLDPSTDMIB', 'MplsLdpLspFecTable.MplsLdpLspFecEntry.MplsLdpLspFecSegment')])),
                    ('mplsldplspfecsegmentindex', (YLeaf(YType.str, 'mplsLdpLspFecSegmentIndex'), ['str'])),
                    ('mplsldplspfecindex', (YLeaf(YType.uint32, 'mplsLdpLspFecIndex'), ['int'])),
                    ('mplsldplspfecstoragetype', (YLeaf(YType.enumeration, 'mplsLdpLspFecStorageType'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('mplsldplspfecrowstatus', (YLeaf(YType.enumeration, 'mplsLdpLspFecRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsldplspfecsegment = None
                self.mplsldplspfecsegmentindex = None
                self.mplsldplspfecindex = None
                self.mplsldplspfecstoragetype = None
                self.mplsldplspfecrowstatus = None
                self._segment_path = lambda: "mplsLdpLspFecEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']" + "[mplsLdpLspFecSegment='" + str(self.mplsldplspfecsegment) + "']" + "[mplsLdpLspFecSegmentIndex='" + str(self.mplsldplspfecsegmentindex) + "']" + "[mplsLdpLspFecIndex='" + str(self.mplsldplspfecindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpLspFecTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsLdpLspFecTable.MplsLdpLspFecEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsldplspfecsegment', 'mplsldplspfecsegmentindex', 'mplsldplspfecindex', 'mplsldplspfecstoragetype', 'mplsldplspfecrowstatus'], name, value)

            class MplsLdpLspFecSegment(Enum):
                """
                MplsLdpLspFecSegment (Enum Class)

                If the value is inSegment(1), then this

                indicates that the following index,

                mplsLdpLspFecSegmentIndex, contains the same

                value as the mplsInSegmentLdpLspIndex.

                Otherwise, if the value of this object is

                outSegment(2),  then this

                indicates that following index,

                mplsLdpLspFecSegmentIndex, contains the same

                value as the mplsOutSegmentLdpLspIndex.

                .. data:: inSegment = 1

                .. data:: outSegment = 2

                """

                inSegment = Enum.YLeaf(1, "inSegment")

                outSegment = Enum.YLeaf(2, "outSegment")





    class MplsLdpSessionPeerAddrTable(Entity):
        """
        This table 'extends' the mplsLdpSessionTable.
        This table is used to store Label Address Information
        from Label Address Messages received by this LSR from
        Peers.  This table is read\-only and should be updated
        
        
        when Label Withdraw Address Messages are received, i.e.,
        Rows should be deleted as appropriate.
        
        NOTE\:  since more than one address may be contained
        in a Label Address Message, this table 'sparse augments',
        the mplsLdpSessionTable's information.
        
        .. attribute:: mplsldpsessionpeeraddrentry
        
        	An entry in this table represents information on a session's single next hop address which was advertised in an Address Message from the LDP peer. The information contained in a row is read\-only
        	**type**\: list of  		 :py:class:`MplsLdpSessionPeerAddrEntry <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'MPLS-LDP-STD-MIB'
        _revision = '2004-06-03'

        def __init__(self):
            super(MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable, self).__init__()

            self.yang_name = "mplsLdpSessionPeerAddrTable"
            self.yang_parent_name = "MPLS-LDP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("mplsLdpSessionPeerAddrEntry", ("mplsldpsessionpeeraddrentry", MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry))])
            self._leafs = OrderedDict()

            self.mplsldpsessionpeeraddrentry = YList(self)
            self._segment_path = lambda: "mplsLdpSessionPeerAddrTable"
            self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable, [], name, value)


        class MplsLdpSessionPeerAddrEntry(Entity):
            """
            An entry in this table represents information on
            a session's single next hop address which was
            advertised in an Address Message from the LDP peer.
            The information contained in a row is read\-only.
            
            .. attribute:: mplsldpentityldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldpentityldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpentityindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`mplsldpentityindex <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpEntityTable.MplsLdpEntityEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldppeerldpid  (key)
            
            	
            	**type**\: str
            
            	**refers to**\:  :py:class:`mplsldppeerldpid <ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB.MPLSLDPSTDMIB.MplsLdpPeerTable.MplsLdpPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionpeeraddrindex  (key)
            
            	An index which uniquely identifies this entry within a given session
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionpeernexthopaddrtype
            
            	The internetwork layer address type of this Next Hop Address as specified in the Label Address Message associated with this Session. The value of this object indicates how to interpret the value of   mplsLdpSessionPeerNextHopAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: mplsldpsessionpeernexthopaddr
            
            	The next hop address.  The type of this address is specified by the value of the mplsLdpSessionPeerNextHopAddrType
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'MPLS-LDP-STD-MIB'
            _revision = '2004-06-03'

            def __init__(self):
                super(MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry, self).__init__()

                self.yang_name = "mplsLdpSessionPeerAddrEntry"
                self.yang_parent_name = "mplsLdpSessionPeerAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['mplsldpentityldpid','mplsldpentityindex','mplsldppeerldpid','mplsldpsessionpeeraddrindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('mplsldpentityldpid', (YLeaf(YType.str, 'mplsLdpEntityLdpId'), ['str'])),
                    ('mplsldpentityindex', (YLeaf(YType.str, 'mplsLdpEntityIndex'), ['int'])),
                    ('mplsldppeerldpid', (YLeaf(YType.str, 'mplsLdpPeerLdpId'), ['str'])),
                    ('mplsldpsessionpeeraddrindex', (YLeaf(YType.uint32, 'mplsLdpSessionPeerAddrIndex'), ['int'])),
                    ('mplsldpsessionpeernexthopaddrtype', (YLeaf(YType.enumeration, 'mplsLdpSessionPeerNextHopAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('mplsldpsessionpeernexthopaddr', (YLeaf(YType.str, 'mplsLdpSessionPeerNextHopAddr'), ['str'])),
                ])
                self.mplsldpentityldpid = None
                self.mplsldpentityindex = None
                self.mplsldppeerldpid = None
                self.mplsldpsessionpeeraddrindex = None
                self.mplsldpsessionpeernexthopaddrtype = None
                self.mplsldpsessionpeernexthopaddr = None
                self._segment_path = lambda: "mplsLdpSessionPeerAddrEntry" + "[mplsLdpEntityLdpId='" + str(self.mplsldpentityldpid) + "']" + "[mplsLdpEntityIndex='" + str(self.mplsldpentityindex) + "']" + "[mplsLdpPeerLdpId='" + str(self.mplsldppeerldpid) + "']" + "[mplsLdpSessionPeerAddrIndex='" + str(self.mplsldpsessionpeeraddrindex) + "']"
                self._absolute_path = lambda: "MPLS-LDP-STD-MIB:MPLS-LDP-STD-MIB/mplsLdpSessionPeerAddrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(MPLSLDPSTDMIB.MplsLdpSessionPeerAddrTable.MplsLdpSessionPeerAddrEntry, ['mplsldpentityldpid', 'mplsldpentityindex', 'mplsldppeerldpid', 'mplsldpsessionpeeraddrindex', 'mplsldpsessionpeernexthopaddrtype', 'mplsldpsessionpeernexthopaddr'], name, value)



    def clone_ptr(self):
        self._top_entity = MPLSLDPSTDMIB()
        return self._top_entity



