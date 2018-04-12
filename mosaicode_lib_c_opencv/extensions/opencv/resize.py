#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Resize class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Resize(BlockModel):
    """
    This class contains methods related the Resize class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        # Appearance
        self.help = "Resizes the input image to the " + \
            "dimensions of the input rectangle."
        self.label = "Resize Image"
        self.color = "20:80:10:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/resize.py
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
=======
                          "name":"input",
                          "conn_type":"Input",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.rect",
                          "name":"size",
                          "conn_type":"Input",
                          "label":"Size"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output",
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/resize.py
                          "conn_type":"Output",
                          "label":"Output Image"}]

        self.group = "Experimental"

        self.properties = [{"label": "Tamanho em X",
                            "name": "size_x",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000
                            },
                            {"label": "Tamanho em Y",
                            "name": "size_y",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000
                            }
                           ]

<<<<<<< HEAD:mosaicode_c_opencv/extensions/opencv/resize.py
        self.codes["declaration"] = \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Size size$id$;\n' 
=======
        self.codes["execution"] = \
            'if($port[input]$){\n' + \
            'CvSize size$id$ = cvSize($port[size]$.width,' + \
            '$port[size]$.height);\n' + \
            '$port[output]$ = cvCreateImage(size$id$, ' + \
            '$port[input]$->depth,$port[input]$->nChannels);\n' + \
            'cvResize($port[input]$, $port[output]$, $prop[method]$);\n' + \
            '}\n'
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/opencv/resize.py

        self.codes["execution"] = \
            'if(!$port[input_image]$.empty()){\n' + \
            'size$id$ = Size($prop[size_x]$,' + \
            '$prop[size_y]$);\n' + \
            'resize($port[input_image]$, $port[output_image]$, size$id$);\n' + \
            '}\n'

        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
