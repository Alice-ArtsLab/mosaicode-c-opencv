#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Dilate class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Dilate(BlockModel):
    """
    This class contains methods related the Dilate class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.help = "Operação morfológica que provoca dilatação " + \
            "nos objetos de uma imagem, aumentando suas dimensões."
        self.label = "Dilate"
        self.color = "180:230:220:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "conn_type":"Input",
                        "label":"Input Image"},
                        {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                         "name":"output_image",
                         "conn_type":"Output",
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
                            },
                           {"label": "Iterations",
                            "name": "iterations",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 65535,
                            "step": 1, 
                            "value":1
                            }
                           ]

        # ----------------------------C/OpenCv code---------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'int block$id$_arg_iterations = $prop[iterations]$;\n' + \
            'IplConvKernel * block$id$_arg_mask = ' + \
            'cvCreateStructuringElementEx($prop[masksizex]$ , $prop[masksizey]$, 1, 1,CV_SHAPE_RECT,NULL);\n'

        self.codes["execution"] = '''
            if($port[input_image]$){
                $port[output_image]$ = cvCloneImage($port[input_image]$);
                cvDilate($port[input_image]$,
                        $port[output_image]$,
                        block$id$_arg_mask,
                        block$id$_arg_iterations);
            }
            '''
        self.codes["deallocation"] = "cvReleaseImage(&$port[input_image]$);\n" + \
                       "cvReleaseImage(&$port[output_image]$);\n"
# -----------------------------------------------------------------------------
