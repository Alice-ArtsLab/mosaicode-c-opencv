#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module contains the LiveMode class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class LiveMode(BlockModel):
    """
    This class contains methods related the LiveMode class.
    """

    def __init__(self):
        BlockModel.__init__(self)
        
        self.language = "c"
        self.framework = "opencv"
        self.label = "Live Mode"
        self.color = "50:100:200:150"
        self.group = "Image Source"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "conn_type":"Output",
                       "label":"Output Image"}
        ]
        self.properties = [{"name": "camera",
                            "label": "Camera ID",
                            "type": MOSAICODE_INT,
                            "lower": -100,
                            "upper": 100,
                            "step": 1,
                            "value": 0
                            }
        ]

# --------------------------- C/OpenCV Code --------------------------- #

        self.codes["declaration"] = \
"""
    Mat $port[output_image]$;
    VideoCapture capture$id$($prop[camera]$);
"""

        self.codes["execution"] = \
"""
    if(!capture$id$.isOpened())
        return -1;
    capture$id$ >> $port[output_image]$;
"""

        self.codes["deallocation"] = \
"""
    $port[output_image]$.release();
"""