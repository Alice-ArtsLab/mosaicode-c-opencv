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
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/save.py
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                         "name":"output_image",
=======
                        "name":"input",
                        "label":"Input Image",
                        "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                         "name":"output",
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/save.py
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
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/save.py
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n'

        self.codes["execution"] = \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'if(!$port[input_image]$.empty())\n' + \
            'imwrite("$prop[filename]$", $port[input_image]$);\n'
=======
        'IplImage * $port[input]$ = NULL;\n' + \
        'IplImage * $port[output]$ = NULL;\n'

        self.codes["execution"] = \
            '$port[output]$ = cvCloneImage($port[input]$);\n' + \
            'if($port[input]$)\n' + \
            'cvSaveImage("$prop[filename]$" ,$port[input]$);\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/save.py

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
