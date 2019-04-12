#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Smooth class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Smooth(BlockModel):
    """
    This class contains methods related the Smooth class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Smooth"
        self.color = "50:125:50:150"
        self.group = "Filters and Conversions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"input_image",
                      "label":"Input Image",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"input_integer1",
                      "label":"Input Integer 1",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"input_integer2",
                      "label":"Input Integer 2",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"output_image",
                      "label":"Output Image",
                      "conn_type":"Output"}
                      ]
        self.properties = [{"name": "integer1",
                            "label": "Sigma A",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "integer2",
                            "label": "Sigma B",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "type",
                            "label": "Smooth Type",
                            "type": MOSAICODE_COMBO,
                            "value":"Gaussian Blur",
                            "values": ["Gaussian Blur",
                                      "Homogeneous Blur",
                                      "Median Blur"]
                            }
                           ]

#-------------------------------- C/OpenCv Code ------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    int $port[input_integer1]$ = $prop[integer1]$;
    int $port[input_integer2]$ = $prop[integer2]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        $port[input_integer1]$ = ($port[input_integer1]$ %2 == 0)? $port[input_integer1]$ + 1 : $port[input_integer1]$;
        $port[input_integer2]$ = ($port[input_integer2]$ %2 == 0)? $port[input_integer2]$ + 1 : $port[input_integer2]$;
        if("$prop[type]$" == "Gaussian Blur"){
            GaussianBlur($port[input_image]$, $port[output_image]$, Size(0,0), $port[input_integer1]$, $port[input_integer2]$);
        }
        if("$prop[type]$" == "Homogeneous Blur"){
            blur($port[input_image]$, $port[output_image]$, Size($port[input_integer1]$, $port[input_integer2]$), Point(-1,-1));
        }
        if("$prop[type]$" == "Median Blur"){
            medianBlur($port[input_image]$, $port[output_image]$, $port[input_integer1]$);
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""    

# -----------------------------------------------------------------------------
