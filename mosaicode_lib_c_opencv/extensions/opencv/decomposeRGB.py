#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the DecomposeRGB class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class DecomposeRGB(BlockModel):
    """
    This class contains methods related the DecomposeRGB class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a decomposição RGB de imagens."
        self.label = "Decompose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image1",
                       "label":"Output 1",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image2",
                       "label":"Output 2",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image3",
                       "label":"Output 3",
                       "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        # ------------------C/OpenCv code--------------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat block$id$_img_t0[3];\n' + \
            'Mat $port[output_image1]$;\n' + \
            'Mat $port[output_image2]$;\n' + \
            'Mat $port[output_image3]$;\n'
        
        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            'split($port[input_image]$, block$id$_img_t0);\n' + \
            '$port[output_image1]$ = block$id$_img_t0[0];\n' + \
            '$port[output_image2]$ = block$id$_img_t0[1];\n' + \
            '$port[output_image3]$ = block$id$_img_t0[2];\n}\n'

        self.codes["deallocation"] = \
            'block$id$_img_t0[0].release();\n' + \
            'block$id$_img_t0[1].release();\n' + \
            'block$id$_img_t0[2].release();\n' + \
            '$port[output_image1]$.release();\n' + \
            '$port[output_image2]$.release();\n' + \
            '$port[output_image3]$.release();\n' + \
            '$port[input_image]$.release();\n'

# -----------------------------------------------------------------------------
