#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Text class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Text(BlockModel):
    """
    This class contains methods related the Text class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Text"
        self.color = "255:217:25:245"
        self.group = "Experimental"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "conn_type":"Input",
                       "label":"Input Image"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "conn_type":"Output",
                       "name":"output_image",
                       "label":"Output Image"}]
        self.properties = [{"name": "text",
                            "label": "Text",
                            "type": MOSAICODE_STRING,
                            "value": ''
                            },
                            {"name": "x",
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
                            {"name": "font_face",
                            "label": "Font face",
                            "type": MOSAICODE_COMBO,
                            "value": 'FONT_HERSHEY_SIMPLEX',
                            "values": [
                                'FONT_HERSHEY_SIMPLEX',
                                'FONT_HERSHEY_PLAIN',
                                'FONT_HERSHEY_DUPLEX',
                                'FONT_HERSHEY_COMPLEX',
                                'FONT_HERSHEY_TRIPLEX',
                                'FONT_HERSHEY_COMPLEX_SMALL',
                                'FONT_HERSHEY_SCRIPT_SIMPLEX',
                                'FONT_HERSHEY_SCRIPT_COMPLEX',
                                'FONT_HERSHEY_ITALIC'
                            ]
                            },
                           {"name": "font_scale",
                            "label": "Font scale",
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
                            }
                           ]

#------------------------------------- C/OpenCV Code ----------------------------------

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

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""            

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        Scalar color = get_scalar_color_$id$("$prop[color]$");
        putText($port[output_image]$, "$prop[text]$", Point($prop[x]$, $prop[y]$), $prop[font_face]$, $prop[font_scale]$, color, $prop[line]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""                    

# -----------------------------------------------------------------------------
