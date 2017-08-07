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
        self.in_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "label":"Input Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "name":"border_size",
                          "label":"Border Size"}
                         ]
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
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
                            "value":"IPL_BORDER_CONSTANT",
                            "values": ["IPL_BORDER_CONSTANT",
                                       "IPL_BORDER_REPLICATE",
                                       "IPL_BORDER_REFLECT",
                                       "IPL_BORDER_WRAP"]
                            },
                           {"label": "Border Size",
                            "name": "border_size",
                            "type": MOSAICODE_INT,
                            "value":"50"
                            }
                           ]

        self.codes["function"] = \
            "CvScalar get_scalar_color(const char * rgbColor){\n" + \
            "   if (strlen(rgbColor) < 13 || rgbColor[0] != '#')\n" + \
            "       return cvScalar(0,0,0,0);\n" + \
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
            "   return cvScalar(bi, gi, ri, 0);\n" + \
            "}\n"

        self.codes["declaration"] = \
            "IplImage * block$id$_img_i0 = NULL;\n" + \
            "int block$id$_int_i1 = $prop[border_size]$;\n" + \
            "IplImage * block$id$_img_o0 = NULL;\n"

        self.codes["execution"] = \
            'if(block$id$_img_i0){\n' + \
            '\tCvSize size$id$ = cvSize(block$id$_img_i0->width +' + \
            ' block$id$_int_i1 * 2, block$id$_img_i0->height' + \
            ' + block$id$_int_i1 * 2);\n' + \
            '\tblock$id$_img_o0 = cvCreateImage(size$id$,' + \
            ' block$id$_img_i0->depth,block$id$_img_i0->nChannels);\n' + \
            '\tCvPoint point$id$ = cvPoint' + \
            '(block$id$_int_i1, block$id$_int_i1);\n' + \
            '\tCvScalar color = get_scalar_color("$prop[color]$");\n' + \
            '\tcvCopyMakeBorder(block$id$_img_i0, block$id$_img_o0,' + \
            ' point$id$, $prop[type]$, color);\n' + \
            '}\n'
# -----------------------------------------------------------------------------
