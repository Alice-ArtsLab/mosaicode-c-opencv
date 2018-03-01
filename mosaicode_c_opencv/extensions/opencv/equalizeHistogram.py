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
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                       {"type":"mosaicode_c_opencv.extensions.ports.image",
                        "name":"output_image",
                        "label":"Output Image",
                        "conn_type":"Output"}]

        self.group = "Histograms"

        # -------------------C/OpenCv code-------------------------------------
        self.codes["declaration"] =  \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplImage * block$id$_SourceCx[3];\n' + \
            'IplImage * block$id$_EqCx[3];\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            'CvSize size$id$ = cvGetSize($port[input_image]$);\n' + \
            '$port[output_image]$ = cvCreateImage' + \
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
            'cvSplit($port[input_image]$, block$id$_SourceCx[0],' + \
            'block$id$_SourceCx[1],block$id$_SourceCx[2], NULL);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[0], block$id$_EqCx[0]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[1], block$id$_EqCx[1]);\n' + \
            'cvEqualizeHist(block$id$_SourceCx[2], block$id$_EqCx[2]);\n' + \
            'cvMerge( block$id$_EqCx[0],block$id$_EqCx[1],' + \
            'block$id$_EqCx[2], NULL, $port[output_image]$);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[0]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[1]);\n' + \
            'cvReleaseImage(&block$id$_SourceCx[2]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[0]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[1]);\n' + \
            'cvReleaseImage(&block$id$_EqCx[2]);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&$port[input_image]$);\n" + \
                    "cvReleaseImage(&$port[output_image]$);\n"

# -----------------------------------------------------------------------------
