#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the GetSize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class GetSize(BlockModel):
    """
    This class contains methods related the GetSize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Extracts the input image size."
        self.label = "Get Size"
        self.color = "250:20:30:150"
        self.in_types = ["mosaicode_c_opencv.extensions.ports.image"]
        self.out_types = ["mosaicode_c_opencv.extensions.ports.rect"]
        self.group = "Experimental"
        self.time_shifts = False

        # ------------------------------C/OpenCv code--------------------------
        self.codes[2] = \
            '\nif(block$id$_img_i0)\n{\n' + \
            '  \tblock$id$_rect_o0 = cvRect( 0, 0, ' + \
            'block$id$_img_i0->width, block$id$_img_i0->height);\n' + \
            '}\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
