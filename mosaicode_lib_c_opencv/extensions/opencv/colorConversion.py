#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ColorConversion class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ColorConversion(BlockModel):
    """
    This class contains methods related the ColorConversion class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        self.conversion_type = 'RGB -> GRAY'

        # Appearance
        self.help = "Realiza a conversão de cores entre diferentes " + \
            "padrões de imagens coloridas e tons de cinza."
        self.label = "Color Conversion"
        self.color = "50:125:50:150"
        ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                  "name":"input0",
                  "conn_type":"Input"},
                  {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                   "name":"output0",
                   "conn_type":"Output"}]
        self.group = "Filters and Color Conversion"

        self.language = "c"
        self.framework = "opencv"

        self.properties = [{"name": "conversion_type",
                            "label": "Conversion Type",
                            "type": MOSAICODE_COMBO,
                            "values": [
                                        'CV_RGB2GRAY',
                                        'CV_RGB2YCrCb',
                                        'CV_YCrCb2RGB',
                                        'CV_RGB2HSV',
                                        'CV_HSV2RGB',
                                        'CV_RGB2HLS',
                                        'CV_HLS2RGB',
                                        'CV_RGB2XYZ',
                                        'CV_XYZ2RGB',
                                        'CV_RGB2Lab',
                                        'CV_Lab2RGB',
                                        'CV_RGB2Luv',
                                        'CV_Luv2RGB'
                                       ]
                            }
                           ]

        self.codes["declaration"] =  \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_o0);\n'

        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_o0 = cvCloneImage' + \
            '(block$id$_img_i0);\n' + \
            'block$id$_img_t = cvCreateImage(cvGetSize(block$id$_img_i0),' + \
            'block$id$_img_i0->depth,3);\n' + \
            'cvCvtColor(block$id$_img_i0, ' + \
            'block$id$_img_t ,$prop[conversion_type]$ );}\n' + \
            'if ($prop[conversion_type]$ == ' + "CV_RGB2GRAY" + ')\n' + \
            '{    cvMerge(block$id$_img_t ,block$id$_img_t ,' + \
            'block$id$_img_t ,NULL ,block$id$_img_o0);\n }\n' + \
            'else\n' + '{ block$id$_img_o0 = cvCloneImage(block$id$_img_t);\n}'
# -----------------------------------------------------------------------------
