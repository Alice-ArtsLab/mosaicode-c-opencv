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

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Extracts the input image size."
        self.label = "Get Size"
        self.color = "250:20:30:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "label":"Output Rect",
                       "conn_type":"Output"}]

        self.group = "Experimental"

        # ------------------------------C/OpenCv code--------------------------

        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' 

        self.codes["execution"] = \
            '\nif($port[input_image]$)\n{\n' + \
            '  \t$port[rect]$ = Rect( 0, 0, ' + \
            '$port[input_image]$.cols, $port[input_image]$.rows);\n' + \
            '}\n'
# -----------------------------------------------------------------------------
