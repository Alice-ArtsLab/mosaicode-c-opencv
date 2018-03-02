#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the DecomposeRGB class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class DecomposeRGB(BlockModel):
    """
    This class contains methods related the DecomposeRGB class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a decomposição RGB de imagens."
        self.label = "Decompose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image1",
                       "label":"Output 1",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image2",
                       "label":"Output 2",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image3",
                       "label":"Output 3",
                       "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        # ------------------C/OpenCv code--------------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * block$id$_img_t0 = NULL;\n' + \
            'IplImage * block$id$_img_t1 = NULL;\n' + \
            'IplImage * block$id$_img_t2 = NULL;\n' + \
            'IplImage * $port[output_image1]$ = NULL;\n' + \
            'IplImage * $port[output_image2]$ = NULL;\n' + \
            'IplImage * $port[output_image3]$ = NULL;\n'
        
        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[output_image1]$ = cvCloneImage($port[input_image]$);\n' + \
            '$port[output_image2]$ = cvCloneImage($port[input_image]$);\n' + \
            '$port[output_image3]$ = cvCloneImage($port[input_image]$);\n' + \
            'block$id$_img_t0 = cvCreateImage' + \
            '(cvGetSize($port[input_image]$), $port[input_image]$->depth, 1);\n' + \
            'block$id$_img_t1 = cvCreateImage' + \
            '(cvGetSize($port[input_image]$), $port[input_image]$->depth, 1);\n' +\
            'block$id$_img_t2 = cvCreateImage' + \
            '(cvGetSize($port[input_image]$), $port[input_image]$->depth, 1);\n' + \
            'cvSplit($port[input_image]$ ,block$id$_img_t2 ,' + \
            'block$id$_img_t1 ,block$id$_img_t0 , NULL);\n' + \
            'cvMerge(block$id$_img_t0 ,block$id$_img_t0, block$id$_img_t0,' + \
            'NULL, $port[output_image1]$);\n' + \
            'cvMerge(block$id$_img_t1 ,block$id$_img_t1, ' + \
            'block$id$_img_t1, NULL, $port[output_image2]$);\n' + \
            'cvMerge(block$id$_img_t2 ,block$id$_img_t2, ' + \
            'block$id$_img_t2, NULL, $port[output_image3]$);\n}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t0);\n' + \
            'cvReleaseImage(&block$id$_img_t1);\n' + \
            'cvReleaseImage(&block$id$_img_t2);\n' + \
            'cvReleaseImage(&$port[output_image1]$);\n' + \
            'cvReleaseImage(&$port[output_image2]$);\n' + \
            'cvReleaseImage(&$port[output_image3]$);\n' + \
            'cvReleaseImage(&$port[input_image]$);\n'

# -----------------------------------------------------------------------------
