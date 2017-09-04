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
                          "name":"apertureSize",
                          "label":"Aperture Size"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"threshold1",
                          "label":"Threshold 1"},
                          {"type":"mosaicode_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"threshold2",
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
            '// $id$ Canny\n' + \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'int block$id$_int_i1 = $prop[apertureSize]$;\n' + \
            'int block$id$_int_i2 = $prop[threshold1]$;\n' + \
            'int block$id$_int_i3 = $prop[threshold2]$;\n'

        self.codes["execution"] = \
            "if(block$id$_img_i0){ //Canny Code\n" + \
            "\tif (block$id$_int_i1 < 1) block$id$_int_i1 = 1;\n" + \
            "\tif (block$id$_int_i2 < 1) block$id$_int_i2 = 1;\n" + \
            "\tif (block$id$_int_i3 < 1) block$id$_int_i3 = 1;\n" + \
            "\tif (block$id$_int_i1 > 10) block$id$_int_i1 = 10;\n" + \
            "\tif (block$id$_int_i2 > 100) block$id$_int_i2 = 100;\n" + \
            "\tif (block$id$_int_i3 > 100) block$id$_int_i3 = 100;\n" + \
            "\tblock$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n" + \
            "\tIplImage * tmpImg$id$ =" + \
            " cvCreateImage(cvGetSize(block$id$_img_i0),8,1);\n" + \
            "\tif(block$id$_img_i0->nChannels == 3){\n" + \
            "    \t\tcvCvtColor(block$id$_img_i0," + \
            " tmpImg$id$ ,CV_RGB2GRAY);\n" + \
            "\t}else{\n" + \
            "    \t\ttmpImg$id$ = block$id$_img_i0 = NULL;\n" + \
            "}\n" + \
            "cvCanny(tmpImg$id$, tmpImg$id$, block$id$_int_i2," + \
            " block$id$_int_i1, block$id$_int_i3);\n" + \
            "\tif(block$id$_img_i0->nChannels == 3){\n" + \
            "    \t\tcvCvtColor(tmpImg$id$, " + \
            "block$id$_img_o0,CV_GRAY2RGB);\n" + \
            "\t}else{\n" + \
            "    \t\tcvCopyImage(tmpImg$id$, block$id$_img_o0);\n" + \
            "\t}\n" + \
            "\tcvReleaseImage(&tmpImg$id$);\n" + \
            "} // End Canny Code\n"

        self.codes["deallocation"] = "cvReleaseImage(&block$id$_img_i0);\n" + \
                       "cvReleaseImage(&block$id$_img_o0);\n"
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
