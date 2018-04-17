#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Resize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Resize(BlockModel):
    """
    This class contains methods related the Resize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Resizes the input image to the " + \
            "dimensions of the input rectangle."
        self.label = "Resize Image"
        self.color = "20:80:10:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]

        self.group = "Experimental"

        self.properties = [{"label": "Tamanho em X",
                            "name": "size_x",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000
                            },
                            {"label": "Tamanho em Y",
                            "name": "size_y",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000
                            }
                           ]

        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Size size$id$;\n' 

        self.codes["execution"] = \
            'if(!$port[input_image]$.empty()){\n' + \
            'size$id$ = Size($prop[size_x]$,' + \
            '$prop[size_y]$);\n' + \
            'resize($port[input_image]$, $port[output_image]$, size$id$);\n' + \
            '}\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
