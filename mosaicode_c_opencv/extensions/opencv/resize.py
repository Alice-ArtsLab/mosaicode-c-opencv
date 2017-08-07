#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Resize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Resize(BlockModel):
    """
    This class contains methods related the Resize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Resizes the input image to the " + \
            "dimensions of the input rectangle."
        self.label = "Resize Image"
        self.color = "20:80:10:150"
        self.in_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "label":"Input Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.rect",
                          "name":"size",
                          "label":"Size"}
                         ]
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Experimental"

        self.properties = [{"label": "Method",
                            "name": "method",
                            "type": MOSAICODE_COMBO,
                            "value": "CV_INTER_LINEAR",
                            "values": ["CV_INTER_NN",
                                       "CV_INTER_LINEAR",
                                       "CV_INTER_AREA",
                                       "CV_INTER_CUBIC"]
                            }
                           ]

        self.codes["execution"] = \
            'if(block$id$_img_i0){\n' + \
            'CvSize size$id$ = cvSize(block$id$_rect_i1.width,' + \
            'block$id$_rect_i1.height);\n' + \
            'block$id$_img_o0 = cvCreateImage(size$id$, ' + \
            'block$id$_img_i0->depth,block$id$_img_i0->nChannels);\n' + \
            'cvResize(block$id$_img_i0, block$id$_img_o0, $method$);\n' + \
            '}\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
