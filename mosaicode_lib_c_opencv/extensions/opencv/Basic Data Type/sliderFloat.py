#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Slider class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class FloatSlider(BlockModel):
    """
    This class contains methods related the Slider class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Creates Slider to float value."
        self.label = "Float Slider"
        self.color = "50:50:200:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.float",
                        "conn_type":"Output",
                        "name":"slider_Fvalue",
                        "label":"Slider Value"}
                        ]
        self.group = "Basic Data Type"
        self.properties = [{"label": "Value",
                            "name": "floatVal",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 10000.0,
                            "step": 0.1,
                            "value":0.0
                            },
                           {"label": "Max Value",
                            "name": "maxVal",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 10000.0,
                            "step": 0.1,
                            "value":0.0
                            },
                           {"label": "Label",
                            "name": "label",
                            "type": MOSAICODE_STRING,
                            "value":"label"
                            },
                           {"label": "Window Title",
                            "name": "window_name",
                            "type": MOSAICODE_STRING,
                            "value":"My Image"
                            }
                           ]

# -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
"""        
    float $port[slider_Fvalue]$ = $prop[floatVal]$;
"""    

        self.codes["execution"] = \
"""        
    namedWindow("$prop[window_name]$", WINDOW_AUTOSIZE );
    createTrackbar("$prop[label]$", "$prop[window_name]$", &$port[slider_Fvalue]$, $prop[maxVal]$, NULL);
"""
    
# -----------------------------------------------------------------------------
