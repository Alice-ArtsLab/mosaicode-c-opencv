#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Contours class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Contours(BlockModel):
    """
    This class contains methods related the Contours class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Contours"
        self.color = "50:100:200:150"
        self.group = "Basic Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "conn_type":"Input",
                       "label":"Input Image"},
                       {"type":"mosaicode_lib_c_opencv.extensions.ports.point",
                       "name":"input_points",
                       "conn_type":"Input",
                       "label":"Input Points"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "conn_type":"Output",
                       "name":"output_image",
                       "label":"Output Image"}]
        self.properties = [{"name": "color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value": "#FF0000"
                            },
                            {"label": "Thickness",
                            "name": "thickness",
                            "type": MOSAICODE_INT,
                            "value": 2,
                            "step": 1,
                            "upper": 20,
                            "lower": 1
                            }
                           ]

#------------------------------------- C/OpenCV Code ----------------------------------

        self.codes["function"] = \
"""        
    Scalar get_scalar_color$id$(const char * rgbColor){
        if(strlen(rgbColor) < 13 || rgbColor[0] != '#')
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

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    vector<vector<Point> > $port[input_points]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        for(int i = 0; i < $port[input_points]$.size(); i++){
            drawContours($port[output_image]$, $port[input_points]$, i, get_scalar_color("$prop[color]$"), $prop[thickness]$, 8);
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""                    

# -----------------------------------------------------------------------------
