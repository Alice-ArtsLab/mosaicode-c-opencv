#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Erode class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Erode(BlockModel):
    """
    This class contains methods related the Erode class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.help = "Operação morfológica que provoca erosão " + \
            "nos objetos de uma imagem, reduzindo suas dimensões."
        self.label = "Erosion"
        self.color = "180:230:220:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"input_image",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.group = "Morphological Operations"

        self.properties = [{"label": "Mask Size X",
                            "name": "masksizex",
                            "type": MOSAICODE_COMBO,
                            "values": ["1", "3", "5", "7"],
                            "value":"3"
                            },
                            {"label": "Mask Size Y",
                            "name": "masksizey",
                            "type": MOSAICODE_COMBO,
                            "values": ["1", "3", "5", "7"],
                            "value":"3"
                            }
                           ]

        # --------------------------C/OpenCv code------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Mat block$id$_arg_mask = ' + \
            'getStructuringElement(MORPH_RECT, Size($prop[masksizex]$ , $prop[masksizey]$), Point(1, 1));\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'erode($port[input_image]$, $port[output_image]$, ' + \
            'block$id$_arg_mask);\n' + \
            '}\n'

        self.codes["deallocation"] =  \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'

# -----------------------------------------------------------------------------
