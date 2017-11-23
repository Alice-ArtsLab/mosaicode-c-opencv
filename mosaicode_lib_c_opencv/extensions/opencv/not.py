#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Not class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Not(BlockModel):
    """
    This class contains methods related the Not class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Realiza a negação lógica de uma imagem. " + \
            "Corresponde à negativa da imagem."
        self.label = "Not"
        self.color = "10:180:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * $port[input_image]$ = NULL;\n" + \
                    "IplImage * $port[output_image]$ = NULL;\n"

        self.codes["execution"] = \
            'if($port[input_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'cvNot($port[input_image]$, $port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&$port[input_image]$);\n" + \
                       "cvReleaseImage(&$port[output_image]$);\n"

# -----------------------------------------------------------------------------
