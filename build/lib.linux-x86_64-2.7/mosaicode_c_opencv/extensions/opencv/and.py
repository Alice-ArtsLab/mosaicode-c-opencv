#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the And class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class And(BlockModel):
    """
    This class contains methods related the And class.
    """
    # ------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Permite a operação lógica 'E' entre as duas entradas." + \
            " Para esse bloco há duas possibilidades." + \
            "Primeira: Executa a operação entre" + \
            " duas imagens ponto a ponto." + \
            "Segunda: Executa a operação entre um " + \
            "valor constante e cada ponto da imagem."
        self.label = "And"
        self.language = "c"
        self.framework = "opencv"
        self.color = "10:180:10:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"first_image",
                          "conn_type":"Input",
                          "label":"First Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "conn_type":"Input",
                          "label":"Second Image"},
                         {"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Arithmetic and logical operations"

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

        self.codes["declaration"] = "// $id$ - And\n" + \
                    "IplImage * $in_ports[first_image]$ = NULL;\n" + \
                    "IplImage * $in_ports[second_image]$ = NULL;\n" + \
                    "IplImage * $out_ports[output_image]$ = NULL;\n"

        self.codes["execution"] = \
            '\nif($in_ports[first_image]$ && $in_ports[second_image]$){\n' + \
            '\t$out_ports[output_image]$ = cvCloneImage($in_ports[first_image]$);\n' + \
            '\tadjust_images_size($in_ports[first_image]$, ' + \
            '$in_ports[second_image]$, $out_ports[output_image]$);\n' + \
            '\tcvAnd($in_ports[first_image]$, ' + \
            '$in_ports[second_image]$, $out_ports[output_image]$,0);\n' + \
            '\tcvResetImageROI($out_ports[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = "cvReleaseImage(&$in_ports[first_image]$);\n" + \
                    "cvReleaseImage(&$in_ports[second_image]$);\n" + \
                    "cvReleaseImage(&$out_ports[output_image]$);\n"
# -----------------------------------------------------------------------------
