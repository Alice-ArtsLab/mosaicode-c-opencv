#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the SideBySide class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class SideBySide(BlockModel):
    """
    This class contains methods related the SideBySide class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.help = "Coloca uma imagem do lado da outra."
        self.label = "Side By Side"
        self.color = "10:180:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"left_image",
                          "conn_type":"Input",
                          "label":"Left Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"right_image",
                          "conn_type":"Input",
                          "label":"Right Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * $port[left_image]$ = NULL;\n" + \
                    "IplImage * $port[right_image]$ = NULL;\n" + \
                    "IplImage * $port[output_image]$ = NULL;\n"

        self.codes["execution"] =  \
            'if($port[left_image]$ && $port[right_image]$){\n' + \
            'int width=$port[left_image]$->width' + \
            ' + $port[right_image]$->width;\n' + \
            'int height= ($port[left_image]$->height > ' + \
            '$port[right_image]$->height)?' + \
            '$port[left_image]$->height:$port[right_image]$->height;\n' + \
            '$port[output_image]$=cvCreateImage(cvSize' + \
            '(width,height),IPL_DEPTH_8U,3); \n' + \
            'cvSetImageROI($port[output_image]$, cvRect(0, 0, ' + \
            '$port[left_image]$->width, $port[left_image]$->height) );\n' + \
            'cvCopy($port[left_image]$,$port[output_image]$,NULL);\n' + \
            'cvResetImageROI($port[output_image]$);\n' + \
            'cvSetImageROI($port[output_image]$, cvRect' + \
            '($port[left_image]$->width, 0, width, ' + \
            '$port[right_image]$->height) );\n' + \
            'cvCopy($port[right_image]$,$port[output_image]$,NULL);\n' + \
            'cvResetImageROI($port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'if ($port[output_image]$) cvReleaseImage(&$port[output_image]$);\n' + \
            'cvReleaseImage(&$port[left_image]$);\n' + \
            'cvReleaseImage(&$port[right_image]$);\n'
# -----------------------------------------------------------------------------
