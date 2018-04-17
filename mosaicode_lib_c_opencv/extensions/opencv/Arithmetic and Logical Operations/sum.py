#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Sum class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Sum(BlockModel):
    """
    This class contains methods related the Sum class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Realiza a soma de duas imagens."
        self.label = "Sum"
        self.color = "180:10:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"first_image",
                          "conn_type":"Input",
                          "label":"First Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "conn_type":"Input",
                          "label":"Second Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and Logical Operations"

        self.codes["declaration"] = \
            "Mat $port[first_image]$;\n" + \
            "Mat $port[second_image]$;\n" + \
            "Mat $port[output_image]$;\n"
            
        self.codes["execution"] = \
            'if(!$port[first_image]$.empty() && !$port[second_image]$.empty()){\n' + \
            'Size size$id$($port[first_image]$.cols, $port[first_image]$.rows);\n' + \
            'resize($port[second_image]$, $port[second_image]$, size$id$);\n' + \
            'add($port[first_image]$, $port[second_image]$, ' + \
            '$port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "$port[first_image]$.release();\n" + \
            "$port[second_image]$.release();\n" + \
            "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------
