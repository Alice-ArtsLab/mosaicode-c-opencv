#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Circle class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Circle(BlockModel):
    """
    This class contains methods related the Circle class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.language = "c"
        self.framework = "opencv"
        self.help = "Desenha círculos."
        self.label = "Circle"
        self.color = "255:0:0:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
			           "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                       "name":"input_x",
			           "label":"X",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                       "name":"input_y",
			           "label":"Y",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                       "name":"input_radius",
			           "label":"Radius",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
			           "label":"Output Image",
                       "conn_type":"Output"}]
        self.group = "Basic Shapes"
        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "line",
                            "label": "Line",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "color",
                            "label": "Color",
                            "value":"#FF0000",
                            "type": MOSAICODE_COLOR
                            }
                           ]
        
# --------------------------------C/OpenCv code --------------------------------------

        self.codes["function"] = \
"""        
    Scalar get_scalar_color(const char * rgbColor){
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
        
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    int $port[input_radius]$ = $prop[radius]$;
    int $port[input_x]$ = $prop[x]$;
    int $port[input_y]$ = $prop[y]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        Point center = Point($port[input_x]$, $port[input_y]$);
        Scalar color = get_scalar_color("$prop[color]$");
        circle($port[input_image]$, center, $port[input_radius]$, color, $prop[line]$, 8, 0);
        $port[output_image]$ = $port[input_image]$.clone();
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""    

# -----------------------------------------------------------------------------
