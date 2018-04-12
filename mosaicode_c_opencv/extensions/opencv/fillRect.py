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
        self.rect_color = "#0000ffff0000"

        # Appearance
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
                            {"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 1000,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "height",
                            "label": "Height",
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
                            "type": MOSAICODE_COLOR,
                            "value": "#FF0000"
                            }
                           ]

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
            'Rect $port[rect]$($prop[x]$, $prop[y]$, ' + \
            '$prop[width]$, $prop[height]$);\n' + \
            'Mat $port[output_image]$;\n'

        # ----------------------------------------------------------------------
        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '\t$port[output_image]$ = $port[input_image]$.clone();\n' + \
            '\tScalar color = get_scalar_color("$prop[color]$");\n' + \
            '\trectangle($port[output_image]$, $port[rect]$, ' + \
            'color, $prop[line]$, 8, 0);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "$port[input_image]$.release();\n" + \
            "$port[output_image]$.release();\n"
                    
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
