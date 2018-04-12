#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the CropImage class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class CropImage(BlockModel):
    """
    This class contains methods related the CropImage class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Corta a imagem de acordo com o retângulo de entrada."
        self.label = "Crop Image"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "label":"Rect",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "Experimental"

        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 200
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 200
                            }
                           ]

        # ------------------------C/OpenCv code--------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Rect $port[rect]$(' + \
            '$prop[x]$, $prop[y]$, $prop[width]$, $prop[height]$);\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$($port[rect]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "$port[input_image]$.release();\n" + \
            "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------
