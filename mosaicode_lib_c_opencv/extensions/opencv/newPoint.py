#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewPoint class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewPoint(BlockModel):
    """
    This class contains methods related the NewPoint class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        self.x0 = 0
        self.y0 = 0

        # Appearance
        self.help = "Creates a new Point."
        self.label = "New Point"
        self.color = "50:50:200:150"
        self.out_types = ["mosaicode_lib_c_opencv.extensions.ports.point"]
        self.group = "Basic Data Type"

        self.properties = [{"name": "X",
                            "label": "x0",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            },
                           {"name": "Y",
                            "label": "y0",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = 'CvPoint block$id$_point_o0 = cvPoint($x0$,$y0$);\n'

        self.codes["execution"] = \
            'block$id$_point_o0 = cvPoint($x0$,$y0$);\n'
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
