#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ImageFile class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ImageFile(BlockModel):
    """
    This class contains methods related the ImageFile class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        
        self.help = "Realiza a aquisição de uma imagem a " + \
            "partir de algum dispositivo, " + \
            "seja este uma mídia ou um dispositivo de " + \
            "aquisição de imagens (câmera, scanner)."
        self.label = "Image File"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/imageFile.py
                           "conn_type":"Output",
=======
                          "conn_type":"Output",
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/imageFile.py
                           "label":"Output Image"}]
        self.group = "Image Source"

        self.properties = [{"label": "File Name",
                            "name": "filename",
                            "type": MOSAICODE_OPEN_FILE,
                            "value":"/usr/share/mosaicode/images/lenna.png"
                            }
                           ]

        # ----------------------------C/OpenCv code-------------------------
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/imageFile.py
        self.codes["declaration"] = \
            'Mat $port[output_image]$;\n' + \
            '$port[output_image]$ = imread("$prop[filename]$", IMREAD_COLOR);\n'
=======
        self.codes["declaration"] = 'IplImage * $port[output_image]$ = NULL;\n'
        self.codes["declaration"] += '$port[output_image]$ = cvLoadImage("$prop[filename]$",-1);\n'
	self.codes["execution"] = "\n"
        self.codes["cleanup"] = "cvReleaseImage(&$port[output_image]$);\n"
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/imageFile.py

        self.codes["execution"] = "\n"

        self.codes["deallocation"] = "$port[output_image]$.release();\n"

# -----------------------------------------------------------------------------