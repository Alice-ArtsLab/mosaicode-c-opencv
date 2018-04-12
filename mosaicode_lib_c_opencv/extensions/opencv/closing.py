#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Closing class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Closing(BlockModel):
    """
    This class contains methods related the Closing class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/closing.py
        
=======
        2
        self.masksize = "7x7"
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/closing.py
        self.language = "c"
        self.framework = "opencv"
        # Appearance
        self.help = "Operação de morfologia matemática para realizar o " + \
            "fechamento da imagem de acordo com o elemento estruturante." + \
            "Equivale a aplicação de uma dilatação seguida de uma erosão."
        self.label = "Closing"
        self.color = "180:230:220:150"
        self.group = "Morphological Operations"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "name":"masksizex",
                          "conn_type":"Input",
                          "label":"Mask Size X"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "name":"masksizey",
                          "conn_type":"Input",
                          "label":"Mask Size Y"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.properties = [{"label": "Mask Size X",
                            "name": "masksizex",
                            "type": MOSAICODE_COMBO,
                            "values": ["1", "3", "5", "7"],
                            "value":"3"
                            },
                            {"label": "Mask Size Y",
                            "name": "masksizey",
                            "type": MOSAICODE_COMBO,
                            "values": ["1", "3", "5", "7"],
                            "value":"3"
                            }
                            ]

        # -------------------C/OpenCv code---------------------------------
        self.codes["declaration"] = \
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/closing.py
            'Mat $port[input_image]$;\n' + \
            'int $port[masksizex]$ = $prop[masksizex]$;\n' + \
            'int $port[masksizey]$ = $prop[masksizey]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Mat block$id$_arg_mask;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            'if ($port[masksizex]$ % 2 == 0) $port[masksizex]$++;\n' + \
            'if ($port[masksizey]$ % 2 == 0) $port[masksizey]$++;\n' + \
            'block$id$_arg_mask = ' + \
            'getStructuringElement(MORPH_RECT, Size($port[masksizex]$ ,' + \
            '$port[masksizey]$), Point(1, 1));\n' + \
            'Mat block$id$_auxImg;\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'block$id$_auxImg = $port[input_image]$.clone();\n' + \
            'morphologyEx($port[input_image]$, $port[output_image]$,' + \
            'MORPH_CLOSE, block$id$_arg_mask);\n}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            'block$id$_arg_mask.release();\n' + \
            '$port[output_image]$.release();\n'
=======
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'int $port[masksizex]$ = $prop[masksizex]$;\n' + \
            'int $port[masksizey]$ = $prop[masksizey]$;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplConvKernel * block$id$_arg_mask = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            'if ($port[masksizex]$ % 2 == 0) $port[masksizex]$++;\n' + \
            'if ($port[masksizey]$ % 2 == 0) $port[masksizey]$++;\n' + \
            'block$id$_arg_mask = ' + \
            'cvCreateStructuringElementEx($port[masksizex]$ ,' + \
            '$port[masksizey]$, 1, 1,CV_SHAPE_RECT,NULL);\n' + \
            'IplImage * block$id$_auxImg;\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'block$id$_auxImg = cvCloneImage($port[input_image]$);\n' + \
            'cvMorphologyEx($port[input_image]$, $port[output_image]$, NULL,' + \
            'block$id$_arg_mask, CV_MOP_CLOSE, 1);\n}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseStructuringElement(&block$id$_arg_mask);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/closing.py

# -----------------------------------------------------------------------------
