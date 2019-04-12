#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Color Conversion class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ColorConversion(BlockModel):
    """
    This class contains methods related the ColorConversion class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Color Conversion"
        self.color = "50:125:50:150"
        self.group = "Filters and Conversions"
        self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "input_image",
                       "label": "Input Image",
                       "conn_type": "Input"},
                      {"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "output_image",
                       "label": "Output Image",
                       "conn_type": "Output"}]
        self.properties = [{"name": "conversion_type",
                            "label": "Conversion Type",
                            "type": MOSAICODE_COMBO,
                            "value": 'COLOR_RGB2GRAY',
                            "values": [
                                'COLOR_RGB2GRAY',
                                'COLOR_RGB2YCrCb',
                                'COLOR_YCrCb2RGB',
                                'COLOR_RGB2HSV',
                                'COLOR_HSV2BGR',
                                'COLOR_RGB2HLS',
                                'COLOR_HLS2RGB',
                                'COLOR_RGB2XYZ',
                                'COLOR_XYZ2RGB',
                                'COLOR_RGB2Lab',
                                'COLOR_Lab2RGB',
                                'COLOR_RGB2Luv',
                                'COLOR_Luv2RGB'
                            ]
                            }
                           ]

# -----------------C/OpenCv code ---------------------------

        self.codes["declaration"] =  \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        cvtColor($port[input_image]$, $port[output_image]$, $prop[conversion_type]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""    

# -----------------------------------------------------------------------------
