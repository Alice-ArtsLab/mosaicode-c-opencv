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
        self.group = "General"

        self.properties = [{"name": "File Name",
                            "label": "filename",
                            "type": MOSAICODE_SAVE_FILE
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["execution"] = \
            'block$id$_img_o0 = cvCloneImage(block$id$_img_i0);\n' + \
            'if(block$id$_img_i0)\n' + \
            'cvSaveImage("$filename$" ,block$id$_img_i0);\n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
