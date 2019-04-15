#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Ellipse class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Ellipse(BlockModel):
    """
    This class contains methods related the Ellipse class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Ellipse"
        self.color = "166:123:91:255"
        self.group = "Basic Shapes"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "conn_type":"Input",
                       "label":"Input Image"},
                       {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"input_rects",
                       "conn_type":"Input",
                       "label":"Input Rects"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "conn_type":"Output",
                       "name":"output_image",
                       "label":"Output Image"}]
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
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 10000.0,
                            "step": 1.0,
                            "value": 1.0
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0.0,
                            "upper": 10000.0,
                            "step": 1.0,
                            "value": 1.0
                            },
                            {"name": "angle",
                            "label": "Angle",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 0
                            },
                            {"name": "start_angle",
                            "label": "Start angle",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 0
                            },
                            {"name": "end_angle",
                            "label": "End angle",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 360
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
                    ellipse($port[output_image]$, Point($port[input_rects]$[i].x, $port[input_rects]$[i].y), Size($port[input_rects]$[i].width, $port[input_rects]$[i].height), $prop[angle]$, $prop[start_angle]$, $prop[end_angle]$, color, $prop[line]$, 8);
                }
            }
            else{
                for(int i = 0; i < $port[input_rects]$.size(); i++){
                    ellipse($port[output_image]$, Point($port[input_rects]$[i].x, $port[input_rects]$[i].y), Size($port[input_rects]$[i].width, $port[input_rects]$[i].height), $prop[angle]$, $prop[start_angle]$, $prop[end_angle]$, color, -1, 8);
                }
            }
        }
        else{ 
            if("$prop[fill]$" == "NO"){
                ellipse($port[output_image]$, Point($prop[x]$, $prop[y]$), Size($prop[width]$, $prop[height]$), $prop[angle]$, $prop[start_angle]$, $prop[end_angle]$, color, $prop[line]$, 8);
            }
            else{
                ellipse($port[output_image]$, Point($prop[x]$, $prop[y]$), Size($prop[width]$, $prop[height]$), $prop[angle]$, $prop[start_angle]$, $prop[end_angle]$, color, -1, 8);
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
