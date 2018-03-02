#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Select class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Select(BlockModel):
    """
    This class contains methods related the Select class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        self.help = "Select between two images."
        self.label = "Select"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image1",
                          "label":"First Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image2",
                          "label":"Second Image",
                          "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "label":"Output Image",
                          "conn_type":"Output"}]

        self.group = "General"

        self.properties = [{"name": "key",
                            "label": "Key",
                            "type": MOSAICODE_STRING,
                            "maxlength": 1,
                            "value":"a"
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
            'IplImage * $port[input_image1]$ = NULL;\n' + \
            'IplImage * $port[input_image2]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'char block$id$_key = $prop[key]$;\n'

        self.codes["execution"] = \
            '\nif($port[input_image1]$ && $port[input_image2]$){\n' + \
            'if ($prop[key]$ != -1)\n' + \
            '\tblock$id$_key = $prop[key]$;\n' + \
            'if (block$id$_key == \'$prop[key]$\' )\n' + \
            '\t$port[output_image]$ = cvCloneImage($port[input_image1]$);\n' + \
            'else\n' + \
            '\t$port[output_image]$ = cvCloneImage($port[input_image2]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image1]$);\n' + \
            'cvReleaseImage(&$port[input_image2]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'     

# -----------------------------------------------------------------------------
