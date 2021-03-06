""" Cisco_IOS_XR_ipv6_smiap_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv6\-smiap package configuration.

This module contains definitions
for the following management objects\:
  ipv6\-virtual\: IPv6 virtual address for management interfaces

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Ipv6Virtual(_Entity_):
    """
    IPv6 virtual address for management interfaces
    
    .. attribute:: vrfs
    
    	VRFs for the virtual IPv6 addresses
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg.Ipv6Virtual.Vrfs>`
    
    .. attribute:: use_as_source_address
    
    	Enable use as default source address on sourced packets
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    

    """

    _prefix = 'ipv6-smiap-cfg'
    _revision = '2016-07-04'

    def __init__(self):
        if sys.version_info > (3,):
            super().__init__()
        else:
            super(Ipv6Virtual, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv6-virtual"
        self.yang_parent_name = "Cisco-IOS-XR-ipv6-smiap-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv6Virtual.Vrfs))])
        self._leafs = OrderedDict([
            ('use_as_source_address', (YLeaf(YType.empty, 'use-as-source-address'), ['Empty'])),
        ])
        self.use_as_source_address = None

        self.vrfs = Ipv6Virtual.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv6-smiap-cfg:ipv6-virtual"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv6Virtual, ['use_as_source_address'], name, value)


    class Vrfs(_Entity_):
        """
        VRFs for the virtual IPv6 addresses
        
        .. attribute:: vrf
        
        	A VRF for a virtual IPv6 address.  Specify 'default' for VRF default
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg.Ipv6Virtual.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv6-smiap-cfg'
        _revision = '2016-07-04'

        def __init__(self):
            if sys.version_info > (3,):
                super().__init__()
            else:
                super(Ipv6Virtual.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv6-virtual"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Ipv6Virtual.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-smiap-cfg:ipv6-virtual/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv6Virtual.Vrfs, [], name, value)


        class Vrf(_Entity_):
            """
            A VRF for a virtual IPv6 address.  Specify
            'default' for VRF default
            
            .. attribute:: vrf_name  (key)
            
            	Name of VRF
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: address
            
            	IPv6 address and mask
            	**type**\:  :py:class:`Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg.Ipv6Virtual.Vrfs.Vrf.Address>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv6-smiap-cfg'
            _revision = '2016-07-04'

            def __init__(self):
                if sys.version_info > (3,):
                    super().__init__()
                else:
                    super(Ipv6Virtual.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("address", ("address", Ipv6Virtual.Vrfs.Vrf.Address))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.address = None
                self._children_name_map["address"] = "address"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv6-smiap-cfg:ipv6-virtual/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv6Virtual.Vrfs.Vrf, ['vrf_name'], name, value)


            class Address(_Entity_):
                """
                IPv6 address and mask
                
                .. attribute:: address
                
                	IPv6 address
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                	**mandatory**\: True
                
                .. attribute:: prefix_length
                
                	IPv6 address prefix length
                	**type**\: int
                
                	**range:** 0..128
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv6-smiap-cfg'
                _revision = '2016-07-04'

                def __init__(self):
                    if sys.version_info > (3,):
                        super().__init__()
                    else:
                        super(Ipv6Virtual.Vrfs.Vrf.Address, self).__init__()

                    self.yang_name = "address"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                        ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                    ])
                    self.address = None
                    self.prefix_length = None
                    self._segment_path = lambda: "address"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv6Virtual.Vrfs.Vrf.Address, ['address', 'prefix_length'], name, value)

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_smiap_cfg as meta
                    return meta._meta_table['Ipv6Virtual.Vrfs.Vrf.Address']['meta_info']

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_smiap_cfg as meta
                return meta._meta_table['Ipv6Virtual.Vrfs.Vrf']['meta_info']

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_smiap_cfg as meta
            return meta._meta_table['Ipv6Virtual.Vrfs']['meta_info']

    def clone_ptr(self):
        self._top_entity = Ipv6Virtual()
        return self._top_entity

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_smiap_cfg as meta
        return meta._meta_table['Ipv6Virtual']['meta_info']


