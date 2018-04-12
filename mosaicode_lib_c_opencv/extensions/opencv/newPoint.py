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
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.point",
                        "name":"point",
                        "label":"Point",
                        "conn_type":"Output"}]
        self.group = "Basic Data Type"

        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            },
                           {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/newPoint.py
        self.codes["declaration"] = 'Point $port[point]$ = Point($prop[x]$, $prop[y]$);\n'

        self.codes["execution"] = \
            '$port[point]$ = Point($prop[x]$, $prop[y]$);\n'
=======
        self.codes["declaration"] = 'CvPoint $port[point]$ = cvPoint($prop[x]$,$prop[y]$);\n'

        self.codes["execution"] = \
            '$port[point]$ = cvPoint($prop[x]$,$prop[y]$);\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/newPoint.py
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
