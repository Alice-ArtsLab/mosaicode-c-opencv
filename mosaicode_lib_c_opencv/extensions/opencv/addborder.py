#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the AddBorder class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class AddBorder(BlockModel):
    """
    This class contains methods related the AddBorder class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.help = "Adiciona bordas na imagem."
        self.label = "Add Border"
        self.color = "0:180:210:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                    "name":"input_image",
                    "conn_type":"Input",
                    "label":"Input Image"},
                    {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                    "name":"border_size",
                    "conn_type":"Input",
                    "label":"Border Size"},
                    {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                    "name":"output_image",
                    "conn_type":"Output",
                    "label":"Output Image"}]
        self.group = "Experimental"

        self.properties = [{"label": "Color",
                            "name": "color",
                            "type": MOSAICODE_COLOR,
                            "value":"#FF0000"
                            },
                           {"name": "type",
                            "label": "Type",
                            "type": MOSAICODE_COMBO,
                            "value":"BORDER_CONSTANT",
                            "values": ["BORDER_CONSTANT",
                                       "BORDER_REPLICATE",]
                            },
                           {"label": "Border Size",
                            "name": "border_size",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "step": 1,
                            "upper": 100,
                            "lower": 1
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
            "Mat $port[input_image]$;\n" + \
            "int $port[border_size]$ = $prop[border_size]$;\n" + \
            "Mat $port[output_image]$;\n"

        self.codes["execution"] = \
            'if(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            '\tScalar color = get_scalar_color("$prop[color]$");\n' + \
            '\tcopyMakeBorder($port[input_image]$, $port[output_image]$,' + \
            '$port[border_size]$, $port[border_size]$, $port[border_size]$, ' + \
            '$port[border_size]$, $prop[type]$, color);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "$port[input_image]$.release();\n" + \
            "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------
