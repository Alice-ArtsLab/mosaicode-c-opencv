#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Slider class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Slider(BlockModel):
    """
    This class contains methods related the Slider class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Creates Slider to int value."
        self.label = "Slider"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Output",
                          "name":"slider_value",
                          "label":"Slider Value"}]
        self.group = "Basic Data Type"

        self.properties = [{"label": "Value",
                            "name": "intVal",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":1
                            },
                           {"label": "Max Value",
                            "name": "maxVal",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":31
                            },
                           {"label": "Label",
                            "name": "label",
                            "type": MOSAICODE_STRING,
                            "value":"label"
                            },
                           {"label": "Window Title",
                            "name": "window_name",
                            "type": MOSAICODE_STRING,
                            "value":"My Image"
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'int $port[slider_value]$ = $prop[intVal]$;\n'

        self.codes["execution"] = \
            'namedWindow("$prop[window_name]$", WINDOW_AUTOSIZE );\n' + \
            'createTrackbar("$prop[label]$", "$prop[window_name]$",' + \
            '&$port[slider_value]$, $prop[maxVal]$, NULL);\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
