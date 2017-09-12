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

        # Appearance
        self.help = "Cria uma nova imagem."
        self.label = "New Image"
        self.color = "50:100:200:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Image Source"

        self.properties = [{"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":800
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":600
                            }
                           ]

        self.codes["declaration"] = \
            'IplImage * $port[output_image]$ = NULL;\n'

        self.codes["execution"] = \
            'CvSize size$id$ = cvSize($prop[width]$,$prop[height]$);\n' + \
            '$port[output_image]$ = cvCreateImage(size$id$, IPL_DEPTH_8U, 3);\n' + \
            'cvSetZero($port[output_image]$);\n'

        self.codes["deallocation"] = "cvReleaseImage(&$port[output_image]$);\n"

# -----------------------------------------------------------------------------
