#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewRect class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewRect(BlockModel):
    """
    This class contains methods related the NewRect class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Creates new rectangle"
        self.label = "New Rectangle"
        self.color = "50:50:200:150"
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.rect",
                          "name":"size",
                          "label":"Size"}]
        self.group = "Basic Data Type"

        self.properties = [{"label": "X",
                            "name": "x",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":0
                            },
                           {"label": "Y",
                            "name": "y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":0
                            },
                           {"label": "Width",
                            "name": "width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":640
                            },
                           {"label": "Height",
                            "name": "height",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":480
                            }
                           ]

        self.codes[1] = "CvRect block$id$_rect_o0 = cvRect( 0, 0, 1, 1);"
        self.codes[2] = \
            'block$id$_rect_o0 = cvRect($prop[x]$, $prop[y]$, $prop[width]$, $prop[height]$);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
