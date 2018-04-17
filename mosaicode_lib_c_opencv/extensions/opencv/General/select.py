#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Select class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Select(BlockModel):
    """
    This class contains methods related the Select class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        self.help = "Select between two images."
        self.label = "Select"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image1",
                          "label":"First Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image2",
                          "label":"Second Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "label":"Output Image",
                          "conn_type":"Output"}]

        self.group = "General"

        self.properties = [{"name": "key",
                            "label": "Key",
                            "type": MOSAICODE_COMBO,
                            "value": "IMAGEM 1",
                            "values": ["IMAGEM 1",
                            "IMAGEM 2"]
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
            'Mat $port[input_image1]$;\n' + \
            'Mat $port[input_image2]$;\n' + \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            'if(!$port[input_image1]$.empty() && !$port[input_image2]$.empty()){\n' + \
            'if("$prop[key]$" == "IMAGEM 1")\n' + \
            '\t$port[output_image]$ = $port[input_image1]$.clone();\n' + \
            'else\n' + \
            '\t$port[output_image]$ = $port[input_image2]$.clone();\n' + \
            '}\n'

        self.codes["deallocation"] = \
            '$port[input_image1]$.release();\n' + \
            '$port[input_image2]$.release();\n' + \
            '$port[output_image]$.release();\n'     

# -----------------------------------------------------------------------------
