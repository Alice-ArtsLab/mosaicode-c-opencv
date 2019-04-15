#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the GetSize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class GetSize(BlockModel):
    """
    This class contains methods related the GetSize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Get Size"
        self.color = "255:217:25:245"
        self.group = "Experimental"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                       {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"output_rect",
                       "label":"Output Rect",
                       "conn_type":"Output"
                       }
                    ]

# ------------------------------C/OpenCv code--------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Rect $port[output_rect]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = Mat::zeros($port[input_image]$.rows, $port[input_image]$.cols, CV_8UC3);
        $port[output_rect]$ = Rect(0, 0, $port[input_image]$.rows, $port[input_image]$.cols);
    }
"""

        self.codes["deallocation"] = \
"""
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------