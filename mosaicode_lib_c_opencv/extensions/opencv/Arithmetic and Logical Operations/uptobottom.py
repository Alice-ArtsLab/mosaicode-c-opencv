#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the UpToBottom class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class UpToBottom(BlockModel):
    """
    This class contains methods related the UpToBottom class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Coloca uma imagem debaixo da outra."
        self.label = "Up to Bottom"
        self.color = "10:180:10:150"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image1",
                          "conn_type":"Input",
                          "label":"Top Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image2",
                          "conn_type":"Input",
                          "label":"Bottom Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "conn_type":"Output",
                           "name":"output_image",
                           "label":"Output Image"}]

        self.group = "Arithmetic and Logical Operations"

#----------------------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image1]$;
    Mat $port[input_image2]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image1]$.empty() && !$port[input_image2]$.empty()){
        Size size_1($port[input_image1]$.cols, $port[input_image1]$.rows);
        Size size_2($port[input_image2]$.cols, $port[input_image2]$.rows);
        Mat block$id$_img_t(size_1.height+size_2.height, size_1.width, CV_8UC3);
        Mat top_image(block$id$_img_t, Rect(0, 0, size_1.width, size_1.height));
        $port[input_image1]$.copyTo(top_image);
        Mat bottom_image(block$id$_img_t, Rect(0, size_1.height, size_2.width, size_2.height));
        $port[input_image2]$.copyTo(bottom_image);
        $port[output_image]$ = block$id$_img_t.clone();
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[output_image]$.release();
    $port[input_image1]$.release();
    $port[input_image2]$.release();
"""

# -----------------------------------------------------------------------------
