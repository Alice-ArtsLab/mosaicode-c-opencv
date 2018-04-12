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
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Preenche toda a imagem de uma cor."
        self.label = "Fill image"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "General"
        
        self.properties = [{"name": "rect_color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value":"#DDDDDD"
                            }
                           ]

        # ------------------------------C/OpenCv code--------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n'  

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
                
        self.codes["execution"] = \
            'if(!$port[input_image]$.empty()){\n' + \
            'Scalar color = get_scalar_color("$prop[rect_color]$");\n' + \
            '\trectangle($port[input_image]$, Point(0, 0), Point($port[input_image]$.cols, ' + \
            '$port[input_image]$.rows), color, CV_FILLED, 1, 0);\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            '}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n' 

# -----------------------------------------------------------------------------
