#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ImageFile class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ImageFile(BlockModel):
    """
    This class contains methods related the ImageFile class.
    """

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Image File"
        self.color = "50:100:200:150"
        self.group = "Image Source"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                           "conn_type":"Output",
                           "label":"Output Image"}]
        self.properties = [{"label": "File Name",
                            "name": "filename",
                            "type": MOSAICODE_OPEN_FILE,
                            "value":"/usr/share/mosaicode/extensions/c-opencv/images/yellow-house.jpg"
                            }
                           ]

# ---------------------------- C/OpenCv Code -------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""
    $port[output_image]$ = imread("$prop[filename]$", IMREAD_COLOR);
"""                

        self.codes["deallocation"] = \
"""        
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------
