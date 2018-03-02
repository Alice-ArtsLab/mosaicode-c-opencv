#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Resize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Resize(BlockModel):
    """
    This class contains methods related the Resize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Resizes the input image to the " + \
            "dimensions of the input rectangle."
        self.label = "Resize Image"
        self.color = "20:80:10:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input",
                          "conn_type":"Input",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                          "name":"size",
                          "conn_type":"Input",
                          "label":"Size"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output",
                          "conn_type":"Output",
                          "label":"Output Image"}]

        self.group = "Experimental"

        self.properties = [{"label": "Method",
                            "name": "method",
                            "type": MOSAICODE_COMBO,
                            "value": "CV_INTER_LINEAR",
                            "values": ["CV_INTER_NN",
                                       "CV_INTER_LINEAR",
                                       "CV_INTER_AREA",
                                       "CV_INTER_CUBIC"]
                            }
                           ]

        self.codes["execution"] = \
            'if($port[input]$){\n' + \
            'CvSize size$id$ = cvSize($port[size]$.width,' + \
            '$port[size]$.height);\n' + \
            '$port[output]$ = cvCreateImage(size$id$, ' + \
            '$port[input]$->depth,$port[input]$->nChannels);\n' + \
            'cvResize($port[input]$, $port[output]$, $prop[method]$);\n' + \
            '}\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
