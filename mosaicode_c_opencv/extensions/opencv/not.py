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
        self.in_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "label":"Input Image"}
                         ]
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * $in_ports[input_image]$ = NULL;\n" + \
                    "IplImage * $out_ports[output_image]$ = NULL;\n"

        self.codes["execution"] = \
            'if($in_ports[input_image]$){\n' + \
            '$out_ports[output_image]$ = cvCloneImage($in_ports[input_image]$);\n' + \
            'cvNot($in_ports[input_image]$, $out_ports[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&$in_ports[input_image]$);\n" + \
                       "cvReleaseImage(&$out_ports[output_image]$);\n"


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
