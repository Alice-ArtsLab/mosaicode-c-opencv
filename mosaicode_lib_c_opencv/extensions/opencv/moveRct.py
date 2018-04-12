#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the MoveRct class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class MoveRct(BlockModel):
    """
    This class contains methods related the MoveRct class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.offset_x = 0
        self.offset_y = 0

        # Appearance
        self.help = "Move Rectangle`s (0,0) point to input point"
        self.label = "Move Rectangle"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "label":"Rect",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.point",
                       "name":"point",
                       "label":"Point",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                       "name":"output",
                       "label":"Output Rect",
                       "conn_type":"Output"}]

        self.group = "Experimental"

        self.properties = [{"name": "Offset x",
                            "label": "offset_x",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            },
                           {"name": "Offset Y",
                            "label": "offset_y",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # --------------------C/OpenCv code--------------------------------
        self.codes["declaration"] = \
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/moveRct.py
            'Rect $port[rect]$;\n' + \
            'Point $port[point]$;\n' + \
            'Rect $port[output]$;\n'

        self.codes["execution"] = \
            '$port[output]$ = $port[rect]$;\n' + \
            '$port[output]$.x = $port[point]$.x + $offset_x$;\n' + \
            '$port[output]$.y = $port[point]$.y + $offset_y$;\n'
=======
            'CvRect $ports[rect]$;\n' + \
            'CvPoint $ports[point]$;\n' + \
            'CvRect $ports[output]$;\n'

        self.codes["execution"] = \
            '$ports[output]$ = $ports[rect]$;\n' + \
            '$ports[output]$.x = $ports[point]$.x + $offset_x$;\n' + \
            '$ports[output]$.y = $ports[point]$.y + $offset_y$;\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/moveRct.py

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
