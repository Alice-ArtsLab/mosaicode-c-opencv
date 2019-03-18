#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ComposeRGB class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ComposeRGB(BlockModel):
    """
    This class contains methods related the ComposeRGB class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Compose RGB"
        self.color = "50:125:50:150"
        self.group = "Filters and Color Conversion"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image1",
                       "label":"Image 1",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image2",
                       "label":"Image 2",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image3",
                       "label":"Image 3",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

# ------------------------------ C/OpenCv Code ---------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image1]$;
    Mat $port[input_image2]$;
    Mat $port[input_image3]$;
    Mat tmp_$id$[3];
    Mat $port[output_image]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image1]$.empty()){
        tmp_$id$[0] = $port[input_image1]$;
        tmp_$id$[1] = $port[input_image2]$;
        tmp_$id$[2] = $port[input_image3]$;
        merge(tmp_$id$, 3, $port[output_image]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    tmp_$id$[0].release();
    tmp_$id$[1].release();
    tmp_$id$[2].release();
    $port[output_image]$.release();
    $port[input_image1]$.release();
    $port[input_image2]$.release();
    $port[input_image3]$.release();
"""    

# -----------------------------------------------------------------------------
