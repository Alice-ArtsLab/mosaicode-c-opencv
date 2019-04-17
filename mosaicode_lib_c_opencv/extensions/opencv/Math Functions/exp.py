#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Exp class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Exp(BlockModel):
    """
    This class contains methods related the Exp class.
    """

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Exp"
        self.color = "179:255:25:245"
        self.group = "Math Functions"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"input_image",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

# --------------------------C/OpenCv code------------------------------

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
        exp(tmp_$id$, tmp_$id$);
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
