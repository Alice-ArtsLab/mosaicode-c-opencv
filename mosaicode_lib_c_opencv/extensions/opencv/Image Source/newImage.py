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
        self.language = "c"
        self.framework = "opencv"
        self.label = "New Image"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Image"}]
        self.group = "Image Source"
        self.properties = [{"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            },
                            {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10000,
                            "step": 1,
                            "value": 1
                            }
                           ]

#----------------------------- C/OpenCv Code ----------------------------------

        self.codes["execution"] = \
"""        
    Mat $port[output_image]$ = Mat::zeros($prop[width]$, $prop[height]$, CV_8UC3);
"""   

        self.codes["deallocation"] = \
"""
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------
