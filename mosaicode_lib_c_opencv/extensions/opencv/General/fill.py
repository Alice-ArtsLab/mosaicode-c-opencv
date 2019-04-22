#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Fill class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Fill(BlockModel):
    """
    This class contains methods related the Fill class.
    """

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Fill image"
        self.color = "0:64:191:220"
        self.group = "General"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]
        self.properties = [{"name": "rect_color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value":"#DDDDDD"
                            }
                           ]

# ----------------------------------- C/OpenCv Code -----------------------------------
        
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;  
"""

        self.codes["function"] = \
"""        
    Scalar get_scalar_color_$id$(const char * rgbColor){
        if (strlen(rgbColor) < 13 || rgbColor[0] != '#')
            return Scalar(0,0,0,0);
        char r[4], g[4], b[4];
        strncpy(r, rgbColor+1, 4);
        strncpy(g, rgbColor+5, 4);
        strncpy(b, rgbColor+9, 4);

        int ri, gi, bi = 0;
        ri = (int)strtol(r, NULL, 16);
        gi = (int)strtol(g, NULL, 16);
        bi = (int)strtol(b, NULL, 16);

        ri /= 257;
        gi /= 257;
        bi /= 257;
            
        return Scalar(bi, gi, ri, 0);
    }
"""  
                
        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        Scalar color = get_scalar_color_$id$("$prop[rect_color]$");
        rectangle($port[input_image]$, Point(0, 0), Point($port[input_image]$.cols, $port[input_image]$.rows), color, CV_FILLED, 1, 0);
        $port[output_image]$ = $port[input_image]$.clone();
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release(); 
"""

# -----------------------------------------------------------------------------