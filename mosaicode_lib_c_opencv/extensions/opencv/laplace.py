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
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_masksize",
                          "label":"Mask Size"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]
        self.group = "Gradients, Edges and Corners"

        self.properties = [{"label": "Mask Size",
                            "name": "masksize",
                            "type": MOSAICODE_INT,
                            "value": 3,
                            "lower": 1,
                            "upper": 13
                            }
                           ]

        # ------------------------------C/OpenCv code--------------------------

        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'int $port[input_masksize]$ = $prop[masksize]$;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[input_masksize]$ = ($port[input_masksize]$ > 31)? 31 : ' + \
            '$port[input_masksize]$ = ($port[input_masksize]$ % 2 == 0)? ' + \
            '$port[input_masksize]$ + 1 : $port[input_masksize]$;\n' + \
            'cvtColor($port[input_image]$, $port[input_image]$, COLOR_RGB2GRAY);\n' + \
            'Laplacian($port[input_image]$, $port[output_image]$, ' + \
            'CV_16S, $port[input_masksize]$, 1, 0);\n' + \
            'convertScaleAbs($port[output_image]$, $port[output_image]$);\n}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'     
        
# -----------------------------------------------------------------------------
