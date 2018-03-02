#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Opening class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Opening(BlockModel):
    """
    This class contains methods related the Opening class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Operação morfológica que visa " + \
            "desconectar objetos em uma imagem ou suprimir ruídos."
        self.label = "Opening"
        self.color = "180:230:220:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
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

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplConvKernel * block$id$_arg_mask = cvCreateStructuringElementEx($prop[masksizex]$ , $prop[masksizey]$, 1, 1,CV_SHAPE_RECT,NULL);\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            'IplImage * block$id$_auxImg;' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'block$id$_auxImg = cvCloneImage($port[input_image]$);\n' + \
            'cvMorphologyEx($port[input_image]$, $port[output_image]$, NULL,' + \
            'block$id$_arg_mask, CV_MOP_OPEN, 1);\n}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseStructuringElement(&block$id$_arg_mask);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'
# -----------------------------------------------------------------------------
