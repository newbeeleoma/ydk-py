""" CISCO_PROCESS_MIB 

The MIB module to describe active system processes.
Virtual Machine refers to those OS which can run the 
code or process of a different executional model OS.
Virtual Process assume the executional model 
of a OS which is different from Native OS. Virtual
Processes are also referred as Tasks.
Thread is a sequence of instructions to be executed
within a program. Thread which adhere to POSIX standard
is referred as a POSIX thread.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOPROCESSMIB(Entity):
    """
    
    
    .. attribute:: cpmcpuhistory
    
    	
    	**type**\:  :py:class:`CpmCPUHistory <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistory>`
    
    	**config**\: False
    
    .. attribute:: cpmcputotaltable
    
    	A table of overall CPU statistics
    	**type**\:  :py:class:`CpmCPUTotalTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable>`
    
    	**config**\: False
    
    .. attribute:: cpmcoretable
    
    	A table of per\-Core statistics
    	**type**\:  :py:class:`CpmCoreTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCoreTable>`
    
    	**config**\: False
    
    .. attribute:: cpmprocesstable
    
    	A table of generic information on all active processes on this device
    	**type**\:  :py:class:`CpmProcessTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable>`
    
    	**config**\: False
    
    .. attribute:: cpmprocessextrevtable
    
    	This table contains information that may or may not be available on all cisco devices. It contains additional objects for the more general cpmProcessTable. This object deprecates  cpmProcessExtTable
    	**type**\:  :py:class:`CpmProcessExtRevTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable>`
    
    	**config**\: False
    
    .. attribute:: cpmcputhresholdtable
    
    	This table contains the information about the thresholding values for CPU , configured by the user
    	**type**\:  :py:class:`CpmCPUThresholdTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable>`
    
    	**config**\: False
    
    .. attribute:: cpmcpuhistorytable
    
    	A list of CPU utilization history entries
    	**type**\:  :py:class:`CpmCPUHistoryTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: cpmcpuprocesshistorytable
    
    	A list of process history entries. This table contains CPU utilization of processes which crossed the  cpmCPUHistoryThreshold
    	**type**\:  :py:class:`CpmCPUProcessHistoryTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUProcessHistoryTable>`
    
    	**config**\: False
    
    .. attribute:: cpmthreadtable
    
    	This table contains generic information about POSIX threads in the device
    	**type**\:  :py:class:`CpmThreadTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable>`
    
    	**config**\: False
    
    .. attribute:: cpmvirtualprocesstable
    
    	This table contains information about virtual processes in a virtual machine
    	**type**\:  :py:class:`CpmVirtualProcessTable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmVirtualProcessTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-PROCESS-MIB'
    _revision = '2011-06-23'

    def __init__(self):
        super(CISCOPROCESSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PROCESS-MIB"
        self.yang_parent_name = "CISCO-PROCESS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cpmCPUHistory", ("cpmcpuhistory", CISCOPROCESSMIB.CpmCPUHistory)), ("cpmCPUTotalTable", ("cpmcputotaltable", CISCOPROCESSMIB.CpmCPUTotalTable)), ("cpmCoreTable", ("cpmcoretable", CISCOPROCESSMIB.CpmCoreTable)), ("cpmProcessTable", ("cpmprocesstable", CISCOPROCESSMIB.CpmProcessTable)), ("cpmProcessExtRevTable", ("cpmprocessextrevtable", CISCOPROCESSMIB.CpmProcessExtRevTable)), ("cpmCPUThresholdTable", ("cpmcputhresholdtable", CISCOPROCESSMIB.CpmCPUThresholdTable)), ("cpmCPUHistoryTable", ("cpmcpuhistorytable", CISCOPROCESSMIB.CpmCPUHistoryTable)), ("cpmCPUProcessHistoryTable", ("cpmcpuprocesshistorytable", CISCOPROCESSMIB.CpmCPUProcessHistoryTable)), ("cpmThreadTable", ("cpmthreadtable", CISCOPROCESSMIB.CpmThreadTable)), ("cpmVirtualProcessTable", ("cpmvirtualprocesstable", CISCOPROCESSMIB.CpmVirtualProcessTable))])
        self._leafs = OrderedDict()

        self.cpmcpuhistory = CISCOPROCESSMIB.CpmCPUHistory()
        self.cpmcpuhistory.parent = self
        self._children_name_map["cpmcpuhistory"] = "cpmCPUHistory"

        self.cpmcputotaltable = CISCOPROCESSMIB.CpmCPUTotalTable()
        self.cpmcputotaltable.parent = self
        self._children_name_map["cpmcputotaltable"] = "cpmCPUTotalTable"

        self.cpmcoretable = CISCOPROCESSMIB.CpmCoreTable()
        self.cpmcoretable.parent = self
        self._children_name_map["cpmcoretable"] = "cpmCoreTable"

        self.cpmprocesstable = CISCOPROCESSMIB.CpmProcessTable()
        self.cpmprocesstable.parent = self
        self._children_name_map["cpmprocesstable"] = "cpmProcessTable"

        self.cpmprocessextrevtable = CISCOPROCESSMIB.CpmProcessExtRevTable()
        self.cpmprocessextrevtable.parent = self
        self._children_name_map["cpmprocessextrevtable"] = "cpmProcessExtRevTable"

        self.cpmcputhresholdtable = CISCOPROCESSMIB.CpmCPUThresholdTable()
        self.cpmcputhresholdtable.parent = self
        self._children_name_map["cpmcputhresholdtable"] = "cpmCPUThresholdTable"

        self.cpmcpuhistorytable = CISCOPROCESSMIB.CpmCPUHistoryTable()
        self.cpmcpuhistorytable.parent = self
        self._children_name_map["cpmcpuhistorytable"] = "cpmCPUHistoryTable"

        self.cpmcpuprocesshistorytable = CISCOPROCESSMIB.CpmCPUProcessHistoryTable()
        self.cpmcpuprocesshistorytable.parent = self
        self._children_name_map["cpmcpuprocesshistorytable"] = "cpmCPUProcessHistoryTable"

        self.cpmthreadtable = CISCOPROCESSMIB.CpmThreadTable()
        self.cpmthreadtable.parent = self
        self._children_name_map["cpmthreadtable"] = "cpmThreadTable"

        self.cpmvirtualprocesstable = CISCOPROCESSMIB.CpmVirtualProcessTable()
        self.cpmvirtualprocesstable.parent = self
        self._children_name_map["cpmvirtualprocesstable"] = "cpmVirtualProcessTable"
        self._segment_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOPROCESSMIB, [], name, value)


    class CpmCPUHistory(Entity):
        """
        
        
        .. attribute:: cpmcpuhistorythreshold
        
        	The user  configured value of this object gives the minimum percent CPU utilization of a process in the last cpmCPUMonInterval duration required to be a  member of history table. When this object is changed the new value will have effect in the next interval
        	**type**\: int
        
        	**range:** 1..100
        
        	**config**\: False
        
        .. attribute:: cpmcpuhistorysize
        
        	A value configured by the user which specifies the number of reports in the history table.  A report contains set of processes which crossed the cpmCPUHistoryThreshold  in the last cpmCPUMonInterval along with  the time at which this report is created, total and interrupt CPU utilizations.  When this object is changed the new value will have effect in the next interval
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCPUHistory, self).__init__()

            self.yang_name = "cpmCPUHistory"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cpmcpuhistorythreshold', (YLeaf(YType.uint32, 'cpmCPUHistoryThreshold'), ['int'])),
                ('cpmcpuhistorysize', (YLeaf(YType.uint32, 'cpmCPUHistorySize'), ['int'])),
            ])
            self.cpmcpuhistorythreshold = None
            self.cpmcpuhistorysize = None
            self._segment_path = lambda: "cpmCPUHistory"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCPUHistory, ['cpmcpuhistorythreshold', 'cpmcpuhistorysize'], name, value)



    class CpmCPUTotalTable(Entity):
        """
        A table of overall CPU statistics.
        
        .. attribute:: cpmcputotalentry
        
        	Overall information about the CPU load. Entries in this table come and go as CPUs are added and removed from the system
        	**type**\: list of  		 :py:class:`CpmCPUTotalEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCPUTotalTable, self).__init__()

            self.yang_name = "cpmCPUTotalTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmCPUTotalEntry", ("cpmcputotalentry", CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry))])
            self._leafs = OrderedDict()

            self.cpmcputotalentry = YList(self)
            self._segment_path = lambda: "cpmCPUTotalTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCPUTotalTable, [], name, value)


        class CpmCPUTotalEntry(Entity):
            """
            Overall information about the CPU load. Entries in this
            table come and go as CPUs are added and removed from the
            system.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	An index that uniquely represents a CPU (or group of CPUs) whose CPU load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcputotalphysicalindex
            
            	The entPhysicalIndex of the physical entity for which the CPU statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the CPU statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpmcputotal5sec
            
            	The overall CPU busy percentage in the last 5 second period. This object obsoletes the busyPer object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5secRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal1min
            
            	The overall CPU busy percentage in the last 1 minute period. This object obsoletes the avgBusy1 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal1minRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal5min
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the avgBusy5 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5minRev which has the changed range  of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal5secrev
            
            	The overall CPU busy percentage in the last 5 second period. This object deprecates the object cpmCPUTotal5sec  and increases the value range to (0..100). This object is deprecated by cpmCPUTotalMonIntervalValue
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal1minrev
            
            	The overall CPU busy percentage in the last 1 minute period. This object deprecates the object cpmCPUTotal1min  and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcputotal5minrev
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the object cpmCPUTotal5min  and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcpumoninterval
            
            	CPU usage monitoring interval. The value of this object in seconds indicates the how often the  CPU utilization is calculated and monitored
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cpmcputotalmonintervalvalue
            
            	The overall CPU busy percentage in the last cpmCPUMonInterval period.  This object deprecates the object cpmCPUTotal5secRev
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcpuinterruptmonintervalvalue
            
            	The overall CPU busy percentage in the interrupt context in the last cpmCPUMonInterval period
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcpumemoryused
            
            	The overall CPU wide system memory which is currently under use
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryfree
            
            	The overall CPU wide system memory which is currently free
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorykernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorylowest
            
            	The lowest free memory that has been recorded since device has booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmcpumemoryusedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryUsed. This object needs to be supported only when the value of cpmCPUMemoryUsed exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhcused
            
            	The overall CPU wide system memory which is currently under use. This object is a 64\-bit version of cpmCPUMemoryUsed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryfreeovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryFree. This object needs to be supported only when the value of cpmCPUMemoryFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhcfree
            
            	The overall CPU wide system memory which is currently free. This object is a 64\-bit version of cpmCPUMemoryFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorykernelreservedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryKernelReserved. This object needs  to be supported only when the value of  cpmCPUMemoryKernelReserved exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhckernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage. This object is a 64\-bit version of cpmCPUMemoryKernelReserved
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorylowestovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryLowest. This object needs to be supported only when the value of cpmCPUMemoryLowest exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhclowest
            
            	The lowest free memory that has been recorded since device has booted. This object is a 64\-bit version of cpmCPUMemoryLowest
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpuloadavg1min
            
            	The overall CPU load Average in the last 1 minute period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpuloadavg5min
            
            	The overall CPU load Average in the last 5 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpuloadavg15min
            
            	The overall CPU load Average in the last 15 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpumemorycommitted
            
            	The overall CPU wide system memory which is currently Committed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpumemorycommittedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryCommitted. This object needs to be supported only when the value of cpmCPUMemoryCommitted exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpumemoryhccommitted
            
            	The overall CPU wide system memory which is currently committed. This object is a 64\-bit version of cpmCPUMemoryCommitted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry, self).__init__()

                self.yang_name = "cpmCPUTotalEntry"
                self.yang_parent_name = "cpmCPUTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.uint32, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmcputotalphysicalindex', (YLeaf(YType.int32, 'cpmCPUTotalPhysicalIndex'), ['int'])),
                    ('cpmcputotal5sec', (YLeaf(YType.uint32, 'cpmCPUTotal5sec'), ['int'])),
                    ('cpmcputotal1min', (YLeaf(YType.uint32, 'cpmCPUTotal1min'), ['int'])),
                    ('cpmcputotal5min', (YLeaf(YType.uint32, 'cpmCPUTotal5min'), ['int'])),
                    ('cpmcputotal5secrev', (YLeaf(YType.uint32, 'cpmCPUTotal5secRev'), ['int'])),
                    ('cpmcputotal1minrev', (YLeaf(YType.uint32, 'cpmCPUTotal1minRev'), ['int'])),
                    ('cpmcputotal5minrev', (YLeaf(YType.uint32, 'cpmCPUTotal5minRev'), ['int'])),
                    ('cpmcpumoninterval', (YLeaf(YType.uint32, 'cpmCPUMonInterval'), ['int'])),
                    ('cpmcputotalmonintervalvalue', (YLeaf(YType.uint32, 'cpmCPUTotalMonIntervalValue'), ['int'])),
                    ('cpmcpuinterruptmonintervalvalue', (YLeaf(YType.uint32, 'cpmCPUInterruptMonIntervalValue'), ['int'])),
                    ('cpmcpumemoryused', (YLeaf(YType.uint32, 'cpmCPUMemoryUsed'), ['int'])),
                    ('cpmcpumemoryfree', (YLeaf(YType.uint32, 'cpmCPUMemoryFree'), ['int'])),
                    ('cpmcpumemorykernelreserved', (YLeaf(YType.uint32, 'cpmCPUMemoryKernelReserved'), ['int'])),
                    ('cpmcpumemorylowest', (YLeaf(YType.uint32, 'cpmCPUMemoryLowest'), ['int'])),
                    ('cpmcpumemoryusedovrflw', (YLeaf(YType.uint32, 'cpmCPUMemoryUsedOvrflw'), ['int'])),
                    ('cpmcpumemoryhcused', (YLeaf(YType.uint64, 'cpmCPUMemoryHCUsed'), ['int'])),
                    ('cpmcpumemoryfreeovrflw', (YLeaf(YType.uint32, 'cpmCPUMemoryFreeOvrflw'), ['int'])),
                    ('cpmcpumemoryhcfree', (YLeaf(YType.uint64, 'cpmCPUMemoryHCFree'), ['int'])),
                    ('cpmcpumemorykernelreservedovrflw', (YLeaf(YType.uint32, 'cpmCPUMemoryKernelReservedOvrflw'), ['int'])),
                    ('cpmcpumemoryhckernelreserved', (YLeaf(YType.uint64, 'cpmCPUMemoryHCKernelReserved'), ['int'])),
                    ('cpmcpumemorylowestovrflw', (YLeaf(YType.uint32, 'cpmCPUMemoryLowestOvrflw'), ['int'])),
                    ('cpmcpumemoryhclowest', (YLeaf(YType.uint64, 'cpmCPUMemoryHCLowest'), ['int'])),
                    ('cpmcpuloadavg1min', (YLeaf(YType.uint32, 'cpmCPULoadAvg1min'), ['int'])),
                    ('cpmcpuloadavg5min', (YLeaf(YType.uint32, 'cpmCPULoadAvg5min'), ['int'])),
                    ('cpmcpuloadavg15min', (YLeaf(YType.uint32, 'cpmCPULoadAvg15min'), ['int'])),
                    ('cpmcpumemorycommitted', (YLeaf(YType.uint32, 'cpmCPUMemoryCommitted'), ['int'])),
                    ('cpmcpumemorycommittedovrflw', (YLeaf(YType.uint32, 'cpmCPUMemoryCommittedOvrflw'), ['int'])),
                    ('cpmcpumemoryhccommitted', (YLeaf(YType.uint64, 'cpmCPUMemoryHCCommitted'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmcputotalphysicalindex = None
                self.cpmcputotal5sec = None
                self.cpmcputotal1min = None
                self.cpmcputotal5min = None
                self.cpmcputotal5secrev = None
                self.cpmcputotal1minrev = None
                self.cpmcputotal5minrev = None
                self.cpmcpumoninterval = None
                self.cpmcputotalmonintervalvalue = None
                self.cpmcpuinterruptmonintervalvalue = None
                self.cpmcpumemoryused = None
                self.cpmcpumemoryfree = None
                self.cpmcpumemorykernelreserved = None
                self.cpmcpumemorylowest = None
                self.cpmcpumemoryusedovrflw = None
                self.cpmcpumemoryhcused = None
                self.cpmcpumemoryfreeovrflw = None
                self.cpmcpumemoryhcfree = None
                self.cpmcpumemorykernelreservedovrflw = None
                self.cpmcpumemoryhckernelreserved = None
                self.cpmcpumemorylowestovrflw = None
                self.cpmcpumemoryhclowest = None
                self.cpmcpuloadavg1min = None
                self.cpmcpuloadavg5min = None
                self.cpmcpuloadavg15min = None
                self.cpmcpumemorycommitted = None
                self.cpmcpumemorycommittedovrflw = None
                self.cpmcpumemoryhccommitted = None
                self._segment_path = lambda: "cpmCPUTotalEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUTotalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry, ['cpmcputotalindex', 'cpmcputotalphysicalindex', 'cpmcputotal5sec', 'cpmcputotal1min', 'cpmcputotal5min', 'cpmcputotal5secrev', 'cpmcputotal1minrev', 'cpmcputotal5minrev', 'cpmcpumoninterval', 'cpmcputotalmonintervalvalue', 'cpmcpuinterruptmonintervalvalue', 'cpmcpumemoryused', 'cpmcpumemoryfree', 'cpmcpumemorykernelreserved', 'cpmcpumemorylowest', 'cpmcpumemoryusedovrflw', 'cpmcpumemoryhcused', 'cpmcpumemoryfreeovrflw', 'cpmcpumemoryhcfree', 'cpmcpumemorykernelreservedovrflw', 'cpmcpumemoryhckernelreserved', 'cpmcpumemorylowestovrflw', 'cpmcpumemoryhclowest', 'cpmcpuloadavg1min', 'cpmcpuloadavg5min', 'cpmcpuloadavg15min', 'cpmcpumemorycommitted', 'cpmcpumemorycommittedovrflw', 'cpmcpumemoryhccommitted'], name, value)




    class CpmCoreTable(Entity):
        """
        A table of per\-Core statistics.
        
        .. attribute:: cpmcoreentry
        
        	Overall information about the Core load. Entries in this table could come and go as Cores go online or offline
        	**type**\: list of  		 :py:class:`CpmCoreEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCoreTable.CpmCoreEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCoreTable, self).__init__()

            self.yang_name = "cpmCoreTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmCoreEntry", ("cpmcoreentry", CISCOPROCESSMIB.CpmCoreTable.CpmCoreEntry))])
            self._leafs = OrderedDict()

            self.cpmcoreentry = YList(self)
            self._segment_path = lambda: "cpmCoreTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCoreTable, [], name, value)


        class CpmCoreEntry(Entity):
            """
            Overall information about the Core load. Entries in this
            table could come and go as Cores go online or offline.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmcoreindex  (key)
            
            	An index that uniquely represents a Core (or group of Cores) whose Core load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcorephysicalindex
            
            	The entCorePhysicalIndex of the physical entity for which the Core statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the Core statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cpmcore5sec
            
            	The overall Core busy percentage in the last 5 second period
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: cpmcore1min
            
            	The overall Core busy percentage in the last 1 minute period
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: cpmcore5min
            
            	The overall Core busy percentage in the last 5 minute period
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: cpmcoreloadavg1min
            
            	The overall Core load Average in the last 1 minute period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcoreloadavg5min
            
            	The overall Core load Average in the last 5 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcoreloadavg15min
            
            	The overall Core load Average in the last 15 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: hundredths of processes
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmCoreTable.CpmCoreEntry, self).__init__()

                self.yang_name = "cpmCoreEntry"
                self.yang_parent_name = "cpmCoreTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmcoreindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmcoreindex', (YLeaf(YType.uint32, 'cpmCoreIndex'), ['int'])),
                    ('cpmcorephysicalindex', (YLeaf(YType.int32, 'cpmCorePhysicalIndex'), ['int'])),
                    ('cpmcore5sec', (YLeaf(YType.uint32, 'cpmCore5sec'), ['int'])),
                    ('cpmcore1min', (YLeaf(YType.uint32, 'cpmCore1min'), ['int'])),
                    ('cpmcore5min', (YLeaf(YType.uint32, 'cpmCore5min'), ['int'])),
                    ('cpmcoreloadavg1min', (YLeaf(YType.uint32, 'cpmCoreLoadAvg1min'), ['int'])),
                    ('cpmcoreloadavg5min', (YLeaf(YType.uint32, 'cpmCoreLoadAvg5min'), ['int'])),
                    ('cpmcoreloadavg15min', (YLeaf(YType.uint32, 'cpmCoreLoadAvg15min'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmcoreindex = None
                self.cpmcorephysicalindex = None
                self.cpmcore5sec = None
                self.cpmcore1min = None
                self.cpmcore5min = None
                self.cpmcoreloadavg1min = None
                self.cpmcoreloadavg5min = None
                self.cpmcoreloadavg15min = None
                self._segment_path = lambda: "cpmCoreEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmCoreIndex='" + str(self.cpmcoreindex) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCoreTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmCoreTable.CpmCoreEntry, ['cpmcputotalindex', 'cpmcoreindex', 'cpmcorephysicalindex', 'cpmcore5sec', 'cpmcore1min', 'cpmcore5min', 'cpmcoreloadavg1min', 'cpmcoreloadavg5min', 'cpmcoreloadavg15min'], name, value)




    class CpmProcessTable(Entity):
        """
        A table of generic information on all active
        processes on this device.
        
        .. attribute:: cpmprocessentry
        
        	Generic information about an active process on this device. Entries in this table come and go as processes are  created and destroyed by the device
        	**type**\: list of  		 :py:class:`CpmProcessEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmProcessTable, self).__init__()

            self.yang_name = "cpmProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmProcessEntry", ("cpmprocessentry", CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry))])
            self._leafs = OrderedDict()

            self.cpmprocessentry = YList(self)
            self._segment_path = lambda: "cpmProcessTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmProcessTable, [], name, value)


        class CpmProcessEntry(Entity):
            """
            Generic information about an active process on this
            device. Entries in this table come and go as processes are 
            created and destroyed by the device.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesspid  (key)
            
            	This object contains the process ID. cpmTimeCreated should be checked against the last time it was polled, and if it has changed the PID has been reused and the entire entry should be polled again
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmprocessname
            
            	The name associated with this process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: cpmprocessusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object is deprecated by cpmProcessAverageUSecs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: microseconds
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocesstimecreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmprocessaverageusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object deprecates the object cpmProcessuSecs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: cpmprocextmemallocated
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreed. This object is deprecated by cpmProcExtMemAllocatedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextmemfreed
            
            	The sum of all memory that this process has returned to the system. This object is deprecated by  cpmProcExtMemFreedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextinvoked
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object is deprecated by cpmProcExtInvokedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextruntime
            
            	The amount of CPU time the process has used, in microseconds. This object is deprecated by cpmProcExtRuntimeRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: microseconds
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil5sec
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil5SecRev which has the  changed range of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil1min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil1MinRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil5min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is deprecated by cpmProcExtUtil5MinRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextpriority
            
            	The priority level at which the process is running. This object is deprecated by cpmProcExtPriorityRev
            	**type**\:  :py:class:`CpmProcExtPriority <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry.CpmProcExtPriority>`
            
            	**config**\: False
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry, self).__init__()

                self.yang_name = "cpmProcessEntry"
                self.yang_parent_name = "cpmProcessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmprocesspid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmprocesspid', (YLeaf(YType.uint32, 'cpmProcessPID'), ['int'])),
                    ('cpmprocessname', (YLeaf(YType.str, 'cpmProcessName'), ['str'])),
                    ('cpmprocessusecs', (YLeaf(YType.uint32, 'cpmProcessuSecs'), ['int'])),
                    ('cpmprocesstimecreated', (YLeaf(YType.uint32, 'cpmProcessTimeCreated'), ['int'])),
                    ('cpmprocessaverageusecs', (YLeaf(YType.uint32, 'cpmProcessAverageUSecs'), ['int'])),
                    ('cpmprocextmemallocated', (YLeaf(YType.uint32, 'cpmProcExtMemAllocated'), ['int'])),
                    ('cpmprocextmemfreed', (YLeaf(YType.uint32, 'cpmProcExtMemFreed'), ['int'])),
                    ('cpmprocextinvoked', (YLeaf(YType.uint32, 'cpmProcExtInvoked'), ['int'])),
                    ('cpmprocextruntime', (YLeaf(YType.uint32, 'cpmProcExtRuntime'), ['int'])),
                    ('cpmprocextutil5sec', (YLeaf(YType.uint32, 'cpmProcExtUtil5Sec'), ['int'])),
                    ('cpmprocextutil1min', (YLeaf(YType.uint32, 'cpmProcExtUtil1Min'), ['int'])),
                    ('cpmprocextutil5min', (YLeaf(YType.uint32, 'cpmProcExtUtil5Min'), ['int'])),
                    ('cpmprocextpriority', (YLeaf(YType.enumeration, 'cpmProcExtPriority'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmProcessTable.CpmProcessEntry.CpmProcExtPriority')])),
                ])
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmprocessname = None
                self.cpmprocessusecs = None
                self.cpmprocesstimecreated = None
                self.cpmprocessaverageusecs = None
                self.cpmprocextmemallocated = None
                self.cpmprocextmemfreed = None
                self.cpmprocextinvoked = None
                self.cpmprocextruntime = None
                self.cpmprocextutil5sec = None
                self.cpmprocextutil1min = None
                self.cpmprocextutil5min = None
                self.cpmprocextpriority = None
                self._segment_path = lambda: "cpmProcessEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmProcessPID='" + str(self.cpmprocesspid) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmprocessname', 'cpmprocessusecs', 'cpmprocesstimecreated', 'cpmprocessaverageusecs', 'cpmprocextmemallocated', 'cpmprocextmemfreed', 'cpmprocextinvoked', 'cpmprocextruntime', 'cpmprocextutil5sec', 'cpmprocextutil1min', 'cpmprocextutil5min', 'cpmprocextpriority'], name, value)

            class CpmProcExtPriority(Enum):
                """
                CpmProcExtPriority (Enum Class)

                The priority level at which the process is

                running. This object is deprecated by

                cpmProcExtPriorityRev.

                .. data:: critical = 1

                .. data:: high = 2

                .. data:: normal = 3

                .. data:: low = 4

                .. data:: notAssigned = 5

                """

                critical = Enum.YLeaf(1, "critical")

                high = Enum.YLeaf(2, "high")

                normal = Enum.YLeaf(3, "normal")

                low = Enum.YLeaf(4, "low")

                notAssigned = Enum.YLeaf(5, "notAssigned")





    class CpmProcessExtRevTable(Entity):
        """
        This table contains information that may or may
        not be available on all cisco devices. It contains
        additional objects for the more general
        cpmProcessTable. This object deprecates 
        cpmProcessExtTable.
        
        .. attribute:: cpmprocessextreventry
        
        	An entry containing additional information for a particular process. This object deprecates  cpmProcessExtEntry
        	**type**\: list of  		 :py:class:`CpmProcessExtRevEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmProcessExtRevTable, self).__init__()

            self.yang_name = "cpmProcessExtRevTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmProcessExtRevEntry", ("cpmprocessextreventry", CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry))])
            self._leafs = OrderedDict()

            self.cpmprocessextreventry = YList(self)
            self._segment_path = lambda: "cpmProcessExtRevTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmProcessExtRevTable, [], name, value)


        class CpmProcessExtRevEntry(Entity):
            """
            An entry containing additional information for
            a particular process. This object deprecates 
            cpmProcessExtEntry.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesspid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmprocextmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreedRev. This object deprecates cpmProcExtMemAllocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object  deprecates  cpmProcExtMemFreed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextinvokedrev
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object  deprecates cpmProcExtInvoked
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmprocextruntimerev
            
            	The amount of CPU time the process has used, in microseconds. This object deprecates cpmProcExtRuntime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: cpmprocextutil5secrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Sec and increases the  value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmprocextutil1minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object  deprecates cpmProcExtUtil1Min and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmprocextutil5minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Min and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmprocextpriorityrev
            
            	The priority level at  which the process is running. This object deprecates  cpmProcExtPriority
            	**type**\:  :py:class:`CpmProcExtPriorityRev <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesstype
            
            	This indicates the kind of process in context
            	**type**\:  :py:class:`CpmProcessType <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType>`
            
            	**config**\: False
            
            .. attribute:: cpmprocessrespawn
            
            	This indicates whether respawn of a process is enabled or not. If enabled the process in context repawns after it has crashed/stopped
            	**type**\: int
            
            	**range:** 0..2
            
            	**config**\: False
            
            .. attribute:: cpmprocessrespawncount
            
            	This indicates the number of times the process has respawned/restarted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmprocessrespawnafterlastpatch
            
            	This indicates the number of times a process has restarted after the last patch is applied. This is to  determine the stability of the last patch
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmprocessmemorycore
            
            	This indicates the part of process memory to be dumped when a process crashes. The process  memory is used for debugging purposes to trace the  root cause of the crash. sparse        \- Some operating systems support minimal                 dump of process core like register                 info, partial stack, partial memory                 pages especially for critical process                 to facilitate faster process restart
            	**type**\:  :py:class:`CpmProcessMemoryCore <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesslastrestartuser
            
            	This indicate the user that has last restarted the process or has taken running coredump of the process
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cpmprocesstextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessstacksize
            
            	This indicates the amount of stack memory used by the process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocextmemallocatedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemAllocatedRev. This object needs to be supported only when the value of  cpmProcExtMemAllocatedRev exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocexthcmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. This object is a 64\-bit version of cpmProcExtMemAllocatedRev
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextmemfreedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemFreedRev. This object needs to  be supported only when the value of cpmProcExtMemFreedRev exceeds 32\-bit,otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocexthcmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object is a 64\-bit version of cpmProcExtMemFreedRev
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmprocesstextsegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessTextSegmentSize. This object needs to be supported only when the value of  cpmProcessTextSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshctextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects. This object is a 64\-bit version of cpmProcessTextSegmentSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdatasegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDataSegmentSize. This object needs to be supported only when the value of  cpmProcessDataSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects.. This object is a 64\-bit version of cpmProcessDataSegmentSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessStackSize. This object needs to be supported only when the value of cpmProcessStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcstacksize
            
            	This indicates the amount of stack memory used by the process. This object is a 64\-bit version of cpmProcessStackSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdynamicmemorysizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDynamicMemorySize. This object needs to be supported only when the value of  cpmProcessDynamicMemorySize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process. This object is a 64\-bit version of cpmProcessDynamicMemorySize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: kilo-bytes
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry, self).__init__()

                self.yang_name = "cpmProcessExtRevEntry"
                self.yang_parent_name = "cpmProcessExtRevTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmprocesspid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmprocesspid', (YLeaf(YType.str, 'cpmProcessPID'), ['int'])),
                    ('cpmprocextmemallocatedrev', (YLeaf(YType.uint32, 'cpmProcExtMemAllocatedRev'), ['int'])),
                    ('cpmprocextmemfreedrev', (YLeaf(YType.uint32, 'cpmProcExtMemFreedRev'), ['int'])),
                    ('cpmprocextinvokedrev', (YLeaf(YType.uint32, 'cpmProcExtInvokedRev'), ['int'])),
                    ('cpmprocextruntimerev', (YLeaf(YType.uint32, 'cpmProcExtRuntimeRev'), ['int'])),
                    ('cpmprocextutil5secrev', (YLeaf(YType.uint32, 'cpmProcExtUtil5SecRev'), ['int'])),
                    ('cpmprocextutil1minrev', (YLeaf(YType.uint32, 'cpmProcExtUtil1MinRev'), ['int'])),
                    ('cpmprocextutil5minrev', (YLeaf(YType.uint32, 'cpmProcExtUtil5MinRev'), ['int'])),
                    ('cpmprocextpriorityrev', (YLeaf(YType.enumeration, 'cpmProcExtPriorityRev'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev')])),
                    ('cpmprocesstype', (YLeaf(YType.enumeration, 'cpmProcessType'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType')])),
                    ('cpmprocessrespawn', (YLeaf(YType.uint32, 'cpmProcessRespawn'), ['int'])),
                    ('cpmprocessrespawncount', (YLeaf(YType.uint32, 'cpmProcessRespawnCount'), ['int'])),
                    ('cpmprocessrespawnafterlastpatch', (YLeaf(YType.uint32, 'cpmProcessRespawnAfterLastPatch'), ['int'])),
                    ('cpmprocessmemorycore', (YLeaf(YType.enumeration, 'cpmProcessMemoryCore'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore')])),
                    ('cpmprocesslastrestartuser', (YLeaf(YType.str, 'cpmProcessLastRestartUser'), ['str'])),
                    ('cpmprocesstextsegmentsize', (YLeaf(YType.uint32, 'cpmProcessTextSegmentSize'), ['int'])),
                    ('cpmprocessdatasegmentsize', (YLeaf(YType.uint32, 'cpmProcessDataSegmentSize'), ['int'])),
                    ('cpmprocessstacksize', (YLeaf(YType.uint32, 'cpmProcessStackSize'), ['int'])),
                    ('cpmprocessdynamicmemorysize', (YLeaf(YType.uint32, 'cpmProcessDynamicMemorySize'), ['int'])),
                    ('cpmprocextmemallocatedrevovrflw', (YLeaf(YType.uint32, 'cpmProcExtMemAllocatedRevOvrflw'), ['int'])),
                    ('cpmprocexthcmemallocatedrev', (YLeaf(YType.uint64, 'cpmProcExtHCMemAllocatedRev'), ['int'])),
                    ('cpmprocextmemfreedrevovrflw', (YLeaf(YType.uint32, 'cpmProcExtMemFreedRevOvrflw'), ['int'])),
                    ('cpmprocexthcmemfreedrev', (YLeaf(YType.uint64, 'cpmProcExtHCMemFreedRev'), ['int'])),
                    ('cpmprocesstextsegmentsizeovrflw', (YLeaf(YType.uint32, 'cpmProcessTextSegmentSizeOvrflw'), ['int'])),
                    ('cpmprocesshctextsegmentsize', (YLeaf(YType.uint64, 'cpmProcessHCTextSegmentSize'), ['int'])),
                    ('cpmprocessdatasegmentsizeovrflw', (YLeaf(YType.uint32, 'cpmProcessDataSegmentSizeOvrflw'), ['int'])),
                    ('cpmprocesshcdatasegmentsize', (YLeaf(YType.uint64, 'cpmProcessHCDataSegmentSize'), ['int'])),
                    ('cpmprocessstacksizeovrflw', (YLeaf(YType.uint32, 'cpmProcessStackSizeOvrflw'), ['int'])),
                    ('cpmprocesshcstacksize', (YLeaf(YType.uint64, 'cpmProcessHCStackSize'), ['int'])),
                    ('cpmprocessdynamicmemorysizeovrflw', (YLeaf(YType.uint32, 'cpmProcessDynamicMemorySizeOvrflw'), ['int'])),
                    ('cpmprocesshcdynamicmemorysize', (YLeaf(YType.uint64, 'cpmProcessHCDynamicMemorySize'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmprocextmemallocatedrev = None
                self.cpmprocextmemfreedrev = None
                self.cpmprocextinvokedrev = None
                self.cpmprocextruntimerev = None
                self.cpmprocextutil5secrev = None
                self.cpmprocextutil1minrev = None
                self.cpmprocextutil5minrev = None
                self.cpmprocextpriorityrev = None
                self.cpmprocesstype = None
                self.cpmprocessrespawn = None
                self.cpmprocessrespawncount = None
                self.cpmprocessrespawnafterlastpatch = None
                self.cpmprocessmemorycore = None
                self.cpmprocesslastrestartuser = None
                self.cpmprocesstextsegmentsize = None
                self.cpmprocessdatasegmentsize = None
                self.cpmprocessstacksize = None
                self.cpmprocessdynamicmemorysize = None
                self.cpmprocextmemallocatedrevovrflw = None
                self.cpmprocexthcmemallocatedrev = None
                self.cpmprocextmemfreedrevovrflw = None
                self.cpmprocexthcmemfreedrev = None
                self.cpmprocesstextsegmentsizeovrflw = None
                self.cpmprocesshctextsegmentsize = None
                self.cpmprocessdatasegmentsizeovrflw = None
                self.cpmprocesshcdatasegmentsize = None
                self.cpmprocessstacksizeovrflw = None
                self.cpmprocesshcstacksize = None
                self.cpmprocessdynamicmemorysizeovrflw = None
                self.cpmprocesshcdynamicmemorysize = None
                self._segment_path = lambda: "cpmProcessExtRevEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmProcessPID='" + str(self.cpmprocesspid) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessExtRevTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmprocextmemallocatedrev', 'cpmprocextmemfreedrev', 'cpmprocextinvokedrev', 'cpmprocextruntimerev', 'cpmprocextutil5secrev', 'cpmprocextutil1minrev', 'cpmprocextutil5minrev', 'cpmprocextpriorityrev', 'cpmprocesstype', 'cpmprocessrespawn', 'cpmprocessrespawncount', 'cpmprocessrespawnafterlastpatch', 'cpmprocessmemorycore', 'cpmprocesslastrestartuser', 'cpmprocesstextsegmentsize', 'cpmprocessdatasegmentsize', 'cpmprocessstacksize', 'cpmprocessdynamicmemorysize', 'cpmprocextmemallocatedrevovrflw', 'cpmprocexthcmemallocatedrev', 'cpmprocextmemfreedrevovrflw', 'cpmprocexthcmemfreedrev', 'cpmprocesstextsegmentsizeovrflw', 'cpmprocesshctextsegmentsize', 'cpmprocessdatasegmentsizeovrflw', 'cpmprocesshcdatasegmentsize', 'cpmprocessstacksizeovrflw', 'cpmprocesshcstacksize', 'cpmprocessdynamicmemorysizeovrflw', 'cpmprocesshcdynamicmemorysize'], name, value)

            class CpmProcExtPriorityRev(Enum):
                """
                CpmProcExtPriorityRev (Enum Class)

                The priority level at  which the process is

                running. This object deprecates 

                cpmProcExtPriority.

                .. data:: critical = 1

                .. data:: high = 2

                .. data:: normal = 3

                .. data:: low = 4

                .. data:: notAssigned = 5

                """

                critical = Enum.YLeaf(1, "critical")

                high = Enum.YLeaf(2, "high")

                normal = Enum.YLeaf(3, "normal")

                low = Enum.YLeaf(4, "low")

                notAssigned = Enum.YLeaf(5, "notAssigned")


            class CpmProcessMemoryCore(Enum):
                """
                CpmProcessMemoryCore (Enum Class)

                This indicates the part of process memory to be

                dumped when a process crashes. The process 

                memory is used for debugging purposes to trace the 

                root cause of the crash.

                sparse        \- Some operating systems support minimal

                                dump of process core like register

                                info, partial stack, partial memory

                                pages especially for critical process

                                to facilitate faster process restart.

                .. data:: none = 0

                .. data:: other = 1

                .. data:: mainmem = 2

                .. data:: mainmemSharedmem = 3

                .. data:: mainmemText = 4

                .. data:: mainmemTextSharedmem = 5

                .. data:: sharedmem = 6

                .. data:: sparse = 7

                .. data:: off = 8

                """

                none = Enum.YLeaf(0, "none")

                other = Enum.YLeaf(1, "other")

                mainmem = Enum.YLeaf(2, "mainmem")

                mainmemSharedmem = Enum.YLeaf(3, "mainmemSharedmem")

                mainmemText = Enum.YLeaf(4, "mainmemText")

                mainmemTextSharedmem = Enum.YLeaf(5, "mainmemTextSharedmem")

                sharedmem = Enum.YLeaf(6, "sharedmem")

                sparse = Enum.YLeaf(7, "sparse")

                off = Enum.YLeaf(8, "off")


            class CpmProcessType(Enum):
                """
                CpmProcessType (Enum Class)

                This indicates the kind of process in context.

                .. data:: none = 0

                .. data:: other = 1

                .. data:: posix = 2

                .. data:: ios = 3

                """

                none = Enum.YLeaf(0, "none")

                other = Enum.YLeaf(1, "other")

                posix = Enum.YLeaf(2, "posix")

                ios = Enum.YLeaf(3, "ios")





    class CpmCPUThresholdTable(Entity):
        """
        This table contains the information about the
        thresholding values for CPU , configured by the user.
        
        .. attribute:: cpmcputhresholdentry
        
        	An entry containing information about CPU thresholding parameters. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this configuration applies
        	**type**\: list of  		 :py:class:`CpmCPUThresholdEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCPUThresholdTable, self).__init__()

            self.yang_name = "cpmCPUThresholdTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmCPUThresholdEntry", ("cpmcputhresholdentry", CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry))])
            self._leafs = OrderedDict()

            self.cpmcputhresholdentry = YList(self)
            self._segment_path = lambda: "cpmCPUThresholdTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCPUThresholdTable, [], name, value)


        class CpmCPUThresholdEntry(Entity):
            """
            An entry containing information about
            CPU thresholding parameters. cpmCPUTotalIndex
            identifies the CPU (or group of CPUs) for which this
            configuration applies.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmcputhresholdclass  (key)
            
            	Value of this object indicates the type of utilization, which is monitored. The total(1) indicates the total CPU utilization, interrupt(2) indicates the the CPU utilization in interrupt context and process(3) indicates the CPU utilization in the process level execution context
            	**type**\:  :py:class:`CpmCPUThresholdClass <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass>`
            
            	**config**\: False
            
            .. attribute:: cpmcpurisingthresholdvalue
            
            	The percentage rising threshold value configured by the user. The value indicates,  if the percentage CPU utilization is equal to or above this value for cpmCPURisingThresholdPeriod duration  then send a cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: cpmcpurisingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that  the CPU utilization should be above cpmCPURisingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 5..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cpmcpufallingthresholdvalue
            
            	The percentage falling threshold value configured by the user. The value indicates, if the percentage  CPU utilization is equal to or below this value for  cpmCPUFallingThresholdPeriod duration then send a cpmCPUFallingThreshold notification  to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            	**config**\: False
            
            .. attribute:: cpmcpufallingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that CPU utilization should be below cpmCPUFallingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 5..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cpmcputhresholdentrystatus
            
            	The status of this table entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry, self).__init__()

                self.yang_name = "cpmCPUThresholdEntry"
                self.yang_parent_name = "cpmCPUThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmcputhresholdclass']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmcputhresholdclass', (YLeaf(YType.enumeration, 'cpmCPUThresholdClass'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass')])),
                    ('cpmcpurisingthresholdvalue', (YLeaf(YType.uint32, 'cpmCPURisingThresholdValue'), ['int'])),
                    ('cpmcpurisingthresholdperiod', (YLeaf(YType.uint32, 'cpmCPURisingThresholdPeriod'), ['int'])),
                    ('cpmcpufallingthresholdvalue', (YLeaf(YType.uint32, 'cpmCPUFallingThresholdValue'), ['int'])),
                    ('cpmcpufallingthresholdperiod', (YLeaf(YType.uint32, 'cpmCPUFallingThresholdPeriod'), ['int'])),
                    ('cpmcputhresholdentrystatus', (YLeaf(YType.enumeration, 'cpmCPUThresholdEntryStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.cpmcputotalindex = None
                self.cpmcputhresholdclass = None
                self.cpmcpurisingthresholdvalue = None
                self.cpmcpurisingthresholdperiod = None
                self.cpmcpufallingthresholdvalue = None
                self.cpmcpufallingthresholdperiod = None
                self.cpmcputhresholdentrystatus = None
                self._segment_path = lambda: "cpmCPUThresholdEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmCPUThresholdClass='" + str(self.cpmcputhresholdclass) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUThresholdTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry, ['cpmcputotalindex', 'cpmcputhresholdclass', 'cpmcpurisingthresholdvalue', 'cpmcpurisingthresholdperiod', 'cpmcpufallingthresholdvalue', 'cpmcpufallingthresholdperiod', 'cpmcputhresholdentrystatus'], name, value)

            class CpmCPUThresholdClass(Enum):
                """
                CpmCPUThresholdClass (Enum Class)

                Value of this object indicates the type of

                utilization, which is monitored. The total(1) indicates

                the total CPU utilization, interrupt(2) indicates the

                the CPU utilization in interrupt context and process(3)

                indicates the CPU utilization in the process level

                execution context.

                .. data:: total = 1

                .. data:: interrupt = 2

                .. data:: process = 3

                """

                total = Enum.YLeaf(1, "total")

                interrupt = Enum.YLeaf(2, "interrupt")

                process = Enum.YLeaf(3, "process")





    class CpmCPUHistoryTable(Entity):
        """
        A list of CPU utilization history entries.
        
        .. attribute:: cpmcpuhistoryentry
        
        	A historical sample of CPU utilization statistics. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this history is collected.  When the cpmCPUHistorySize is reached the least recent entry is lost
        	**type**\: list of  		 :py:class:`CpmCPUHistoryEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCPUHistoryTable, self).__init__()

            self.yang_name = "cpmCPUHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmCPUHistoryEntry", ("cpmcpuhistoryentry", CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry))])
            self._leafs = OrderedDict()

            self.cpmcpuhistoryentry = YList(self)
            self._segment_path = lambda: "cpmCPUHistoryTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCPUHistoryTable, [], name, value)


        class CpmCPUHistoryEntry(Entity):
            """
            A historical sample of CPU utilization statistics.
            cpmCPUTotalIndex identifies the CPU (or group of CPUs)
            for which this history is collected. 
            When the cpmCPUHistorySize is
            reached the least recent entry is lost.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryreportid  (key)
            
            	All the entries which are created at the same time will have same value for this object. When the configured threshold for being a part of History table is reached then the qualified processes become the part of history table. The entries which became the  part of history table at one instant will have the same value for this object. When this object reaches the max index value then it will wrap around
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryreportsize
            
            	The number of process entries in a report. This object gives information about how many processes  became a part of history table at one instant
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistorytotalutil
            
            	Total percentage of CPU utilization at cpmCPUHistoryCreated
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcpuhistoryinterruptutil
            
            	Percentage of CPU utilization in the interrupt context at cpmCPUHistoryCreated
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmcpuhistorycreatedtime
            
            	Time stamp with respect to sysUpTime indicating the time at which this report is created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry, self).__init__()

                self.yang_name = "cpmCPUHistoryEntry"
                self.yang_parent_name = "cpmCPUHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmcpuhistoryreportid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmcpuhistoryreportid', (YLeaf(YType.uint32, 'cpmCPUHistoryReportId'), ['int'])),
                    ('cpmcpuhistoryreportsize', (YLeaf(YType.uint32, 'cpmCPUHistoryReportSize'), ['int'])),
                    ('cpmcpuhistorytotalutil', (YLeaf(YType.uint32, 'cpmCPUHistoryTotalUtil'), ['int'])),
                    ('cpmcpuhistoryinterruptutil', (YLeaf(YType.uint32, 'cpmCPUHistoryInterruptUtil'), ['int'])),
                    ('cpmcpuhistorycreatedtime', (YLeaf(YType.uint32, 'cpmCPUHistoryCreatedTime'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmcpuhistoryreportid = None
                self.cpmcpuhistoryreportsize = None
                self.cpmcpuhistorytotalutil = None
                self.cpmcpuhistoryinterruptutil = None
                self.cpmcpuhistorycreatedtime = None
                self._segment_path = lambda: "cpmCPUHistoryEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmCPUHistoryReportId='" + str(self.cpmcpuhistoryreportid) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry, ['cpmcputotalindex', 'cpmcpuhistoryreportid', 'cpmcpuhistoryreportsize', 'cpmcpuhistorytotalutil', 'cpmcpuhistoryinterruptutil', 'cpmcpuhistorycreatedtime'], name, value)




    class CpmCPUProcessHistoryTable(Entity):
        """
        A list of process history entries. This table contains
        CPU utilization of processes which crossed the 
        cpmCPUHistoryThreshold.
        
        .. attribute:: cpmcpuprocesshistoryentry
        
        	A historical sample of process utilization statistics. The entries in this table will have corresponding entires in the cpmCPUHistoryTable. The entries in this table get deleted when the entry associated with this entry in the cpmCPUHistoryTable  gets deleted
        	**type**\: list of  		 :py:class:`CpmCPUProcessHistoryEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmCPUProcessHistoryTable, self).__init__()

            self.yang_name = "cpmCPUProcessHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmCPUProcessHistoryEntry", ("cpmcpuprocesshistoryentry", CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry))])
            self._leafs = OrderedDict()

            self.cpmcpuprocesshistoryentry = YList(self)
            self._segment_path = lambda: "cpmCPUProcessHistoryTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmCPUProcessHistoryTable, [], name, value)


        class CpmCPUProcessHistoryEntry(Entity):
            """
            A historical sample of process utilization
            statistics. The entries in this table will have
            corresponding entires in the cpmCPUHistoryTable.
            The entries in this table get deleted when the entry
            associated with this entry in the cpmCPUHistoryTable 
            gets deleted.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryreportid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmcpuhistoryreportid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmcpuprocesshistoryindex  (key)
            
            	An index that uniquely identifies an entry in the cmpCPUProcessHistory table among those in the  same report. This index is between 1 to N,  where N is the cpmCPUHistoryReportSize
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryprocid
            
            	The process Id associated with this entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryprocname
            
            	The process name associated with this entry
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryproccreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmcpuhistoryprocutil
            
            	The percentage CPU utilization of a process at cpmCPUHistoryCreatedTime
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry, self).__init__()

                self.yang_name = "cpmCPUProcessHistoryEntry"
                self.yang_parent_name = "cpmCPUProcessHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmcpuhistoryreportid','cpmcpuprocesshistoryindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmcpuhistoryreportid', (YLeaf(YType.str, 'cpmCPUHistoryReportId'), ['int'])),
                    ('cpmcpuprocesshistoryindex', (YLeaf(YType.uint32, 'cpmCPUProcessHistoryIndex'), ['int'])),
                    ('cpmcpuhistoryprocid', (YLeaf(YType.uint32, 'cpmCPUHistoryProcId'), ['int'])),
                    ('cpmcpuhistoryprocname', (YLeaf(YType.str, 'cpmCPUHistoryProcName'), ['str'])),
                    ('cpmcpuhistoryproccreated', (YLeaf(YType.uint32, 'cpmCPUHistoryProcCreated'), ['int'])),
                    ('cpmcpuhistoryprocutil', (YLeaf(YType.uint32, 'cpmCPUHistoryProcUtil'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmcpuhistoryreportid = None
                self.cpmcpuprocesshistoryindex = None
                self.cpmcpuhistoryprocid = None
                self.cpmcpuhistoryprocname = None
                self.cpmcpuhistoryproccreated = None
                self.cpmcpuhistoryprocutil = None
                self._segment_path = lambda: "cpmCPUProcessHistoryEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmCPUHistoryReportId='" + str(self.cpmcpuhistoryreportid) + "']" + "[cpmCPUProcessHistoryIndex='" + str(self.cpmcpuprocesshistoryindex) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUProcessHistoryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry, ['cpmcputotalindex', 'cpmcpuhistoryreportid', 'cpmcpuprocesshistoryindex', 'cpmcpuhistoryprocid', 'cpmcpuhistoryprocname', 'cpmcpuhistoryproccreated', 'cpmcpuhistoryprocutil'], name, value)




    class CpmThreadTable(Entity):
        """
        This table contains generic information about
        POSIX threads in the device.
        
        .. attribute:: cpmthreadentry
        
        	An entry containing the general statistics of a POSIX thread
        	**type**\: list of  		 :py:class:`CpmThreadEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmThreadTable, self).__init__()

            self.yang_name = "cpmThreadTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmThreadEntry", ("cpmthreadentry", CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry))])
            self._leafs = OrderedDict()

            self.cpmthreadentry = YList(self)
            self._segment_path = lambda: "cpmThreadTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmThreadTable, [], name, value)


        class CpmThreadEntry(Entity):
            """
            An entry containing the general statistics
            of a POSIX thread.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesspid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmthreadid  (key)
            
            	This object contains the thread ID. ThreadID is Unique per process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmthreadname
            
            	This object represents the name of the thread. Thread names need not be unique. Hence statistics  should be analyzed against thread ID
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cpmthreadpriority
            
            	This object indicates the priority of a POSIX thread. The higher the number, the higher the priority of the  thread over other threads
            	**type**\: int
            
            	**range:** 0..63
            
            	**config**\: False
            
            .. attribute:: cpmthreadstate
            
            	This object indicates the current state of a thread. Running state means that the thread is actively  consumig CPU. All the other states are just waiting  states. The valid states are\: other         \- Any other state apart from the listed                  ones. dead          \- Kernel is waiting to release the                  thread's resources. running       \- Actively running on a CPU. ready         \- Not running on a CPU, but is ready to                  run (one or more higher or equal                  priority threads are running). stopped       \- Suspended (SIGSTOP signal). send          \- Waiting for a server to receive                  a message. receive       \- Waiting for a client to send a message. reply         \- Waiting for a server to reply to a                  message. stack         \- Waiting for more stack to be allocated. waitpage      \- Waiting for process manager to                  resolve a fault on a page. sigsuspend    \- Suspended for a signal. sigwaitinfo   \- Waiting for a signal. nanosleep     \- Sleeping for a period of time. mutex         \- Waiting to acquire a mutex condvar       \- Waiting for a condition variable to be                  signalled. join          \- Waiting for the completion of another                  thread. intr          \- Waiting for an interrupt. sem           \- Waiting to acquire a semaphore
            	**type**\:  :py:class:`CpmThreadState <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry.CpmThreadState>`
            
            	**config**\: False
            
            .. attribute:: cpmthreadblockingprocess
            
            	This object identifies the process on which the current thread is blocked on. This points to the  cpmProcessTable of the process on which the thread  in context is blocked. This is valid only to threads which are either in send/reply states. For the  rest of the threads it is returned as 0.0
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cpmthreadcpuutilization
            
            	This object provides a general idea on how busy the thread in context caused the processor to be
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: cpmthreadstacksize
            
            	This object indicates the stack size allocated to the thread in context
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmthreadstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmThreadStackSize. This object needs to be supported only when the value of cpmThreadStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmthreadhcstacksize
            
            	This object indicates the stack size allocated to the thread in context. This object is a 64\-bit version of cpmThreadStackSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry, self).__init__()

                self.yang_name = "cpmThreadEntry"
                self.yang_parent_name = "cpmThreadTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmprocesspid','cpmthreadid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmprocesspid', (YLeaf(YType.str, 'cpmProcessPID'), ['int'])),
                    ('cpmthreadid', (YLeaf(YType.uint32, 'cpmThreadID'), ['int'])),
                    ('cpmthreadname', (YLeaf(YType.str, 'cpmThreadName'), ['str'])),
                    ('cpmthreadpriority', (YLeaf(YType.uint32, 'cpmThreadPriority'), ['int'])),
                    ('cpmthreadstate', (YLeaf(YType.enumeration, 'cpmThreadState'), [('ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB', 'CpmThreadTable.CpmThreadEntry.CpmThreadState')])),
                    ('cpmthreadblockingprocess', (YLeaf(YType.str, 'cpmThreadBlockingProcess'), ['str'])),
                    ('cpmthreadcpuutilization', (YLeaf(YType.uint32, 'cpmThreadCpuUtilization'), ['int'])),
                    ('cpmthreadstacksize', (YLeaf(YType.uint32, 'cpmThreadStackSize'), ['int'])),
                    ('cpmthreadstacksizeovrflw', (YLeaf(YType.uint32, 'cpmThreadStackSizeOvrflw'), ['int'])),
                    ('cpmthreadhcstacksize', (YLeaf(YType.uint64, 'cpmThreadHCStackSize'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmthreadid = None
                self.cpmthreadname = None
                self.cpmthreadpriority = None
                self.cpmthreadstate = None
                self.cpmthreadblockingprocess = None
                self.cpmthreadcpuutilization = None
                self.cpmthreadstacksize = None
                self.cpmthreadstacksizeovrflw = None
                self.cpmthreadhcstacksize = None
                self._segment_path = lambda: "cpmThreadEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmProcessPID='" + str(self.cpmprocesspid) + "']" + "[cpmThreadID='" + str(self.cpmthreadid) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmThreadTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmthreadid', 'cpmthreadname', 'cpmthreadpriority', 'cpmthreadstate', 'cpmthreadblockingprocess', 'cpmthreadcpuutilization', 'cpmthreadstacksize', 'cpmthreadstacksizeovrflw', 'cpmthreadhcstacksize'], name, value)

            class CpmThreadState(Enum):
                """
                CpmThreadState (Enum Class)

                This object indicates the current state of a thread.

                Running state means that the thread is actively 

                consumig CPU. All the other states are just waiting 

                states. The valid states are\:

                other         \- Any other state apart from the listed 

                                ones.

                dead          \- Kernel is waiting to release the 

                                thread's resources.

                running       \- Actively running on a CPU.

                ready         \- Not running on a CPU, but is ready to 

                                run (one or more higher or equal 

                                priority threads are running).

                stopped       \- Suspended (SIGSTOP signal).

                send          \- Waiting for a server to receive 

                                a message.

                receive       \- Waiting for a client to send a message.

                reply         \- Waiting for a server to reply to a 

                                message.

                stack         \- Waiting for more stack to be allocated.

                waitpage      \- Waiting for process manager to 

                                resolve a fault on a page.

                sigsuspend    \- Suspended for a signal.

                sigwaitinfo   \- Waiting for a signal.

                nanosleep     \- Sleeping for a period of time.

                mutex         \- Waiting to acquire a mutex

                condvar       \- Waiting for a condition variable to be 

                                signalled.

                join          \- Waiting for the completion of another 

                                thread.

                intr          \- Waiting for an interrupt.

                sem           \- Waiting to acquire a semaphore.

                .. data:: other = 1

                .. data:: dead = 2

                .. data:: running = 3

                .. data:: ready = 4

                .. data:: stopped = 5

                .. data:: send = 6

                .. data:: receive = 7

                .. data:: reply = 8

                .. data:: stack = 9

                .. data:: waitpage = 10

                .. data:: sigsuspend = 11

                .. data:: sigwaitinfo = 12

                .. data:: nanosleep = 13

                .. data:: mutex = 14

                .. data:: condvar = 15

                .. data:: join = 16

                .. data:: intr = 17

                .. data:: sem = 18

                """

                other = Enum.YLeaf(1, "other")

                dead = Enum.YLeaf(2, "dead")

                running = Enum.YLeaf(3, "running")

                ready = Enum.YLeaf(4, "ready")

                stopped = Enum.YLeaf(5, "stopped")

                send = Enum.YLeaf(6, "send")

                receive = Enum.YLeaf(7, "receive")

                reply = Enum.YLeaf(8, "reply")

                stack = Enum.YLeaf(9, "stack")

                waitpage = Enum.YLeaf(10, "waitpage")

                sigsuspend = Enum.YLeaf(11, "sigsuspend")

                sigwaitinfo = Enum.YLeaf(12, "sigwaitinfo")

                nanosleep = Enum.YLeaf(13, "nanosleep")

                mutex = Enum.YLeaf(14, "mutex")

                condvar = Enum.YLeaf(15, "condvar")

                join = Enum.YLeaf(16, "join")

                intr = Enum.YLeaf(17, "intr")

                sem = Enum.YLeaf(18, "sem")





    class CpmVirtualProcessTable(Entity):
        """
        This table contains information about virtual
        processes in a virtual machine.
        
        .. attribute:: cpmvirtualprocessentry
        
        	An entry containing the general statistics of a virtual process in a virtual machine
        	**type**\: list of  		 :py:class:`CpmVirtualProcessEntry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.CpmVirtualProcessTable, self).__init__()

            self.yang_name = "cpmVirtualProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cpmVirtualProcessEntry", ("cpmvirtualprocessentry", CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry))])
            self._leafs = OrderedDict()

            self.cpmvirtualprocessentry = YList(self)
            self._segment_path = lambda: "cpmVirtualProcessTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.CpmVirtualProcessTable, [], name, value)


        class CpmVirtualProcessEntry(Entity):
            """
            An entry containing the general statistics of a
            virtual process in a virtual machine.
            
            .. attribute:: cpmcputotalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmprocesspid  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry>`
            
            	**config**\: False
            
            .. attribute:: cpmvirtualprocessid  (key)
            
            	This object indicates the process ID of a virtual process. PID is unique only inside one address space. Virtual process PID should be considered along with  Parent process cpmProcessPID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmvirtualprocessname
            
            	This object indicates the name of a virtual process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: cpmvirtualprocessutil5sec
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 seconds
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmvirtualprocessutil1min
            
            	This indicates an estimated CPU utilization by a virtual process over the last one minute
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmvirtualprocessutil5min
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 minutes
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            	**units**\: percent
            
            .. attribute:: cpmvirtualprocessmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a  process running on Native OS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running  on Native OS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessinvokecount
            
            	The number of times a virtual process is invoked
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cpmvirtualprocessruntime
            
            	The amount of CPU time a virtual process has used in microseconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: cpmvirtualprocessmemallocatedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemAllocated. This object  needs to be supported only when the value of cpmVirtualProcessMemAllocated exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocesshcmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a process running on Native OS. This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessmemfreedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemFreed. This object needs to be supported only when the value of  cpmVirtualProcessMemFreed exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocesshcmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running on Native OS.This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry, self).__init__()

                self.yang_name = "cpmVirtualProcessEntry"
                self.yang_parent_name = "cpmVirtualProcessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['cpmcputotalindex','cpmprocesspid','cpmvirtualprocessid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('cpmcputotalindex', (YLeaf(YType.str, 'cpmCPUTotalIndex'), ['int'])),
                    ('cpmprocesspid', (YLeaf(YType.str, 'cpmProcessPID'), ['int'])),
                    ('cpmvirtualprocessid', (YLeaf(YType.uint32, 'cpmVirtualProcessID'), ['int'])),
                    ('cpmvirtualprocessname', (YLeaf(YType.str, 'cpmVirtualProcessName'), ['str'])),
                    ('cpmvirtualprocessutil5sec', (YLeaf(YType.uint32, 'cpmVirtualProcessUtil5Sec'), ['int'])),
                    ('cpmvirtualprocessutil1min', (YLeaf(YType.uint32, 'cpmVirtualProcessUtil1Min'), ['int'])),
                    ('cpmvirtualprocessutil5min', (YLeaf(YType.uint32, 'cpmVirtualProcessUtil5Min'), ['int'])),
                    ('cpmvirtualprocessmemallocated', (YLeaf(YType.uint32, 'cpmVirtualProcessMemAllocated'), ['int'])),
                    ('cpmvirtualprocessmemfreed', (YLeaf(YType.uint32, 'cpmVirtualProcessMemFreed'), ['int'])),
                    ('cpmvirtualprocessinvokecount', (YLeaf(YType.uint32, 'cpmVirtualProcessInvokeCount'), ['int'])),
                    ('cpmvirtualprocessruntime', (YLeaf(YType.uint32, 'cpmVirtualProcessRuntime'), ['int'])),
                    ('cpmvirtualprocessmemallocatedovrflw', (YLeaf(YType.uint32, 'cpmVirtualProcessMemAllocatedOvrflw'), ['int'])),
                    ('cpmvirtualprocesshcmemallocated', (YLeaf(YType.uint64, 'cpmVirtualProcessHCMemAllocated'), ['int'])),
                    ('cpmvirtualprocessmemfreedovrflw', (YLeaf(YType.uint32, 'cpmVirtualProcessMemFreedOvrflw'), ['int'])),
                    ('cpmvirtualprocesshcmemfreed', (YLeaf(YType.uint64, 'cpmVirtualProcessHCMemFreed'), ['int'])),
                ])
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmvirtualprocessid = None
                self.cpmvirtualprocessname = None
                self.cpmvirtualprocessutil5sec = None
                self.cpmvirtualprocessutil1min = None
                self.cpmvirtualprocessutil5min = None
                self.cpmvirtualprocessmemallocated = None
                self.cpmvirtualprocessmemfreed = None
                self.cpmvirtualprocessinvokecount = None
                self.cpmvirtualprocessruntime = None
                self.cpmvirtualprocessmemallocatedovrflw = None
                self.cpmvirtualprocesshcmemallocated = None
                self.cpmvirtualprocessmemfreedovrflw = None
                self.cpmvirtualprocesshcmemfreed = None
                self._segment_path = lambda: "cpmVirtualProcessEntry" + "[cpmCPUTotalIndex='" + str(self.cpmcputotalindex) + "']" + "[cpmProcessPID='" + str(self.cpmprocesspid) + "']" + "[cpmVirtualProcessID='" + str(self.cpmvirtualprocessid) + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmVirtualProcessTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmvirtualprocessid', 'cpmvirtualprocessname', 'cpmvirtualprocessutil5sec', 'cpmvirtualprocessutil1min', 'cpmvirtualprocessutil5min', 'cpmvirtualprocessmemallocated', 'cpmvirtualprocessmemfreed', 'cpmvirtualprocessinvokecount', 'cpmvirtualprocessruntime', 'cpmvirtualprocessmemallocatedovrflw', 'cpmvirtualprocesshcmemallocated', 'cpmvirtualprocessmemfreedovrflw', 'cpmvirtualprocesshcmemfreed'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOPROCESSMIB()
        return self._top_entity



