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

        # Appearance
        self.help = "BLOCO Decomposição RGB."
        self.label = "Decompose RGB"
        self.color = "50:125:50:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input0",
                       "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output0",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output1",
                       "conn_type":"Output"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"output2",
                       "conn_type":"Output"}]
        self.group = "Filters and Color Conversion"

        # ------------------C/OpenCv code--------------------------------------
        self.codes["declaration"] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_t0 = NULL;\n' + \
            'IplImage * block$id$_img_t1 = NULL;\n' + \
            'IplImage * block$id$_img_t2 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_o1 = NULL;\n' + \
            'IplImage * block$id$_img_o2 = NULL;\n'
        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'block$id$_img_o1 = cvCloneImage(block$id$_img_i0);\n' + \
            'block$id$_img_o2 = cvCloneImage(block$id$_img_i0);\n' + \
            'block$id$_img_t0 = cvCreateImage' + \
            '(cvGetSize(block$id$_img_i0), block$id$_img_i0->depth, 1);\n' + \
            'block$id$_img_t1 = cvCreateImage' + \
            '(cvGetSize(block$id$_img_i0), block$id$_img_i0->depth, 1);\n' +\
            'block$id$_img_t2 = cvCreateImage' + \
            '(cvGetSize(block$id$_img_i0), block$id$_img_i0->depth, 1);\n' + \
            'cvSplit(block$id$_img_i0 ,block$id$_img_t2 ,' + \
            'block$id$_img_t1 ,block$id$_img_t0 , NULL);\n' + \
            'cvMerge(block$id$_img_t0 ,block$id$_img_t0, block$id$_img_t0,' + \
            'NULL, block$id$_img_o0);\n' + \
            'cvMerge(block$id$_img_t1 ,block$id$_img_t1, ' + \
            'block$id$_img_t1, NULL, block$id$_img_o1);\n' + \
            'cvMerge(block$id$_img_t2 ,block$id$_img_t2, ' + \
            'block$id$_img_t2, NULL, block$id$_img_o2);\n}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t0);\n' + \
            'cvReleaseImage(&block$id$_img_t1);\n' + \
            'cvReleaseImage(&block$id$_img_t2);\n' + \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_o1);\n' + \
            'cvReleaseImage(&block$id$_img_o2);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
