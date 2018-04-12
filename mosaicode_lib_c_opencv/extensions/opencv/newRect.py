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
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                          "name":"rect",
                          "conn_type":"Output",
                          "label":"Rect"}]
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

        self.codes["execution"] = \
            '$port[rect]$ = Rect($prop[x]$, $prop[y]$, $prop[width]$, $prop[height]$);\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
