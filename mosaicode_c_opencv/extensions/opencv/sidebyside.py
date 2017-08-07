#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the SideBySide class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class SideBySide(BlockModel):
    """
    This class contains methods related the SideBySide class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.help = "Coloca uma imagem do lado da outra."
        self.label = "Side By Side"
        self.color = "10:180:10:150"
        self.in_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"left_image",
                          "label":"Left Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"right_image",
                          "label":"Right Image"}
                         ]
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * block$id$_img_i0 = NULL;\n" + \
                    "IplImage * block$id$_img_i1 = NULL;\n" + \
                    "IplImage * block$id$_img_o0 = NULL;\n"

        self.codes["execution"] =  \
            'if(block$id$_img_i0 && block$id$_img_i1){\n' + \
            'int width=block$id$_img_i0->width' + \
            ' + block$id$_img_i1->width;\n' + \
            'int height= (block$id$_img_i0->height > ' + \
            'block$id$_img_i1->height)?' + \
            'block$id$_img_i0->height:block$id$_img_i1->height;\n' + \
            'block$id$_img_o0=cvCreateImage(cvSize' + \
            '(width,height),IPL_DEPTH_8U,3); \n' + \
            'cvSetImageROI(block$id$_img_o0, cvRect(0, 0, ' + \
            'block$id$_img_i0->width, block$id$_img_i0->height) );\n' + \
            'cvCopy(block$id$_img_i0,block$id$_img_o0,NULL);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            'cvSetImageROI(block$id$_img_o0, cvRect' + \
            '(block$id$_img_i0->width, 0, width, ' + \
            'block$id$_img_i1->height) );\n' + \
            'cvCopy(block$id$_img_i1,block$id$_img_o0,NULL);\n' + \
            'cvResetImageROI(block$id$_img_o0);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            'if (block$id$_img_o0) cvReleaseImage(&block$id$_img_o0);\n' + \
            'cvReleaseImage(&block$id$_img_i0);\n' + \
            'cvReleaseImage(&block$id$_img_i1);\n'
        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
