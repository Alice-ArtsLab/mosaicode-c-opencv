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
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"first_image",
                          "conn_type":"Input",
                          "label":"First Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"second_image",
                          "conn_type":"Input",
                          "label":"Second Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Arithmetic and Logical Operations"

#----------------------------- C/OpenCV code --------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[first_image]$;
    Mat $port[second_image]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[first_image]$.empty() && !$port[second_image]$.empty()){
        Size size$id$($port[first_image]$.cols, $port[first_image]$.rows);
        resize($port[second_image]$, $port[second_image]$, size$id$);
        bitwise_and($port[first_image]$, $port[second_image]$, $port[output_image]$);
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[first_image]$.release();
    $port[second_image]$.release();
    $port[output_image]$.release();
"""

#-----------------------------------------------------------------------------