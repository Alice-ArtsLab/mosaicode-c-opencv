#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Rotate class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Rotate(BlockModel):
    """
    This class contains methods related the Rotate class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Rotate Image"
        self.color = "255:217:25:245"
        self.group = "Experimental"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.double",
                       "name":"input_angle",
                       "label":"Angle",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]
        self.properties = [{"name": "angle",
                            "label": "Angle",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 90.0
                            }
                           ]

# --------------------------------- C/OpenCv Code ------------------------------------
        self.codes["function"] = \
"""        
    #define PI 3.1415926535898
    double rads(double degs){
        return(PI/180 * degs);
    }
"""               

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Mat tmp_$id$;
    double $port[input_angle]$ = $prop[angle]$;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        int W = $port[input_image]$.cols;
        int H = $port[input_image]$.rows;
        Point center(W/2.0F, H/2.0F);
        tmp_$id$ = getRotationMatrix2D(center, $port[input_angle]$, 1.0);
        warpAffine($port[input_image]$, $port[output_image]$, tmp_$id$, $port[input_image]$.size());
    }
"""

        self.codes["deallocation"] = \
"""          
    $port[input_image]$.release();
    $port[output_image]$.release();
    tmp_$id$.release();
"""
    
# -----------------------------------------------------------------------------
