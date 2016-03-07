


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RttMonRttType_Enum' : _MetaInfoEnum('RttMonRttType_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'echo':'ECHO',
            'pathEcho':'PATHECHO',
            'fileIO':'FILEIO',
            'script':'SCRIPT',
            'udpEcho':'UDPECHO',
            'tcpConnect':'TCPCONNECT',
            'http':'HTTP',
            'dns':'DNS',
            'jitter':'JITTER',
            'dlsw':'DLSW',
            'dhcp':'DHCP',
            'ftp':'FTP',
            'voip':'VOIP',
            'rtp':'RTP',
            'lspGroup':'LSPGROUP',
            'icmpjitter':'ICMPJITTER',
            'lspPing':'LSPPING',
            'lspTrace':'LSPTRACE',
            'ethernetPing':'ETHERNETPING',
            'ethernetJitter':'ETHERNETJITTER',
            'lspPingPseudowire':'LSPPINGPSEUDOWIRE',
            'video':'VIDEO',
            'y1731Delay':'Y1731DELAY',
            'y1731Loss':'Y1731LOSS',
            'mcastJitter':'MCASTJITTER',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMonLSPPingReplyMode_Enum' : _MetaInfoEnum('RttMonLSPPingReplyMode_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'replyIpv4Udp':'REPLYIPV4UDP',
            'replyIpv4UdpRA':'REPLYIPV4UDPRA',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMonProtocol_Enum' : _MetaInfoEnum('RttMonProtocol_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'ipIcmpEcho':'IPICMPECHO',
            'ipUdpEchoAppl':'IPUDPECHOAPPL',
            'snaRUEcho':'SNARUECHO',
            'snaLU0EchoAppl':'SNALU0ECHOAPPL',
            'snaLU2EchoAppl':'SNALU2ECHOAPPL',
            'snaLU62Echo':'SNALU62ECHO',
            'snaLU62EchoAppl':'SNALU62ECHOAPPL',
            'appleTalkEcho':'APPLETALKECHO',
            'appleTalkEchoAppl':'APPLETALKECHOAPPL',
            'decNetEcho':'DECNETECHO',
            'decNetEchoAppl':'DECNETECHOAPPL',
            'ipxEcho':'IPXECHO',
            'ipxEchoAppl':'IPXECHOAPPL',
            'isoClnsEcho':'ISOCLNSECHO',
            'isoClnsEchoAppl':'ISOCLNSECHOAPPL',
            'vinesEcho':'VINESECHO',
            'vinesEchoAppl':'VINESECHOAPPL',
            'xnsEcho':'XNSECHO',
            'xnsEchoAppl':'XNSECHOAPPL',
            'apolloEcho':'APOLLOECHO',
            'apolloEchoAppl':'APOLLOECHOAPPL',
            'netbiosEchoAppl':'NETBIOSECHOAPPL',
            'ipTcpConn':'IPTCPCONN',
            'httpAppl':'HTTPAPPL',
            'dnsAppl':'DNSAPPL',
            'jitterAppl':'JITTERAPPL',
            'dlswAppl':'DLSWAPPL',
            'dhcpAppl':'DHCPAPPL',
            'ftpAppl':'FTPAPPL',
            'mplsLspPingAppl':'MPLSLSPPINGAPPL',
            'voipAppl':'VOIPAPPL',
            'rtpAppl':'RTPAPPL',
            'icmpJitterAppl':'ICMPJITTERAPPL',
            'ethernetPingAppl':'ETHERNETPINGAPPL',
            'ethernetJitterAppl':'ETHERNETJITTERAPPL',
            'videoAppl':'VIDEOAPPL',
            'y1731dmm':'Y1731DMM',
            'y17311dm':'Y17311DM',
            'y1731lmm':'Y1731LMM',
            'mcastJitterAppl':'MCASTJITTERAPPL',
            'y1731slm':'Y1731SLM',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMplsVpnMonLpdGrpStatus_Enum' : _MetaInfoEnum('RttMplsVpnMonLpdGrpStatus_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'up':'UP',
            'partial':'PARTIAL',
            'down':'DOWN',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMonReactVar_Enum' : _MetaInfoEnum('RttMonReactVar_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'rtt':'RTT',
            'jitterSDAvg':'JITTERSDAVG',
            'jitterDSAvg':'JITTERDSAVG',
            'packetLossSD':'PACKETLOSSSD',
            'packetLossDS':'PACKETLOSSDS',
            'mos':'MOS',
            'timeout':'TIMEOUT',
            'connectionLoss':'CONNECTIONLOSS',
            'verifyError':'VERIFYERROR',
            'jitterAvg':'JITTERAVG',
            'icpif':'ICPIF',
            'packetMIA':'PACKETMIA',
            'packetLateArrival':'PACKETLATEARRIVAL',
            'packetOutOfSequence':'PACKETOUTOFSEQUENCE',
            'maxOfPositiveSD':'MAXOFPOSITIVESD',
            'maxOfNegativeSD':'MAXOFNEGATIVESD',
            'maxOfPositiveDS':'MAXOFPOSITIVEDS',
            'maxOfNegativeDS':'MAXOFNEGATIVEDS',
            'iaJitterDS':'IAJITTERDS',
            'frameLossDS':'FRAMELOSSDS',
            'mosLQDS':'MOSLQDS',
            'mosCQDS':'MOSCQDS',
            'rFactorDS':'RFACTORDS',
            'successivePacketLoss':'SUCCESSIVEPACKETLOSS',
            'maxOfLatencyDS':'MAXOFLATENCYDS',
            'maxOfLatencySD':'MAXOFLATENCYSD',
            'latencyDSAvg':'LATENCYDSAVG',
            'latencySDAvg':'LATENCYSDAVG',
            'packetLoss':'PACKETLOSS',
            'iaJitterSD':'IAJITTERSD',
            'mosCQSD':'MOSCQSD',
            'rFactorSD':'RFACTORSD',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttReset_Enum' : _MetaInfoEnum('RttReset_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'ready':'READY',
            'reset':'RESET',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMplsVpnMonLpdFailureSense_Enum' : _MetaInfoEnum('RttMplsVpnMonLpdFailureSense_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'noPath':'NOPATH',
            'allPathsBroken':'ALLPATHSBROKEN',
            'allPathsUnexplorable':'ALLPATHSUNEXPLORABLE',
            'allPathsBrokenOrUnexplorable':'ALLPATHSBROKENORUNEXPLORABLE',
            'timeout':'TIMEOUT',
            'error':'ERROR',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMonCodecType_Enum' : _MetaInfoEnum('RttMonCodecType_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'g711ulaw':'G711ULAW',
            'g711alaw':'G711ALAW',
            'g729a':'G729A',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMonOperation_Enum' : _MetaInfoEnum('RttMonOperation_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'NOTAPPLICABLE',
            'httpGet':'HTTPGET',
            'httpRaw':'HTTPRAW',
            'ftpGet':'FTPGET',
            'ftpPassive':'FTPPASSIVE',
            'ftpActive':'FTPACTIVE',
            'voipDTAlertRinging':'VOIPDTALERTRINGING',
            'voipDTConnectOK':'VOIPDTCONNECTOK',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttMplsVpnMonRttType_Enum' : _MetaInfoEnum('RttMplsVpnMonRttType_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'jitter':'JITTER',
            'echo':'ECHO',
            'pathEcho':'PATHECHO',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttResponseSense_Enum' : _MetaInfoEnum('RttResponseSense_Enum', 'ydk.models.rttmon.CISCO_RTTMON_TC_MIB',
        {
            'other':'OTHER',
            'ok':'OK',
            'disconnected':'DISCONNECTED',
            'overThreshold':'OVERTHRESHOLD',
            'timeout':'TIMEOUT',
            'busy':'BUSY',
            'notConnected':'NOTCONNECTED',
            'dropped':'DROPPED',
            'sequenceError':'SEQUENCEERROR',
            'verifyError':'VERIFYERROR',
            'applicationSpecific':'APPLICATIONSPECIFIC',
            'dnsServerTimeout':'DNSSERVERTIMEOUT',
            'tcpConnectTimeout':'TCPCONNECTTIMEOUT',
            'httpTransactionTimeout':'HTTPTRANSACTIONTIMEOUT',
            'dnsQueryError':'DNSQUERYERROR',
            'httpError':'HTTPERROR',
            'error':'ERROR',
            'mplsLspEchoTxError':'MPLSLSPECHOTXERROR',
            'mplsLspUnreachable':'MPLSLSPUNREACHABLE',
            'mplsLspMalformedReq':'MPLSLSPMALFORMEDREQ',
            'mplsLspReachButNotFEC':'MPLSLSPREACHBUTNOTFEC',
            'enableOk':'ENABLEOK',
            'enableNoConnect':'ENABLENOCONNECT',
            'enableVersionFail':'ENABLEVERSIONFAIL',
            'enableInternalError':'ENABLEINTERNALERROR',
            'enableAbort':'ENABLEABORT',
            'enableFail':'ENABLEFAIL',
            'enableAuthFail':'ENABLEAUTHFAIL',
            'enableFormatError':'ENABLEFORMATERROR',
            'enablePortInUse':'ENABLEPORTINUSE',
            'statsRetrieveOk':'STATSRETRIEVEOK',
            'statsRetrieveNoConnect':'STATSRETRIEVENOCONNECT',
            'statsRetrieveVersionFail':'STATSRETRIEVEVERSIONFAIL',
            'statsRetrieveInternalError':'STATSRETRIEVEINTERNALERROR',
            'statsRetrieveAbort':'STATSRETRIEVEABORT',
            'statsRetrieveFail':'STATSRETRIEVEFAIL',
            'statsRetrieveAuthFail':'STATSRETRIEVEAUTHFAIL',
            'statsRetrieveFormatError':'STATSRETRIEVEFORMATERROR',
            'statsRetrievePortInUse':'STATSRETRIEVEPORTINUSE',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
}