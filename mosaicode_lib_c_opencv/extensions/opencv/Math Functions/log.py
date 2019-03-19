#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Log class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Log(BlockModel):
    """
    This class contains methods related the Log class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Log"
        self.color = "230:230:60:150"
        self.group = "Math Functions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

# ------------------------------C/OpenCv code--------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Mat tmp_$id$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        cvtColor($port[input_image]$, tmp_$id$, COLOR_RGB2GRAY);
        tmp_$id$.convertTo(tmp_$id$, CV_32F);
        tmp_$id$ = tmp_$id$ + 1;
        log(tmp_$id$, tmp_$id$);
        convertScaleAbs(tmp_$id$, tmp_$id$);
        normalize(tmp_$id$, $port[output_image]$, 0, 255, NORM_MINMAX);
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
    tmp_$id$.release();
"""

# -----------------------------------------------------------------------------
