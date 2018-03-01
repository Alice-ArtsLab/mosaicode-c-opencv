#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Canny class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Canny(BlockModel):
    """
    This class contains methods related the Canny class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        self.help = "Operacão de filtragem que implementa o algoritmo " + \
            "Canny para detecção de contornos e bordas." + \
            "\nPropriedades\nLimiar 1 e Limiar 2: os dois valores" + \
            " de limiar são utilizados em conjunto." + \
            "O menor valor é utilizado para a realizar a " + \
            "conexão de cantos e bordas." + \
            "O maior valor é utilizado para encontrar" + \
            " segmentos iniciais das bordas mais significativas."
        self.label = "Canny"
        self.color = "50:180:80:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_apertureSize",
                          "label":"Aperture Size"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold1",
                          "label":"Threshold 1"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold2",
                          "label":"Threshold 2"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]

        self.group = "Gradients, Edges and Corners"

        self.properties = [{"label": "Aperture Size",
                            "name": "apertureSize",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 10,
                            "value":3,
                            "step": 1
                            },
                           {"label": "Threshold 1",
                            "name": "threshold1",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 100,
                            "value": 16,
                            "step": 1
                            },
                           {"label": "Threshold 2",
                            "name": "threshold2",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 100,
                            "value": 33,
                            "step": 1
                            }
                           ]

        # -------------------------C/OpenCV code----------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'int $port[input_apertureSize]$ = $prop[apertureSize]$;\n' + \
            'int $port[input_threshold1]$ = $prop[threshold1]$;\n' + \
            'int $port[input_threshold2]$ = $prop[threshold2]$;\n'

        self.codes["execution"] = \
            "\nif($port[input_image]$){ \n" + \
            "\tif ($port[input_apertureSize]$ < 1) $port[input_apertureSize]$ = 1;\n" + \
            "\tif ($port[input_threshold1]$ < 1) $port[input_threshold1]$ = 1;\n" + \
            "\tif ($port[input_threshold2]$ < 1) $port[input_threshold2]$ = 1;\n" + \
            "\tif ($port[input_apertureSize]$ > 10) $port[input_apertureSize]$ = 10;\n" + \
            "\tif ($port[input_threshold1]$ > 100) $port[input_threshold1]$ = 100;\n" + \
            "\tif ($port[input_threshold2]$ > 100) $port[input_threshold2]$ = 100;\n" + \
            "\t$port[output_image]$ = cvCloneImage($port[input_image]$);\n" + \
            "\tIplImage * tmpImg$id$ =" + \
            " cvCreateImage(cvGetSize($port[input_image]$),8,1);\n" + \
            "\tif($port[input_image]$->nChannels == 3){\n" + \
            "    \t\tcvCvtColor($port[input_image]$," + \
            " tmpImg$id$ ,CV_RGB2GRAY);\n" + \
            "\t}else{\n" + \
            "    \t\ttmpImg$id$ = $port[input_image]$ = NULL;\n" + \
            "}\n" + \
            "cvCanny(tmpImg$id$, tmpImg$id$, $port[input_threshold1]$," + \
            " $port[input_threshold2]$, $port[input_apertureSize]$);\n" + \
            "\tif($port[input_image]$->nChannels == 3){\n" + \
            "    \t\tcvCvtColor(tmpImg$id$, " + \
            "$port[output_image]$,CV_GRAY2RGB);\n" + \
            "\t}else{\n" + \
            "    \t\tcvCopy(tmpImg$id$, $port[output_image]$);\n" + \
            "\t}\n" + \
            "\tcvReleaseImage(&tmpImg$id$);\n" + \
            "}\n"

        self.codes["deallocation"] = \
            "cvReleaseImage(&$port[input_image]$);\n" + \
            "cvReleaseImage(&$port[output_image]$);\n"
# -----------------------------------------------------------------------------
