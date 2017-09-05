#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewImage class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewImage(BlockModel):
    """
    This class contains methods related the NewImage class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.width = "640"
        self.height = "480"

        # Appearance
        self.help = "Cria uma nova imagem."
        self.label = "New Image"
        self.color = "50:100:200:150"
        self.out_types = ["mosaicode_c_opencv.extensions.ports.image"]
        self.group = "Image Source"

        self.properties = [{"name": "Width",
                            "label": "width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            },
                           {"name": "Height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["execution"] = \
            'CvSize size$id$ = cvSize($width$,$height$);\n' + \
            'block$id$_img_o0 = cvCreateImage(size$id$,IPL_DEPTH_8U,3);\n' + \
            'cvSetZero(block$id$_img_o0);\n'
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
