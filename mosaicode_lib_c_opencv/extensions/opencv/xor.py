#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Xor class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Xor(BlockModel):
    """
    This class contains methods related the Xor class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Realiza a operação lógica XOR entre duas imagens."
        self.label = "Xor"
        self.color = "10:180:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"first_image",
                          "conn_type":"Input",
                          "label":"First Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "conn_type":"Input",
                          "label":"Second Image"},
                          {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

        self.codes["declaration"] = "IplImage * $port[first_image]$ = NULL;\n" + \
                    "IplImage * $port[second_image]$ = NULL;\n" + \
                    "IplImage * $port[output_image]$ = NULL;\n"

        self.codes["deallocation"] = "cvReleaseImage(&$port[first_image]$);\n" + \
                    "cvReleaseImage(&$port[second_image]$);\n" + \
                    "cvReleaseImage(&$port[output_image]$);\n"

        self.codes["function"] = r"""
// And, Xor, Division, subtraction, sum, or,
//multiplication need images with the same size
void adjust_images_size(IplImage * img1, IplImage * img2, IplImage * img3){
    if(img1->width != img2->width || img1->height != img2->height){
    int minW,minH;
    if(img1->width > img2->width)
        minW = img2->width;
    else
        minW = img1->width;

    if(img1->height > img2->height)
        minH = img2->height;
    else
        minH = img1->height;

    cvSetImageROI(img2, cvRect( 0, 0, minW, minH ));
    cvSetImageROI(img1, cvRect( 0, 0, minW, minH ));
    cvSetImageROI(img3, cvRect( 0, 0, minW, minH ));
    }
}
"""
        self.codes["execution"] = \
            'if($port[first_image]$ && $port[second_image]$){\n' + \
            '$port[output_image]$ = cvCloneImage($port[first_image]$);\n' + \
            'adjust_images_size($port[first_image]$, ' + \
            '$port[second_image]$, $port[output_image]$);\n' + \
            'cvXor($port[first_image]$, $port[second_image]$, ' + \
            '$port[output_image]$,0);\n' + \
            'cvResetImageROI($port[output_image]$);\n' + \
            '}\n'

# -----------------------------------------------------------------------------
