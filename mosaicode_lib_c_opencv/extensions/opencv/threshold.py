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
                            "step": 1
                            },
                           {"name": "value",
                            "label": "Gray max value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 255,
                            "step": 1
                            },
                           {"name": "type",
                            "label": "Threshold Type",
                            "type": MOSAICODE_COMBO,
                            "values": ["CV_THRESH_BINARY",
                                       "CV_THRESH_BINARY_INV",
                                       "CV_THRESH_TRUNC",
                                       "CV_THRESH_TOZERO",
                                       "CV_THRESH_TOZERO_INV"]
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'cvThreshold($port[input_image]$, $port[output_image]$, ' + \
            '$prop[threshold]$, $prop[value]$, $prop[type]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'
# -----------------------------------------------------------------------------
