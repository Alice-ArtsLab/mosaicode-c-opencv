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
        self.label = "Circle"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "conn_type":"Input",
                       "label":"Input Image"},
                       {"type":"mosaicode_lib_c_opencv.extensions.ports.rects",
                       "name":"input_rects",
                       "conn_type":"Input",
                       "label":"Input Rects"},
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
                            {"name": "radius",
                            "label": "Radius",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 10000.0,
                            "step": 1.0,
                            "value": 1.0
                            },
                            {"name": "line",
                            "label": "Line",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value": "#FF0000"
                            },
                            {"name": "fill",
                            "label": "Fill",
                            "type": MOSAICODE_COMBO,
                            "value": 'NO',
                            "values": [
                                    'YES',
                                    'NO'
                            ]
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
    vector<Rect> $port[input_rects]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        Scalar color = get_scalar_color$id$("$prop[color]$");
        if(!$port[input_rects]$.empty()){
            if("$prop[fill]$" == "NO"){
                for(int i = 0; i < $port[input_rects]$.size(); i++){
                    circle($port[output_image]$, Point($port[input_rects]$[i].x, $port[input_rects]$[i].y), $prop[radius]$, color, $prop[line]$, 8);
                }
            }
            else{
                for(int i = 0; i < $port[input_rects]$.size(); i++){
                    circle($port[output_image]$, Point($port[input_rects]$[i].x, $port[input_rects]$[i].y), $prop[radius]$, color, -1, 8);
                }
            }
        }
        else{ 
            if("$prop[fill]$" == "NO"){
                circle($port[output_image]$, Point($prop[x]$, $prop[y]$), $prop[radius]$, color, $prop[line]$, 8);
            }
            else{
                circle($port[output_image]$, Point($prop[x]$, $prop[y]$), $prop[radius]$, color, -1, 8);
            }
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""                    

# -----------------------------------------------------------------------------
