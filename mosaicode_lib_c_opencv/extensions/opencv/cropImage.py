#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the CropImage class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class CropImage(BlockModel):
    """
    This class contains methods related the CropImage class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Corta a imagem de acordo com o retângulo de entrada."
        self.label = "Crop Image"
        self.color = "50:50:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.rect",
                       "name":"rect",
                       "label":"Rect",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "Experimental"

        self.properties = [{"name": "x",
                            "label": "X",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "y",
                            "label": "Y",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 1
                            },
                           {"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 200
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 65535,
                            "step": 1,
                            "value": 200
                            }
                           ]

        # ------------------------C/OpenCv code--------------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'CvRect $port[rect]$ = cvRect' + \
            '($prop[x]$, $prop[y]$, $prop[width]$, $prop[height]$);\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '   $port[rect]$.x = MAX' + \
            '(0,$port[rect]$.x);//Check whether point is negative\n' + \
            '   $port[rect]$.y = MAX' + \
            '(0,$port[rect]$.y);\n' + \
            '   $port[rect]$.x = MIN($port[input_image]$->width-1,' + \
            '$port[rect]$.x);//Check whether ' + \
            'point is out of the image\n' + \
            '   $port[rect]$.y = MIN' + \
            '($port[input_image]$->height-1,' + \
            '$port[rect]$.y);\n' + \
            '   $port[rect]$.width = MIN' + \
            '($port[input_image]$->width-$port[rect]$.x,' + \
            '$port[rect]$.width);' + \
            '//Check whether rect reaches out of the image\n' + \
            '   $port[rect]$.height = MIN($port[rect]$->' + \
            'height-$port[rect]$.y,$port[rect]$.height);\n' + \
            '   $port[output_image]$ = cvCreateImage' + \
            '(cvSize($port[rect]$.width,' + \
            '$port[rect]$.height),' + \
            ' $port[input_image]$->depth,$port[input_image]$->nChannels);\n' + \
            '   cvSetImageROI($port[input_image]$,$port[rect]$);\n' + \
            '   cvCopy($port[input_image]$,$port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "cvReleaseImage(&$port[input_image]$);\n" + \
            "cvReleaseImage(&$port[output_image]$);\n"

# -----------------------------------------------------------------------------
