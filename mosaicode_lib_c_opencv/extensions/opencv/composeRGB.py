#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ComposeRGB class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ComposeRGB(BlockModel):
    """
    This class contains methods related the ComposeRGB class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a composição RGB de várias imagens."
        self.label = "Compose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image1",
                       "label":"Image 1",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image2",
                       "label":"Image 2",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input_image3",
                       "label":"Image 3",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "Filters and Color Conversion"

        # ------------------------C/OpenCv code-------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image1]$ = NULL;\n' + \
            'IplImage * $port[input_image2]$ = NULL;\n' + \
            'IplImage * $port[input_image3]$ = NULL;\n' + \
            'IplImage * block$id$_img_t0 = NULL;\n' + \
            'IplImage * block$id$_img_t1 = NULL;\n' + \
            'IplImage * block$id$_img_t2 = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image1]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image1]$);\n' + \
            'CvSize size$id$ = cvSize' + \
            '($port[input_image1]$->width,$port[input_image1]$->height);\n' + \
            'block$id$_img_t0 = cvCreateImage' + \
            '(size$id$, $port[input_image1]$->depth, 1);\n' +\
            'block$id$_img_t1 = cvCreateImage' + \
            '(size$id$, $port[input_image2]$->depth, 1);\n' +\
            'block$id$_img_t2 = cvCreateImage' + \
            '(size$id$, $port[input_image3]$->depth, 1);\n' +\
            'cvSplit($port[input_image1]$ ,' + \
            'block$id$_img_t0  ,NULL, NULL , NULL);\n' + \
            'cvSplit($port[input_image2]$ ,' + \
            'NULL ,block$id$_img_t1, NULL, NULL);\n' + \
            'cvSplit( $port[input_image3]$,' + \
            'NULL ,NULL, block$id$_img_t2 , NULL);\n' + \
            'cvMerge(block$id$_img_t2 ,block$id$_img_t1 ,' + \
            'block$id$_img_t0 , NULL, $port[output_image]$);}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t0);\n' + \
            'cvReleaseImage(&block$id$_img_t1);\n' + \
            'cvReleaseImage(&block$id$_img_t2);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n' + \
            'cvReleaseImage(&$port[input_image1]$);\n' + \
            'cvReleaseImage(&$port[input_image2]$);\n' + \
            'cvReleaseImage(&$port[input_image3]$);\n'

# -----------------------------------------------------------------------------
