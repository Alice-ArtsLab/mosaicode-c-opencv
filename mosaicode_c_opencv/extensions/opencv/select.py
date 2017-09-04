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
        self.help = "Select between two images."
        self.label = "Select"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"first_image",
                          "label":"First Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "label":"Second Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.image",
                           "conn_type":"Output",
                          "name":"output_image",
                           "label":"Output Image"}]
        self.group = "General"

        self.properties = [{"name": "Key",
                            "label": "key",
                            "type": MOSAICODE_STRING,
                            "maxlength": 1,
                            "value":"a"
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = 'IplImage * block$id$_img_i0 = NULL;\n'
        self.codes["declaration"] += 'IplImage * block$id$_img_i1 = NULL;\n'
        self.codes["declaration"] += 'IplImage * block$id$_img_o0 = NULL;\n'
        self.codes["declaration"] += 'char block$id$_key = \'$key$\';\n'

        self.codes["execution"] = 'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'if (key != -1)\n' + \
            '\tblock$id$_key = key;\n' + \
            'if (block$id$_key == \'$key$\' )\n' + \
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'else\n' + \
            '\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i1);\n' + \
            '}\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
