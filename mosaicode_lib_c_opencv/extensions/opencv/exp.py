#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Exp class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Exp(BlockModel):
    """
    This class contains methods related the Exp class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Aplica a função exponencial a uma imagem, ou seja, " + \
            "eleva a constante neperiana ao valor " + \
            "de intensidade luminosa de cada ponto da imagem."
        self.label = "Exp"
        self.color = "230:230:60:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Input",
                          "name":"input_image",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Math Functions"

        # --------------------------C/OpenCv code------------------------------
        self.codes["declaration"] = \
            'IplImage * block$id$_img_i0 = NULL;\n' + \
            'IplImage * block$id$_img_o0 = NULL;\n' + \
            'IplImage * block$id$_img_t = NULL;\n'

        self.codes["execution"] = \
            '\nif(block$id$_img_i0){\n' + \
            'block$id$_img_t = cvCreateImage' + \
            '(cvGetSize(block$id$_img_i0), IPL_DEPTH_32F,' + \
            'block$id$_img_i0->nChannels);\n' + \
            'block$id$_img_o0 = cvCloneImage' + \
            '(block$id$_img_i0);\n' + \
            'cvConvertScale(block$id$_img_i0, ' + \
            'block$id$_img_t,(1/255.0),0);\n' + \
            'cvExp(block$id$_img_t, block$id$_img_t);\n' + \
            'cvConvertScale(block$id$_img_t, block$id$_img_o0,' + \
            ' (double)93.8092,0);\n}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_t);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
