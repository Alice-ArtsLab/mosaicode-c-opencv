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

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Desenha Circulos."
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
        
        # -----------------C/OpenCv code ---------------------------

        self.codes["function"] = \
            "Scalar get_scalar_color(const char * rgbColor){\n" + \
            "   if (strlen(rgbColor) < 13 || rgbColor[0] != '#')\n" + \
            "       return Scalar(0,0,0,0);\n" + \
            "   char r[4], g[4], b[4];\n" + \
            "   strncpy(r, rgbColor+1, 4);\n" + \
            "   strncpy(g, rgbColor+5, 4);\n" + \
            "   strncpy(b, rgbColor+9, 4);\n" + \
            "\n" + \
            "   int ri, gi, bi = 0;\n" + \
            "   ri = (int)strtol(r, NULL, 16);\n" + \
            "   gi = (int)strtol(g, NULL, 16);\n" + \
            "   bi = (int)strtol(b, NULL, 16);\n" + \
            "\n" + \
            "   ri /= 257;\n" + \
            "   gi /= 257;\n" + \
            "   bi /= 257;\n" + \
            "   \n" + \
            "   return Scalar(bi, gi, ri, 0);\n" + \
            "}\n"
        
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'int $port[input_radius]$ = $prop[radius]$;\n' + \
            'int $port[input_x]$ = $prop[x]$;\n' + \
            'int $port[input_y]$ = $prop[y]$;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            'Point center = Point($port[input_x]$, $port[input_y]$);\n' + \
            'Scalar color = get_scalar_color("$prop[color]$");\n' + \
            'circle($port[input_image]$, center, $port[input_radius]$, color, $prop[line]$, 8, 0);\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n}\n'

        self.codes["deallocation"] = \
            "$port[input_image]$.release();\n" + \
            "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------
