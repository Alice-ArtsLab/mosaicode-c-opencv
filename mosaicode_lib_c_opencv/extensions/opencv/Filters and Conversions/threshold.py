#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Threshold class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Threshold(BlockModel):
    """
    This class contains methods related the Threshold class.
    """
    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Threshold"
        self.color = "230:0:50:245"
        self.group = "Filters and Conversions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"output_image",
                        "label":"Output Image",
                        "conn_type":"Output"}]
        self.properties = [{"name": "threshold",
                            "label": "Threshold",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 255,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "value",
                            "label": "Gray max value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 255,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "type",
                            "label": "Threshold Type",
                            "type": MOSAICODE_COMBO,
                            "value":"THRESH_BINARY",
                            "values": ["THRESH_BINARY",
                                       "THRESH_BINARY_INV",
                                       "THRESH_TRUNC",
                                       "THRESH_TOZERO",
                                       "THRESH_TOZERO_INV",
                                       "THRESH_MASK",
                                       "THRESH_OTSU",
                                       "THRESH_TRIANGLE"]
                            }
                           ]

# -------------------------------- C/OpenCv code ------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        threshold($port[input_image]$, $port[output_image]$, $prop[threshold]$, $prop[value]$, $prop[type]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------