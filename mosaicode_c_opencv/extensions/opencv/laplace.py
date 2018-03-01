#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Laplace class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Laplace(BlockModel):
    """
    This class contains methods related the laplace class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        self.help = "Operação de filtragem que calcula o " + \
            "Laplaciano de uma imagem," + \
            "realçando cantos e bordas de objetos."
        self.label = "Laplace"
        self.color = "250:180:80:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_masksize",
                          "label":"Mask Size"},
                          {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]
        self.group = "Gradients, Edges and Corners"

        self.properties = [{"label": "Mask Size",
                            "name": "masksize",
                            "type": MOSAICODE_COMBO,
                            "value":3,
                            "values": ["1", "3", "5", "7", "9", "11", "13"]
                            }
                           ]

        # ------------------------------C/OpenCv code--------------------------

        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'int $port[input_masksize]$ = $prop[masksize]$;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[input_masksize]$ = ($port[input_masksize]$ > 31)? 31 : ' + \
            '$port[input_masksize]$ = ($port[input_masksize]$ % 2 == 0)? ' + \
            '$port[input_masksize]$ + 1 : $port[input_masksize]$;\n' + \
            'CvSize size$id$ = cvGetSize($port[input_image]$);\n' + \
            '$port[output_image]$ = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_32F, $port[input_image]$->nChannels);\n' + \
            'cvLaplace($port[input_image]$, $port[output_image]$, ' + \
            '$port[input_masksize]$);}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'     
        
# -----------------------------------------------------------------------------
