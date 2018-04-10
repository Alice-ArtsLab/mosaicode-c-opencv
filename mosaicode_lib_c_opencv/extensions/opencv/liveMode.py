#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the LiveMode class.
"""
import os
from glob import glob
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class LiveMode(BlockModel):
    """
    This class contains methods related the LiveMode class.
    """
    # --------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Realiza a aquisição de uma imagem a partir de câmera."
        self.label = "Live Mode"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                          "name":"output_image",
                          "label":"Output Image"}
                          ]
        self.group = "Image Source"

        self.properties = [{"name": "camera",
                 "label": "Camera",
                 "type": MOSAICODE_INT,
                 "value":"0",
                 "lower": 0,
                 "upper": 4}]

        self.language = "c"
        self.framework = "opencv"

        self.codes["declaration"] = \
            '// Live Mode Cam \n' + \
            'CvCapture * block$id$_capture = NULL;\n' + \
            'block$id$_capture = cvCaptureFromCAM($prop[camera]$);\n' + \
            'IplImage * block$id$_frame = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n'

        self.codes["execution"] = \
            '// Live Mode \n' + \
            'int value = cvGrabFrame(block$id$_capture);\n' + \
            'block$id$_frame = cvRetrieveFrame(block$id$_capture);\n' + \
            'if(block$id$_frame){\n' +\
            '\t$port[output_image]$ = cvCloneImage(block$id$_frame);\n'+ \
            '}\n'

        self.codes["cleanup"] = 'cvReleaseCapture(&block$id$_capture);\n'

# -----------------------------------------------------------------------------
