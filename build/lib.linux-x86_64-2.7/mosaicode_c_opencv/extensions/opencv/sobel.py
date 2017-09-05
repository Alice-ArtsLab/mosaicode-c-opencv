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
        self.masksize = 3
        self.xorder = 1
        self.yorder = 1

        # Appearance
        self.help = "Operação de filtragem que utiliza uma máscara " + \
            "Sobel para realçar cantos e bordas da imagem."
        self.label = "Sobel"
        self.color = "250:180:80:150"
        self.in_types = ["mosaicode_c_opencv.extensions.ports.image"]
        self.out_types = ["mosaicode_c_opencv.extensions.ports.image"]
        self.group = "Gradients, Edges and Corners"

        self.properties = [{"name": "X Axis Derivate Order",
                            "label": "xorder",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 6,
                            "step": 1
                            },
                           {"name": "Y Axis Derivate Order",
                            "label": "yorder",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 6,
                            "step": 1
                            },
                           {"name": "Mask Size",
                            "label": "masksize",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 7,
                            "step": 2
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'CvSize size$id$ = cvGetSize(block$id$_img_i0);\n' + \
            'block$id$_img_o0 = cvCreateImage(size$id$, ' + \
            'IPL_DEPTH_32F,block$id$_img_i0->nChannels);\n' + \
            'cvSobel(block$id$_img_i0, block$id$_img_o0, ' + \
            '$xorder$, $yorder$, $masksize$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
