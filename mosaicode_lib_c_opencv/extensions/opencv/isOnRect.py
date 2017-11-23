#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the IsOnRect class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class IsOnRect(BlockModel):
    """
    This class contains methods related the IsOnRect class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Checks Wheather the given " + \
            "point is inside the given rectangle."
        self.label = "Check Point"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.point",
                       "name":"input0",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"input1",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.double",
                       "name":"output0",
                       "conn_type":"Output"}]
        self.group = "Experimental"

        # ------------------------------C/OpenCv code--------------------------
        self.codes["execution"] = \
            '\n block$id$_double_o0 = 0.0;\n' + \
            'if(block$id$_point_i0.x >= block$id$_rect_i1.x)\n' + \
            '   if(block$id$_point_i0.y >= block$id$_rect_i1.y)\n' + \
            '       if(block$id$_point_i0.x < block$id$_rect_i1.x + ' + \
            'block$id$_rect_i1.width)\n' + \
            '           if(block$id$_point_i0.y < block$id$_rect_i1.y + ' + \
            'block$id$_rect_i1.height)\n' + \
            '               block$id$_double_o0 = 1.0;\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
