#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Threshold class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Threshold(BlockModel):
    """
    This class contains methods related the Threshold class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Operador de binarização da imagem, de acordo " + \
            "com um valor fixo de intensidade luminosa (valor de limiar)."
        self.label = "Threshold"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"output_image",
                        "label":"Output Image",
                        "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        self.properties = [{"name": "threshold",
                            "label": "Threshold",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 255,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "value",
                            "label": "Gray max value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 255,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "type",
                            "label": "Threshold Type",
                            "type": MOSAICODE_COMBO,
                            "value":"THRESH_BINARY",
                            "values": ["THRESH_BINARY",
                                       "THRESH_BINARY_INV",
                                       "THRESH_TRUNC",
                                       "THRESH_TOZERO",
                                       "THRESH_TOZERO_INV"]
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'threshold($port[input_image]$, $port[output_image]$, ' + \
            '$prop[threshold]$, $prop[value]$, $prop[type]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'
# -----------------------------------------------------------------------------
