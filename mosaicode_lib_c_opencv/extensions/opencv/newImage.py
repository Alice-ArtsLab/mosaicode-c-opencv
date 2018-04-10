#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewImage class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewImage(BlockModel):
    """
    This class contains methods related the NewImage class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Cria uma nova imagem."
        self.label = "New Image"
        self.color = "50:100:200:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Image Source"

        self.properties = [{"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":800
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":600
                            }
                           ]

        self.codes["declaration"] = \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            'Size size$id$($prop[width]$, $prop[height]$);\n' + \
            'Mat $port[output_image]$(size$id$, CV_8UC1);\n' + \
            'zeros($port[output_image]$.rows, $port[output_image]$.cols, ' + \
            'CV_8UC1);\n'

        self.codes["deallocation"] = "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------
