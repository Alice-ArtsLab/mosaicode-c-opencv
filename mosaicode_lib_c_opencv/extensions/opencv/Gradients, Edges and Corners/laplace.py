#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Laplace class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Laplace(BlockModel):
    """
    This class contains methods related the laplace class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.help = "Operação de filtragem que calcula o " + \
            "Laplaciano de uma imagem," + \
            "realçando cantos e bordas de objetos."
        self.label = "Laplace"
        self.color = "250:180:80:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_masksize",
                          "label":"Mask Size"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]
        self.group = "Gradients, Edges and Corners"
        self.properties = [{"label": "Mask Size",
                            "name": "masksize",
                            "type": MOSAICODE_COMBO,
                            "value": 3,
                            "values": ["3", "5", "7"]
                            }
                           ]

# ------------------------------- C/OpenCv Code -----------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    int $port[input_masksize]$ = $prop[masksize]$;
"""

        self.codes["execution"] = \
"""
    if(!$port[input_image]$.empty()){
        $port[input_masksize]$ = ($port[input_masksize]$ > 31)? 31 : $port[input_masksize]$ = ($port[input_masksize]$ % 2 == 0)? $port[input_masksize]$ + 1 : $port[input_masksize]$;
        cvtColor($port[input_image]$, $port[input_image]$, COLOR_RGB2GRAY);
        Laplacian($port[input_image]$, $port[output_image]$, CV_16S, $port[input_masksize]$, 1, 0);
        convertScaleAbs($port[output_image]$, $port[output_image]$);
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();     
"""

# -----------------------------------------------------------------------------
