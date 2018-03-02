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

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a conversão de cores entre diferentes " + \
            "padrões de imagens coloridas e tons de cinza."
        self.label = "Color Conversion"
        self.color = "50:125:50:150"
        self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "input_image",
                       "label": "Input Image",
                       "conn_type": "Input"},
                      {"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "output_image",
                       "label": "Output Image",
                       "conn_type": "Output"}]

        self.group = "Filters and Color Conversion"

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

        # -----------------C/OpenCv code ---------------------------

        self.codes["declaration"] =  \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'block$id$_img_t = cvCreateImage(cvGetSize($port[input_image]$),' + \
            '$port[input_image]$->depth,3);\n' + \
            'cvCvtColor($port[input_image]$, ' + \
            'block$id$_img_t ,$prop[conversion_type]$ );}\n' + \
            'if ($prop[conversion_type]$ == ' + "CV_RGB2GRAY" + ')\n' + \
            '{    cvMerge(block$id$_img_t ,block$id$_img_t ,' + \
            'block$id$_img_t ,NULL ,$port[output_image]$);\n }\n' + \
            'else\n' + \
            '{ $port[output_image]$ = cvCloneImage(block$id$_img_t);\n}'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_t);\n' + \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'

# -----------------------------------------------------------------------------
