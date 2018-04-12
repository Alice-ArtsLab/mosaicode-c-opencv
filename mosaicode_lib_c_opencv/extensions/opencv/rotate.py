#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Rotate class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Rotate(BlockModel):
    """
    This class contains methods related the Rotate class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Adiciona bordas na imagem."
        self.label = "Rotate Image"
        self.color = "90:5:10:150"
        self.group = "Experimental"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.double",
                       "name":"input_angle",
                       "label":"Angle",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.properties = [{"name": "angle",
                            "label": "Angle",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 360,
                            "step": 1,
                            "value": 90.0
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'double $port[input_angle]$ = $prop[angle]$;\n' + \
            'Mat $port[output_image]$;'

        self.codes["function"] = \
            "#define PI 3.1415926535898\n" + \
            "double rads(double degs){\n" + \
            "return(PI/180 * degs);\n" + \
            "}\n"

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            'Mat temp;\n int H;\n int W;\n' + \
            'W = $port[input_image]$.cols;\n' + \
            'H = $port[input_image]$.rows;\n' + \
            'Point center(W/2.0F, H/2.0F);\n' + \
            'temp = getRotationMatrix2D(center, ' + \
            '$port[input_angle]$, 1.0);\n' + \
            'warpAffine($port[input_image]$, $port[output_image]$, ' + \
            'temp, $port[input_image]$.size());\n' + \
            '}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'
# -----------------------------------------------------------------------------
