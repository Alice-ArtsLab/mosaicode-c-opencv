#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the EqualizeHistogram class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class EqualizeHistogram(BlockModel):
    """
    This class contains methods related the EqualizeHistogram class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "A equalização do histograma de uma imagem visa " + \
            "alcançar maior contraste entre os " + \
            "diversos elementos de uma imagem."
        self.label = "Equalize Histogram"
        self.color = "0:0:0:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                       "name":"input0",
                       "conn_type":"Input"},
                       {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"output0",
                        "conn_type":"Output"}]
        self.group = "Histograms"

        # -------------------C/OpenCv code-------------------------------------
        self.codes["declaration"] =  \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_SourceCx[3];\n' + \
            'IplImage * block$id$_EqCx[3];\n'

        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'CvSize size$id$ = cvGetSize(block$id$_img_i0);\n' + \
            'block$id$_img_o0 = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 3);\n' + \
            'block$id$_SourceCx[0] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_SourceCx[1] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_SourceCx[2] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[0] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[1] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'block$id$_EqCx[2] = cvCreateImage' + \
            '(size$id$, IPL_DEPTH_8U, 1);\n' + \
            'cvSplit(block$id$_img_i0, block$id$_SourceCx[0],' + \
            'block$id$_SourceCx[1],block$id$_SourceCx[2], NULL);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[0], block$id$_EqCx[0]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[1], block$id$_EqCx[1]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[2], block$id$_EqCx[2]);\n' + \
            'cvMerge( block$id$_EqCx[0],block$id$_EqCx[1],' + \
            'block$id$_EqCx[2], NULL,block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[0]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[1]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[2]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[0]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[1]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[2]);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&block$id$_img_i0);\n" + \
                    "cvReleaseImage(&block$id$_img_o0);\n"

# -----------------------------------------------------------------------------
