#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Log class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Log(BlockModel):
    """
    This class contains methods related the Log class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Aplica a função logarítmica a uma imagem, ou seja," + \
            "calcula o logarítmo natural do valor de intensidade" + \
            " luminosa de cada ponto da imagem."
        self.label = "Log"
        self.color = "230:230:60:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Math Functions"

        # ------------------------------C/OpenCv code--------------------------
        self.codes["declaration"] = \
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/log.py
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Mat block$id$_img_t;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            'cvtColor($port[input_image]$, block$id$_img_t, ' + \
            'COLOR_RGB2GRAY);\n' + \
            'block$id$_img_t.convertTo(block$id$_img_t, CV_32F);\n' + \
            'block$id$_img_t = block$id$_img_t + 1;\n' + \
            'log(block$id$_img_t, block$id$_img_t);\n' + \
            'convertScaleAbs(block$id$_img_t, block$id$_img_t);\n' + \
            'normalize(block$id$_img_t, $port[output_image]$, ' + \
            '0, 255, NORM_MINMAX);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n' + \
            'block$id$_img_t.release();\n'
=======
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["execution"] = \
            '\nif($port[input_image]$){\n' + \
            'block$id$_img_t = cvCreateImage(cvGetSize' + \
            '($port[input_image]$), IPL_DEPTH_32F,' + \
            '$port[input_image]$->nChannels);\n' + \
            '$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
            'cvConvertScale($port[input_image]$, ' + \
            'block$id$_img_t,(1/93.8092),0);\n' + \
            'cvLog(block$id$_img_t, block$id$_img_t);\n' + \
            'cvConvertScale(block$id$_img_t,$port[output_image]$,255.0,0);}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/log.py
# -----------------------------------------------------------------------------
