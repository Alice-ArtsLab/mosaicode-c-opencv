#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Erode class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Erode(BlockModel):
    """
    This class contains methods related the Erode class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.help = "Operação morfológica que provoca erosão " + \
            "nos objetos de uma imagem, reduzindo suas dimensões."
        self.label = "Erosion"
        self.color = "180:230:220:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"input_image",
                          "label":"Input Image"},
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/erode.py
=======
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"iteraction",
                          "label":"Iteractions"},
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/erode.py
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.group = "Morphological Operations"

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
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/erode.py
=======
                            },
                           {"label": "Iterations",
                            "name": "iterations",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/erode.py
                            }
                           ]

        # --------------------------C/OpenCv code------------------------------
        self.codes["declaration"] = \
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/erode.py
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Mat block$id$_arg_mask = ' + \
            'getStructuringElement(MORPH_RECT, Size($prop[masksizex]$ , $prop[masksizey]$), Point(1, 1));\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'erode($port[input_image]$, $port[output_image]$, ' + \
            'block$id$_arg_mask);\n' + \
            '}\n'

        self.codes["deallocation"] =  \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'
=======
            'IplImage * $port[input_image]$ = NULL; // ERODE input\n' + \
            'int $port[iteraction]$ = $prop[iterations]$; // ERODE iterarions\n' + \
            'IplImage * $port[output_image]$ = NULL; // ERODE output\n' + \
            'IplConvKernel * block$id$_arg_mask = ' + \
            'cvCreateStructuringElementEx($prop[masksizex]$ , $prop[masksizey]$, 1, 1,CV_SHAPE_RECT,NULL);\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'cvErode($port[input_image]$, $port[output_image]$, ' + \
            'block$id$_arg_mask, $port[iteraction]$);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&$port[input_image]$);\n" + \
                    "cvReleaseImage(&$port[output_image]$);\n"
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/erode.py

# -----------------------------------------------------------------------------
