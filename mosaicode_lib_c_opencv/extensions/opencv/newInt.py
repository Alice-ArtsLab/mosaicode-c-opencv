#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewInt class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewInt(BlockModel):
    """
    This class contains methods related the NewInt class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Creates new literal value (Int)."
        self.label = "New Int"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                        "name":"value",
                        "label":"Value",
                        "conn_type":"Output"}]
        self.group = "Basic Data Type"

        self.properties = [{"name": "integer",
                            "label": "Value",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1,
                            "value":1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/newInt.py
        self.codes["declaration"] = 'int $port[value]$ = $prop[integer]$;\n'
=======
        self.codes["declaration"] = 'int  $port[value]$ = $prop[integer]$; // New Int Out\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/newInt.py
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
