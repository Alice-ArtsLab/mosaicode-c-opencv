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
        self.masksize = "3x3"
        self.iterations = 1

        # Appearance
        self.help = "Operação morfológica que provoca erosão " + \
            "nos objetos de uma imagem, reduzindo suas dimensões."
        self.label = "Erosion"
        self.color = "180:230:220:150"
        self.in_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "label":"Input Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "name":"interaction",
                          "label":"Interactions"}
                         ]
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
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
                            },
                           {"name": "Iterations",
                            "label": "iterations",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # --------------------------C/OpenCv code------------------------------
        self.codes[1] = \
            'IplImage * block$id$_img_i0 = NULL; // ERODE input\n' + \
            'int block$id$_int_i1 = $prop[iterations]$; // ERODE iterarions\n' + \
            'IplImage * block$id$_img_o0 = NULL; // ERODE output\n' + \
            'IplConvKernel * block$id$_arg_mask = ' + \
            'cvCreateStructuringElementEx($prop[masksizex]$ , $prop[masksizey]$, 1, 1,CV_SHAPE_RECT,NULL);\n'

        self.codes[2] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'cvErode(block$id$_img_i0, block$id$_img_o0, ' + \
            'block$id$_arg_mask, block$id$_int_i1);\n' + \
            '}\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
