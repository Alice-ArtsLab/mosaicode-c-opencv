#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FillRect class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class FillRect(BlockModel):
    """
    This class contains methods related the FillRect class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.language = "c"
        self.framework = "opencv"
        self.help = "Preenche o retângulo de uma cor."
        self.label = "Fill Rectangle"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "conn_type":"Input",
                       "label":"Input Image"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "conn_type":"Input",
                       "label":"Rectangle"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "conn_type":"Output",
                       "name":"output_image",
                       "label":"Output Image"}]
        self.group = "Basic Shapes"
        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "line",
                            "label": "Line",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value": "#FF0000"
                            }
                           ]

#------------------------------------- C/OpenCV Code ----------------------------------

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
            
        return Scalar(bi, gi, ri, 0);\n" + \
    }
"""

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Rect $port[rect]$($prop[x]$, $prop[y]$, $prop[width]$, $prop[height]$);
    Mat $port[output_image]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        Scalar color = get_scalar_color("$prop[color]$");
        rectangle($port[output_image]$, $port[rect]$, color, $prop[line]$, 8, 0);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""                    

# -----------------------------------------------------------------------------
