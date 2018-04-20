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
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_apertureSize",
                          "label":"Aperture Size"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold1",
                          "label":"Threshold 1"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold2",
                          "label":"Threshold 2"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]

        self.group = "Gradients, Edges and Corners"

        self.properties = [{"label": "Aperture Size",
                            "name": "apertureSize",
                            "type": MOSAICODE_INT,
                            "lower": 3,
                            "upper": 7,
                            "value":5,
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
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'int $port[input_apertureSize]$ = $prop[apertureSize]$;\n' + \
            'int $port[input_threshold1]$ = $prop[threshold1]$;\n' + \
            'int $port[input_threshold2]$ = $prop[threshold2]$;\n'

        self.codes["execution"] = \
            "\nif(!$port[input_image]$.empty()){ \n" + \
            "\tif ($port[input_apertureSize]$ < 1) $port[input_apertureSize]$ = 1;\n" + \
            "\tif ($port[input_threshold1]$ < 1) $port[input_threshold1]$ = 1;\n" + \
            "\tif ($port[input_threshold2]$ < 1) $port[input_threshold2]$ = 1;\n" + \
            "\tif ($port[input_apertureSize]$ > 10) $port[input_apertureSize]$ = 10;\n" + \
            "\tif ($port[input_threshold1]$ > 100) $port[input_threshold1]$ = 100;\n" + \
            "\tif ($port[input_threshold2]$ > 100) $port[input_threshold2]$ = 100;\n" + \
            "\t$port[output_image]$ = $port[input_image]$.clone();\n" + \
            "\tMat tmpImg$id$($port[input_image]$.rows,$port[input_image]$.cols,CV_8U);\n" + \
            "\tif($port[input_image]$.channels() == 3){\n" + \
            "    \t\tcvtColor($port[input_image]$," + \
            " tmpImg$id$ ,COLOR_RGB2GRAY);\n" + \
            "\t}else{\n" + \
            "    \t\ttmpImg$id$ = $port[input_image]$ = Mat::zeros($port[input_image]$.cols, " + \
            "$port[input_image]$.rows, CV_8UC1);\n" + \
            "}\n" + \
            "Canny(tmpImg$id$, tmpImg$id$, $port[input_threshold1]$," + \
            " $port[input_threshold2]$, $port[input_apertureSize]$);\n" + \
            "\tif($port[input_image]$.channels() == 3){\n" + \
            "    \t\tcvtColor(tmpImg$id$, " + \
            "$port[output_image]$,COLOR_GRAY2RGB);\n" + \
            "\t}else{\n" + \
            "    \t\t$port[output_image]$ = tmpImg$id$.clone();\n" + \
            "\t}\n" + \
            "\ttmpImg$id$.release();\n" + \
            "}\n"

        self.codes["deallocation"] = \
            "$port[input_image]$.release();\n" + \
            "$port[output_image]$.release();\n"
# -----------------------------------------------------------------------------
