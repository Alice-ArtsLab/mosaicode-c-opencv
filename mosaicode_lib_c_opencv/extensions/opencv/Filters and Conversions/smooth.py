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
        self.color = "230:0:50:245"
        self.group = "Filters and Conversions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"input_image",
                      "label":"Input Image",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"ksizex",
                      "label":"Kernel X Size",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"ksizey",
                      "label":"Kernel Y Size",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"output_image",
                      "label":"Output Image",
                      "conn_type":"Output"}
                      ]
        self.properties = [{"name": "type",
                            "label": "Smooth Type",
                            "type": MOSAICODE_COMBO,
                            "value":"Gaussian Blur",
                            "values": ["Gaussian Blur",
                                      "Average Blur",
                                      "Median Blur",
                                      "Bilateral Filter"]
                            },
                            {"name": "ksizex",
                            "label": "Kernel X Size",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 3
                            },
                           {"name": "ksizey",
                            "label": "Kernel Y Size",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 3
                            },
                            {"name": "sigma1",
                            "label": "Sigma A",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 150,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "sigma2",
                            "label": "Sigma B",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 150,
                            "step": 1,
                            "value": 1
                            }
                           ]

#-------------------------------- C/OpenCv Code ------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    int $port[ksizex]$ = $prop[ksizex]$;
    int $port[ksizey]$ = $prop[ksizey]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        $port[ksizex]$ = ($port[ksizex]$ %2 == 0)? $port[ksizex]$ + 1 : $port[ksizex]$;
        $port[ksizey]$ = ($port[ksizey]$ %2 == 0)? $port[ksizey]$ + 1 : $port[ksizey]$;
        if("$prop[type]$" == "Average Blur"){
            blur($port[input_image]$, $port[output_image]$, Size($port[ksizex]$, $port[ksizey]$), Point(-1,-1));
        }
        if("$prop[type]$" == "Gaussian Blur"){
            GaussianBlur($port[input_image]$, $port[output_image]$, Size($port[ksizex]$, $port[ksizey]$), $prop[sigma1]$, $prop[sigma2]$);
        }
        if("$prop[type]$" == "Median Blur"){
            medianBlur($port[input_image]$, $port[output_image]$, $port[ksizex]$);
        }
        if("$prop[type]$" == "Bilateral Filter"){
            bilateralFilter($port[input_image]$, $port[output_image]$, $prop[sigma1]$, $prop[sigma1]$*2, $prop[sigma1]$/2 );
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""    

# -----------------------------------------------------------------------------
