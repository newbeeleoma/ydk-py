""" NOTIFICATION_LOG_MIB 

The MIB module for logging SNMP Notifications, that is, Traps
and Informs.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class NOTIFICATIONLOGMIB(object):
    """
    
    
    .. attribute:: nlmconfig
    
    	
    	**type**\: :py:class:`NlmConfig <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmConfig>`
    
    .. attribute:: nlmconfiglogtable
    
    	A table of logging control entries
    	**type**\: :py:class:`NlmConfigLogTable <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmConfigLogTable>`
    
    .. attribute:: nlmlogtable
    
    	A table of Notification log entries.  It is an implementation\-specific matter whether entries in this table are preserved across initializations of the management system.  In general one would expect that they are not.  Note that keeping entries across initializations of the management system leads to some confusion with counters and TimeStamps, since both of those are based on sysUpTime, which resets on management initialization.  In this situation, counters apply only after the reset and nlmLogTime for entries made before the reset MUST be set to 0
    	**type**\: :py:class:`NlmLogTable <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmLogTable>`
    
    .. attribute:: nlmlogvariabletable
    
    	A table of variables to go with Notification log entries
    	**type**\: :py:class:`NlmLogVariableTable <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmLogVariableTable>`
    
    .. attribute:: nlmstats
    
    	
    	**type**\: :py:class:`NlmStats <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmStats>`
    
    

    """

    _prefix = 'notification-log'
    _revision = '2000-11-27'

    def __init__(self):
        self.nlmconfig = NOTIFICATIONLOGMIB.NlmConfig()
        self.nlmconfig.parent = self
        self.nlmconfiglogtable = NOTIFICATIONLOGMIB.NlmConfigLogTable()
        self.nlmconfiglogtable.parent = self
        self.nlmlogtable = NOTIFICATIONLOGMIB.NlmLogTable()
        self.nlmlogtable.parent = self
        self.nlmlogvariabletable = NOTIFICATIONLOGMIB.NlmLogVariableTable()
        self.nlmlogvariabletable.parent = self
        self.nlmstats = NOTIFICATIONLOGMIB.NlmStats()
        self.nlmstats.parent = self


    class NlmConfig(object):
        """
        
        
        .. attribute:: nlmconfigglobalageout
        
        	The number of minutes a Notification SHOULD be kept in a log before it is automatically removed.  If an application changes the value of nlmConfigGlobalAgeOut, Notifications older than the new time MAY be discarded to meet the new time.  A value of 0 means no age out.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: nlmconfigglobalentrylimit
        
        	The maximum number of notification entries that may be held in nlmLogTable for all nlmLogNames added together.  A particular setting does not guarantee that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications MUST be discarded to bring the log down to the new limit \- thus the value of nlmConfigGlobalEntryLimit MUST take precedence over the values of nlmConfigGlobalAgeOut and nlmConfigLogEntryLimit, even if the Notification being discarded has been present for fewer minutes than the value of nlmConfigGlobalAgeOut, or if the named log has fewer entries than that specified in nlmConfigLogEntryLimit.  A value of 0 means no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'notification-log'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmconfigglobalageout = None
            self.nlmconfigglobalentrylimit = None

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmconfigglobalageout is not None:
                return True

            if self.nlmconfigglobalentrylimit is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NOTIFICATIONLOGMIB.NlmConfig']['meta_info']


    class NlmConfigLogTable(object):
        """
        A table of logging control entries.
        
        .. attribute:: nlmconfiglogentry
        
        	A logging control entry.  Depending on the entry's storage type entries may be supplied by the system or created and deleted by applications using nlmConfigLogEntryStatus
        	**type**\: list of :py:class:`NlmConfigLogEntry <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry>`
        
        

        """

        _prefix = 'notification-log'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmconfiglogentry = YList()
            self.nlmconfiglogentry.parent = self
            self.nlmconfiglogentry.name = 'nlmconfiglogentry'


        class NlmConfigLogEntry(object):
            """
            A logging control entry.  Depending on the entry's storage type
            entries may be supplied by the system or created and deleted by
            applications using nlmConfigLogEntryStatus.
            
            .. attribute:: nlmlogname
            
            	The name of the log.  An implementation may allow multiple named logs, up to some implementation\-specific limit (which may be none).  A zero\-length log name is reserved for creation and deletion by the managed system, and MUST be used as the default log name by systems that do not support named logs
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: nlmconfiglogadminstatus
            
            	Control to enable or disable the log without otherwise disturbing the log's entry.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\: :py:class:`NlmConfigLogAdminStatus_Enum <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry.NlmConfigLogAdminStatus_Enum>`
            
            .. attribute:: nlmconfiglogentrylimit
            
            	The maximum number of notification entries that can be held in nlmLogTable for this named log.  A particular setting does not guarantee that that much data can be held.  If an application changes the limit while there are Notifications in the log, the oldest Notifications are discarded to bring the log down to the new limit.  A value of 0 indicates no limit.  Please be aware that contention between multiple managers trying to set this object to different values MAY affect the reliability and completeness of data seen by each manager
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmconfiglogentrystatus
            
            	Control for creating and deleting entries.  Entries may be modified while active.  For non\-null\-named logs, the managed system records the security credentials from the request that sets nlmConfigLogStatus to 'active' and uses that identity to apply access control to the objects in the Notification to decide if that Notification may be logged
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nlmconfiglogfiltername
            
            	A value of snmpNotifyFilterProfileName as used as an index into the snmpNotifyFilterTable in the SNMP Notification MIB, specifying the locally or remotely originated Notifications to be filtered out and not logged in this log.  A zero\-length value or a name that does not identify an existing entry in snmpNotifyFilterTable indicate no Notifications are to be logged in this log
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: nlmconfiglogoperstatus
            
            	The operational status of this log\:  disabled  administratively disabled  operational    administratively enabled and working  noFilter  administratively enabled but either           nlmConfigLogFilterName is zero length           or does not name an existing entry in           snmpNotifyFilterTable
            	**type**\: :py:class:`NlmConfigLogOperStatus_Enum <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry.NlmConfigLogOperStatus_Enum>`
            
            .. attribute:: nlmconfiglogstoragetype
            
            	The storage type of this conceptual row
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: nlmstatslognotificationsbumped
            
            	The number of log entries discarded from this named log to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmstatslognotificationslogged
            
            	The number of Notifications put in this named log
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'notification-log'
            _revision = '2000-11-27'

            def __init__(self):
                self.parent = None
                self.nlmlogname = None
                self.nlmconfiglogadminstatus = None
                self.nlmconfiglogentrylimit = None
                self.nlmconfiglogentrystatus = None
                self.nlmconfiglogfiltername = None
                self.nlmconfiglogoperstatus = None
                self.nlmconfiglogstoragetype = None
                self.nlmstatslognotificationsbumped = None
                self.nlmstatslognotificationslogged = None

            class NlmConfigLogAdminStatus_Enum(Enum):
                """
                NlmConfigLogAdminStatus_Enum

                Control to enable or disable the log without otherwise
                disturbing the log's entry.
                
                Please be aware that contention between multiple managers
                trying to set this object to different values MAY affect the
                reliability and completeness of data seen by each manager.

                """

                ENABLED = 1

                DISABLED = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry.NlmConfigLogAdminStatus_Enum']


            class NlmConfigLogOperStatus_Enum(Enum):
                """
                NlmConfigLogOperStatus_Enum

                The operational status of this log\:
                
                disabled  administratively disabled
                
                operational    administratively enabled and working
                
                noFilter  administratively enabled but either
                          nlmConfigLogFilterName is zero length
                          or does not name an existing entry in
                          snmpNotifyFilterTable

                """

                DISABLED = 1

                OPERATIONAL = 2

                NOFILTER = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry.NlmConfigLogOperStatus_Enum']


            @property
            def _common_path(self):
                if self.nlmlogname is None:
                    raise YPYDataValidationError('Key property nlmlogname is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfigLogTable/NOTIFICATION-LOG-MIB:nlmConfigLogEntry[NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nlmlogname is not None:
                    return True

                if self.nlmconfiglogadminstatus is not None:
                    return True

                if self.nlmconfiglogentrylimit is not None:
                    return True

                if self.nlmconfiglogentrystatus is not None:
                    return True

                if self.nlmconfiglogfiltername is not None:
                    return True

                if self.nlmconfiglogoperstatus is not None:
                    return True

                if self.nlmconfiglogstoragetype is not None:
                    return True

                if self.nlmstatslognotificationsbumped is not None:
                    return True

                if self.nlmstatslognotificationslogged is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NOTIFICATIONLOGMIB.NlmConfigLogTable.NlmConfigLogEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmConfigLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmconfiglogentry is not None:
                for child_ref in self.nlmconfiglogentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NOTIFICATIONLOGMIB.NlmConfigLogTable']['meta_info']


    class NlmLogTable(object):
        """
        A table of Notification log entries.
        
        It is an implementation\-specific matter whether entries in this
        table are preserved across initializations of the management
        system.  In general one would expect that they are not.
        
        Note that keeping entries across initializations of the
        management system leads to some confusion with counters and
        TimeStamps, since both of those are based on sysUpTime, which
        resets on management initialization.  In this situation,
        counters apply only after the reset and nlmLogTime for entries
        made before the reset MUST be set to 0.
        
        .. attribute:: nlmlogentry
        
        	A Notification log entry.  Entries appear in this table when Notifications occur and pass filtering by nlmConfigLogFilterName and access control.  They are removed to make way for new entries due to lack of resources or the values of nlmConfigGlobalEntryLimit, nlmConfigGlobalAgeOut, or nlmConfigLogEntryLimit.  If adding an entry would exceed nlmConfigGlobalEntryLimit or system resources in general, the oldest entry in any log SHOULD be removed to make room for the new one.  If adding an entry would exceed nlmConfigLogEntryLimit the oldest entry in that log SHOULD be removed to make room for the new one.  Before the managed system puts a locally\-generated Notification into a non\-null\-named log it assures that the creator of the log has access to the information in the Notification.  If not it does not log that Notification in that log
        	**type**\: list of :py:class:`NlmLogEntry <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmLogTable.NlmLogEntry>`
        
        

        """

        _prefix = 'notification-log'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmlogentry = YList()
            self.nlmlogentry.parent = self
            self.nlmlogentry.name = 'nlmlogentry'


        class NlmLogEntry(object):
            """
            A Notification log entry.
            
            Entries appear in this table when Notifications occur and pass
            filtering by nlmConfigLogFilterName and access control.  They are
            removed to make way for new entries due to lack of resources or
            the values of nlmConfigGlobalEntryLimit, nlmConfigGlobalAgeOut, or
            nlmConfigLogEntryLimit.
            
            If adding an entry would exceed nlmConfigGlobalEntryLimit or system
            resources in general, the oldest entry in any log SHOULD be removed
            to make room for the new one.
            
            If adding an entry would exceed nlmConfigLogEntryLimit the oldest
            entry in that log SHOULD be removed to make room for the new one.
            
            Before the managed system puts a locally\-generated Notification
            into a non\-null\-named log it assures that the creator of the log
            has access to the information in the Notification.  If not it
            does not log that Notification in that log.
            
            .. attribute:: nlmlogindex
            
            	A monotonically increasing integer for the sole purpose of indexing entries within the named log.  When it reaches the maximum value, an extremely unlikely event, the agent wraps the value back to 1
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: nlmlogcontextengineid
            
            	If the Notification was received in a protocol which has a contextEngineID element like SNMPv3, this object has that value. Otherwise its value is a zero\-length string
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: nlmlogcontextname
            
            	The name of the SNMP MIB context from which the Notification came. For SNMPv1 Traps this is the community string from the Trap
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: nlmlogdateandtime
            
            	The local date and time when the entry was logged, instantiated only by systems that have date and time capability
            	**type**\: str
            
            .. attribute:: nlmlogengineid
            
            	The identification of the SNMP engine at which the Notification originated.  If the log can contain Notifications from only one engine or the Trap is in SNMPv1 format, this object is a zero\-length string
            	**type**\: str
            
            	**pattern:** (([0\-9a\-fA\-F]){2}(\:([0\-9a\-fA\-F]){2})\*)?
            
            .. attribute:: nlmlogenginetaddress
            
            	The transport service address of the SNMP engine from which the Notification was received, formatted according to the corresponding value of nlmLogEngineTDomain. This is used to identify the source of an SNMPv1 trap, since an nlmLogEngineId cannot be extracted from the SNMPv1 trap pdu.  This object MUST always be instantiated, even if the log can contain Notifications from only one engine.  Please be aware that the nlmLogEngineTAddress may not uniquely identify the SNMP engine from which the Notification was received. For example, if an SNMP engine uses DHCP or NAT to obtain ip addresses, the address it uses may be shared with other network devices, and hence will not uniquely identify the SNMP engine
            	**type**\: str
            
            	**pattern:** (\\d\*(.\\d\*)\*)?
            
            .. attribute:: nlmlogenginetdomain
            
            	Indicates the kind of transport service by which a Notification was received from an SNMP engine. nlmLogEngineTAddress contains the transport service address of the SNMP engine from which this Notification was received.  Possible values for this object are presently found in the Transport Mappings for SNMPv2 document (RFC 1906 [8])
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlognotificationid
            
            	The NOTIFICATION\-TYPE object identifier of the Notification that occurred
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogtime
            
            	The value of sysUpTime when the entry was placed in the log. If the entry occurred before the most recent management system initialization this object value MUST be set to zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'notification-log'
            _revision = '2000-11-27'

            def __init__(self):
                self.parent = None
                self.nlmlogindex = None
                self.nlmlogname = None
                self.nlmlogcontextengineid = None
                self.nlmlogcontextname = None
                self.nlmlogdateandtime = None
                self.nlmlogengineid = None
                self.nlmlogenginetaddress = None
                self.nlmlogenginetdomain = None
                self.nlmlognotificationid = None
                self.nlmlogtime = None

            @property
            def _common_path(self):
                if self.nlmlogindex is None:
                    raise YPYDataValidationError('Key property nlmlogindex is None')
                if self.nlmlogname is None:
                    raise YPYDataValidationError('Key property nlmlogname is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogTable/NOTIFICATION-LOG-MIB:nlmLogEntry[NOTIFICATION-LOG-MIB:nlmLogIndex = ' + str(self.nlmlogindex) + '][NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nlmlogindex is not None:
                    return True

                if self.nlmlogname is not None:
                    return True

                if self.nlmlogcontextengineid is not None:
                    return True

                if self.nlmlogcontextname is not None:
                    return True

                if self.nlmlogdateandtime is not None:
                    return True

                if self.nlmlogengineid is not None:
                    return True

                if self.nlmlogenginetaddress is not None:
                    return True

                if self.nlmlogenginetdomain is not None:
                    return True

                if self.nlmlognotificationid is not None:
                    return True

                if self.nlmlogtime is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NOTIFICATIONLOGMIB.NlmLogTable.NlmLogEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmlogentry is not None:
                for child_ref in self.nlmlogentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NOTIFICATIONLOGMIB.NlmLogTable']['meta_info']


    class NlmLogVariableTable(object):
        """
        A table of variables to go with Notification log entries.
        
        .. attribute:: nlmlogvariableentry
        
        	A Notification log entry variable.  Entries appear in this table when there are variables in the varbind list of a Notification in nlmLogTable
        	**type**\: list of :py:class:`NlmLogVariableEntry <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmLogVariableTable.NlmLogVariableEntry>`
        
        

        """

        _prefix = 'notification-log'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmlogvariableentry = YList()
            self.nlmlogvariableentry.parent = self
            self.nlmlogvariableentry.name = 'nlmlogvariableentry'


        class NlmLogVariableEntry(object):
            """
            A Notification log entry variable.
            
            Entries appear in this table when there are variables in
            the varbind list of a Notification in nlmLogTable.
            
            .. attribute:: nlmlogindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogname
            
            	
            	**type**\: str
            
            	**range:** 0..32
            
            .. attribute:: nlmlogvariableindex
            
            	A monotonically increasing integer, starting at 1 for a given nlmLogIndex, for indexing variables within the logged Notification
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nlmlogvariablecounter32val
            
            	The value when nlmLogVariableType is 'counter32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariablecounter64val
            
            	The value when nlmLogVariableType is 'counter64'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: nlmlogvariableid
            
            	The variable's object identifier
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariableinteger32val
            
            	The value when nlmLogVariableType is 'integer32'
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: nlmlogvariableipaddressval
            
            	The value when nlmLogVariableType is 'ipAddress'. Although this seems to be unfriendly for IPv6, we have to recognize that there are a number of older MIBs that do contain an IPv4 format address, known as IpAddress.  IPv6 addresses are represented using TAddress or InetAddress, and so the underlying datatype is OCTET STRING, and their value would be stored in the nlmLogVariableOctetStringVal column
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: nlmlogvariableoctetstringval
            
            	The value when nlmLogVariableType is 'octetString'
            	**type**\: str
            
            .. attribute:: nlmlogvariableoidval
            
            	The value when nlmLogVariableType is 'objectId'
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: nlmlogvariableopaqueval
            
            	The value when nlmLogVariableType is 'opaque'
            	**type**\: str
            
            .. attribute:: nlmlogvariabletimeticksval
            
            	The value when nlmLogVariableType is 'timeTicks'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariableunsigned32val
            
            	The value when nlmLogVariableType is 'unsigned32'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nlmlogvariablevaluetype
            
            	The type of the value.  One and only one of the value objects that follow must be instantiated, based on this type
            	**type**\: :py:class:`NlmLogVariableValueType_Enum <ydk.models.notification.NOTIFICATION_LOG_MIB.NOTIFICATIONLOGMIB.NlmLogVariableTable.NlmLogVariableEntry.NlmLogVariableValueType_Enum>`
            
            

            """

            _prefix = 'notification-log'
            _revision = '2000-11-27'

            def __init__(self):
                self.parent = None
                self.nlmlogindex = None
                self.nlmlogname = None
                self.nlmlogvariableindex = None
                self.nlmlogvariablecounter32val = None
                self.nlmlogvariablecounter64val = None
                self.nlmlogvariableid = None
                self.nlmlogvariableinteger32val = None
                self.nlmlogvariableipaddressval = None
                self.nlmlogvariableoctetstringval = None
                self.nlmlogvariableoidval = None
                self.nlmlogvariableopaqueval = None
                self.nlmlogvariabletimeticksval = None
                self.nlmlogvariableunsigned32val = None
                self.nlmlogvariablevaluetype = None

            class NlmLogVariableValueType_Enum(Enum):
                """
                NlmLogVariableValueType_Enum

                The type of the value.  One and only one of the value
                objects that follow must be instantiated, based on this type.

                """

                COUNTER32 = 1

                UNSIGNED32 = 2

                TIMETICKS = 3

                INTEGER32 = 4

                IPADDRESS = 5

                OCTETSTRING = 6

                OBJECTID = 7

                COUNTER64 = 8

                OPAQUE = 9


                @staticmethod
                def _meta_info():
                    from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                    return meta._meta_table['NOTIFICATIONLOGMIB.NlmLogVariableTable.NlmLogVariableEntry.NlmLogVariableValueType_Enum']


            @property
            def _common_path(self):
                if self.nlmlogindex is None:
                    raise YPYDataValidationError('Key property nlmlogindex is None')
                if self.nlmlogname is None:
                    raise YPYDataValidationError('Key property nlmlogname is None')
                if self.nlmlogvariableindex is None:
                    raise YPYDataValidationError('Key property nlmlogvariableindex is None')

                return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogVariableTable/NOTIFICATION-LOG-MIB:nlmLogVariableEntry[NOTIFICATION-LOG-MIB:nlmLogIndex = ' + str(self.nlmlogindex) + '][NOTIFICATION-LOG-MIB:nlmLogName = ' + str(self.nlmlogname) + '][NOTIFICATION-LOG-MIB:nlmLogVariableIndex = ' + str(self.nlmlogvariableindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nlmlogindex is not None:
                    return True

                if self.nlmlogname is not None:
                    return True

                if self.nlmlogvariableindex is not None:
                    return True

                if self.nlmlogvariablecounter32val is not None:
                    return True

                if self.nlmlogvariablecounter64val is not None:
                    return True

                if self.nlmlogvariableid is not None:
                    return True

                if self.nlmlogvariableinteger32val is not None:
                    return True

                if self.nlmlogvariableipaddressval is not None:
                    return True

                if self.nlmlogvariableoctetstringval is not None:
                    return True

                if self.nlmlogvariableoidval is not None:
                    return True

                if self.nlmlogvariableopaqueval is not None:
                    return True

                if self.nlmlogvariabletimeticksval is not None:
                    return True

                if self.nlmlogvariableunsigned32val is not None:
                    return True

                if self.nlmlogvariablevaluetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
                return meta._meta_table['NOTIFICATIONLOGMIB.NlmLogVariableTable.NlmLogVariableEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmLogVariableTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmlogvariableentry is not None:
                for child_ref in self.nlmlogvariableentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NOTIFICATIONLOGMIB.NlmLogVariableTable']['meta_info']


    class NlmStats(object):
        """
        
        
        .. attribute:: nlmstatsglobalnotificationsbumped
        
        	The number of log entries discarded to make room for a new entry due to lack of resources or the value of nlmConfigGlobalEntryLimit or nlmConfigLogEntryLimit.  This does not include entries discarded due to the value of nlmConfigGlobalAgeOut
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: nlmstatsglobalnotificationslogged
        
        	The number of Notifications put into the nlmLogTable.  This counts a Notification once for each log entry, so a Notification  put into multiple logs is counted multiple times
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'notification-log'
        _revision = '2000-11-27'

        def __init__(self):
            self.parent = None
            self.nlmstatsglobalnotificationsbumped = None
            self.nlmstatsglobalnotificationslogged = None

        @property
        def _common_path(self):

            return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB/NOTIFICATION-LOG-MIB:nlmStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nlmstatsglobalnotificationsbumped is not None:
                return True

            if self.nlmstatsglobalnotificationslogged is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
            return meta._meta_table['NOTIFICATIONLOGMIB.NlmStats']['meta_info']

    @property
    def _common_path(self):

        return '/NOTIFICATION-LOG-MIB:NOTIFICATION-LOG-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.nlmconfig is not None and self.nlmconfig._has_data():
            return True

        if self.nlmconfig is not None and self.nlmconfig.is_presence():
            return True

        if self.nlmconfiglogtable is not None and self.nlmconfiglogtable._has_data():
            return True

        if self.nlmconfiglogtable is not None and self.nlmconfiglogtable.is_presence():
            return True

        if self.nlmlogtable is not None and self.nlmlogtable._has_data():
            return True

        if self.nlmlogtable is not None and self.nlmlogtable.is_presence():
            return True

        if self.nlmlogvariabletable is not None and self.nlmlogvariabletable._has_data():
            return True

        if self.nlmlogvariabletable is not None and self.nlmlogvariabletable.is_presence():
            return True

        if self.nlmstats is not None and self.nlmstats._has_data():
            return True

        if self.nlmstats is not None and self.nlmstats.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.notification._meta import _NOTIFICATION_LOG_MIB as meta
        return meta._meta_table['NOTIFICATIONLOGMIB']['meta_info']

