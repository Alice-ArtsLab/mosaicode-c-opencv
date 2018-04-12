#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the UpToBottom class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class UpToBottom(BlockModel):
    """
    This class contains methods related the UpToBottom class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Coloca uma imagem debaixo da outra."
        self.label = "Up to Bottom"
        self.color = "10:180:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"top_image",
                          "conn_type":"Input",
                          "label":"Top Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"bottom_image",
                          "conn_type":"Input",
                          "label":"Bottom Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * $port[top_image]$ = NULL;\n" + \
                    "IplImage * $port[bottom_image]$ = NULL;\n" + \
                    "IplImage * $port[output_image]$ = NULL;\n"

        self.codes["execution"] = \
            'if($port[top_image]$ && $port[bottom_image]$){\n' + \
            'int width = ($port[top_image]$->width > ' + \
            '$port[bottom_image]$->width)? $port[top_image]$->width :' + \
            ' $port[bottom_image]$->width;\n' + \
            'int height = $port[top_image]$->height +' + \
            ' $port[bottom_image]$->height;\n' + \
            '$port[output_image]$=cvCreateImage' + \
            '(cvSize(width,height),IPL_DEPTH_8U,3); \n' + \
            'cvSetImageROI($port[output_image]$, cvRect(0, 0, ' + \
            '$port[top_image]$->width, $port[top_image]$->height) );\n' + \
            'cvCopy($port[top_image]$,$port[output_image]$,NULL);\n' + \
            'cvResetImageROI($port[output_image]$);\n' + \
            'cvSetImageROI($port[output_image]$, cvRect' + \
            '(0, $port[top_image]$->height, ' + \
            '$port[bottom_image]$->width, height) );\n' + \
            'cvCopy($port[bottom_image]$,$port[output_image]$,NULL);\n' + \
            'cvResetImageROI($port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'if ($port[output_image]$) cvReleaseImage(&$port[output_image]$);\n' + \
            'cvReleaseImage(&$port[top_image]$);\n' + \
            'cvReleaseImage(&$port[bottom_image]$);\n'
# -----------------------------------------------------------------------------
