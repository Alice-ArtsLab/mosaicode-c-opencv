#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Smooth class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Smooth(BlockModel):
    """
    This class contains methods related the Smooth class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Aplicação de um filtro de suavização. " + \
            "Suaviza os contornos de objetos na imagem, borrando-os levemente."
        self.label = "Smooth"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                      "name":"input_image",
                      "label":"Input Image",
                      "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.int",
                      "name":"input_integer",
                      "label":"Input Integer",
                      "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                      "name":"output_image",
                      "label":"Output Image",
                      "conn_type":"Output"},
                      {"type":"mosaicode_c_opencv.extensions.ports.int",
                      "name":"output_integer1",
                      "label":"Output integer 1",
                      "conn_type":"Output"},
                      {"type":"mosaicode_c_opencv.extensions.ports.int",
                      "name":"output_integer2",
                      "label":"Output integer 2",
                      "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        self.properties = [{"name": "type",
                            "label": "smooth_type",
                            "type": MOSAICODE_COMBO,
                            "values": ["CV_GAUSSIAN", "CV_BLUR", "CV_MEDIAN"],
                            "step":"CV_GAUSSIAN"
                            },
                           {"name": "integer1",
                            "label": "Integer 1",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1
                            },
                           {"name": "integer2",
                            "label": "Integer 2",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'int $port[input_integer]$ = $prop[integer1]$;\n' + \
            'int block$id$_int_i2 = $prop[integer2]$;\n' + \
            'IplImage * $port[output]$ = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input]$){\n' + \
            '$port[output]$ = cvCloneImage($port[input]$);\n' + \
            '$port[integer]$ = ($port[integer]$ %2 == 0)? ' + \
            '$port[integer]$ + 1 : $port[integer]$;\n' + \
            'block$id$_int_i2 = (block$id$_int_i2 %2 == 0)? ' + \
            'block$id$_int_i2 + 1 : block$id$_int_i2;\n' + \
            'cvSmooth($port[input]$, $port[output]$, ' + \
            '$smooth_type$,$port[integer]$,block$id$_int_i2,0,0);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
