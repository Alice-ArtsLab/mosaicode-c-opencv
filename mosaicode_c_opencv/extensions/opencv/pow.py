#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Pow class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Pow(BlockModel):
    """
    This class contains methods related the Pow class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Eleva cada ponto de uma " + \
            "imagem a um valor fixo de potência."
        self.label = "Pow"
        self.color = "230:230:60:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.group = "Math Functions"

        self.properties = [{"label": "Exponent",
                            "name": "exponent",
                            "value":1,
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'cvPow($port[input_image]$, $port[output_image]$, $prop[exponent]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'
# -----------------------------------------------------------------------------
