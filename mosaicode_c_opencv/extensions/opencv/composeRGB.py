#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ComposeRGB class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ComposeRGB(BlockModel):
    """
    This class contains methods related the ComposeRGB class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a composição RGB de várias imagens."
        self.label = "Compose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image1",
                       "label":"Image 1",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image2",
                       "label":"Image 2",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image3",
                       "label":"Image 3",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        # ------------------------C/OpenCv code-------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image1]$;\n' + \
            'Mat $port[input_image2]$;\n' + \
            'Mat $port[input_image3]$;\n' + \
            'Mat block$id$_img_t0[3];\n' + \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image1]$.empty()){\n' + \
            'block$id$_img_t0[0] = $port[input_image1]$;\n' + \
            'block$id$_img_t0[1] = $port[input_image2]$;\n' + \
            'block$id$_img_t0[2] = $port[input_image3]$;\n' + \
            'merge(block$id$_img_t0, 3, $port[output_image]$);\n}\n'

        self.codes["deallocation"] = \
            'block$id$_img_t0[0].release();\n' + \
            'block$id$_img_t0[1].release();\n' + \
            'block$id$_img_t0[2].release();\n' + \
            '$port[output_image]$.release();\n' + \
            '$port[input_image1]$.release();\n' + \
            '$port[input_image2]$.release();\n' + \
            '$port[input_image3]$.release();\n'

# -----------------------------------------------------------------------------
