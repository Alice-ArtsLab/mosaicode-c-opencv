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

        self.codes["declaration"] = \
            "Mat $port[first_image]$;\n" + \
            "Mat $port[second_image]$;\n" + \
            "Mat $port[output_image]$;\n"

        self.codes["execution"] = \
            '\nif(!$port[first_image]$.empty() && !$port[second_image]$.empty()){\n' + \
            'Size size$id$($port[first_image]$.cols, $port[first_image]$.rows);\n' + \
            'resize($port[second_image]$, $port[second_image]$, size$id$);\n' + \
            'bitwise_and($port[first_image]$, ' + \
            '$port[second_image]$, $port[output_image]$);\n' + \
            '}\n'

        self.codes["deallocation"] = \
            "$port[first_image]$.release();\n" + \
            "$port[second_image]$.release();\n" + \
            "$port[output_image]$.release();\n"
# -----------------------------------------------------------------------------
