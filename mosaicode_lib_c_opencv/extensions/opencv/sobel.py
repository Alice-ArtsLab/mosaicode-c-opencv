#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Sobel class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Sobel(BlockModel):
    """
    This class contains methods related the Sobel class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Operação de filtragem que utiliza uma máscara " + \
            "Sobel para realçar cantos e bordas da imagem."
        self.label = "Sobel"
        self.color = "250:180:80:150"
        self.in_types = [""]
        self.out_types = []
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                        {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"output_image",
                        "label":"Output Image",
                        "conn_type":"Output"}]

        self.group = "Gradients, Edges and Corners"

        self.properties = [{"name": "xorder",
                            "label": "X Axis Derivate Order",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 6,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "yorder",
                            "label": "Y Axis Derivate Order",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 6,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "masksize",
                            "label": "Mask Size",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 7,
                            "step": 2,
                            "value": 3
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            'CvSize size$id$ = cvGetSize($port[input_image]$);\n' + \
            '$port[output_image]$ = cvCreateImage(size$id$, ' + \
            'IPL_DEPTH_32F, $port[input_image]$->nChannels);\n' + \
            'cvSobel($port[input_image]$, $port[output_image]$, ' + \
            '$prop[xorder]$, $prop[yorder]$, $prop[masksize]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[output_image]$);\n' + \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'

# -----------------------------------------------------------------------------
