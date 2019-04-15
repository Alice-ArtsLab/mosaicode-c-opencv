#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Not class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Not(BlockModel):
    """
    This class contains methods related the Not class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.label = "Not"
        self.color = "255:102:25:245"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]

#-------------------------------- C/OpenCV Code ---------------------------------                          

        self.group = "Arithmetic and Logical Operations"

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        bitwise_not($port[input_image]$, $port[output_image]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""    

# -----------------------------------------------------------------------------
