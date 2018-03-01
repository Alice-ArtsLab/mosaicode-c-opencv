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

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Checks Wheather the given " + \
            "point is inside the given rectangle."
        self.label = "Check Point"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.point",
                       "name":"point",
                       "label":"Point",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "label":"Rect",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.double",
                       "name":"double",
                       "label":"Double",
                       "conn_type":"Output"}]

        self.group = "Experimental"

        # ------------------------------C/OpenCv code--------------------------
        self.codes["execution"] = \
            '\n $port[double]$ = 0.0;\n' + \
            'if($port[point]$.x >= $port[rect]$.x)\n' + \
            '   if($port[point]$.y >= $port[rect]$.y)\n' + \
            '       if($port[point]$.x < $port[rect]$.x + ' + \
            '$port[rect]$.width)\n' + \
            '           if($port[point]$.y < $port[rect]$.y + ' + \
            '$port[rect]$.height)\n' + \
            '               $port[double]$ = 1.0;\n'

# -----------------------------------------------------------------------------
