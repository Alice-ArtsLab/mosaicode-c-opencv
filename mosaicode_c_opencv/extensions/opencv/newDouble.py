#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the NewDouble class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class NewDouble(BlockModel):
    """
    This class contains methods related the NewDouble class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.help = "Creates new literal value (Double)."
        self.label = "New Double"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.double",
                          "name":"double",
                          "conn_type":"Output",
                          "label":"Double"}]
        self.group = "Basic Data Type"

        self.properties = [{"name": "value",
                            "label": "doubleVal",
                            "type": MOSAICODE_FLOAT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = 'double $ports[double]$ = ' + \
            '$prop[value]$; // New Double Out\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
