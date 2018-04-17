#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Save class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Save(BlockModel):
    """
    This class contains methods related the Save class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.filename = ""

        # Appearance
        self.help = "Salva uma imagem em uma mídia indicada pelo usuário." + \
            "Atualmente a imagem é salva como PNG por padrão."
        self.label = "Save Image"
        self.color = "50:100:200:150"
        self.in_types = ["mosaicode_lib_c_opencv.extensions.ports.image"]
        self.out_types = ["mosaicode_lib_c_opencv.extensions.ports.image"]
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                         "name":"output_image",
                         "label":"Output Image",
                         "conn_type":"Output"}]

        self.group = "General"
        self.properties = [{"name": "filename",
                            "label": "File Name",
                            "type": MOSAICODE_SAVE_FILE
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'if(!$port[input_image]$.empty())\n' + \
            'imwrite("$prop[filename]$", $port[input_image]$);\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
