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

        # Appearance
        self.help = "BLOCO Composição RGB"
        self.label = "Compose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input0",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input1",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input2",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"output0",
                       "conn_type":"Output"}]
        self.group = "Filters and Color Conversion"

        # ------------------------C/OpenCv code-------------------------------
        self.codes["declaration"] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_i1 = NULL;\n' + \
            'IplImage * block$id$_img_i2 = NULL;\n' + \
            'IplImage * block$id$_img_t0 = NULL;\n' + \
            'IplImage * block$id$_img_t1 = NULL;\n' + \
            'IplImage * block$id$_img_t2 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n'

        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'CvSize size$id$ = cvSize' + \
            '(block$id$_img_i0->width,block$id$_img_i0->height);\n' + \
            'block$id$_img_t0 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'block$id$_img_t1 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'block$id$_img_t2 = cvCreateImage' + \
            '(size$id$, block$id$_img_i0->depth, 1);\n' +\
            'cvSplit(block$id$_img_i0 ,' + \
            'block$id$_img_t0  ,NULL, NULL , NULL);\n' + \
            'cvSplit(block$id$_img_i1 ,' + \
            'NULL ,block$id$_img_t1, NULL, NULL);\n' + \
            'cvSplit(block$id$_img_i2 ,' + \
            'NULL ,NULL, block$id$_img_t2 , NULL);\n' + \
            'cvMerge(block$id$_img_t2 ,block$id$_img_t1 ,' + \
            'block$id$_img_t0 , NULL, block$id$_img_o0);}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t0);\n' + \
            'cvReleaseImage(&block$id$_img_t1);\n' + \
            'cvReleaseImage(&block$id$_img_t2);\n' + \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_i1);\n' + \
            'cvReleaseImage(&block$id$_img_i2);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
