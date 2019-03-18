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

        self.language = "c"
        self.framework = "opencv"
        self.label = "Resize Image"
        self.color = "20:80:10:150"
        self.group = "Experimental"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]
        self.properties = [{"label": "Tamanho em X",
                            "name": "size_x",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000,
                            "step": 1
                            },
                            {"label": "Tamanho em Y",
                            "name": "size_y",
                            "type": MOSAICODE_INT,
                            "value": 1,
                            "lower": 1,
                            "upper": 5000,
                            "step": 1
                            }
                           ]

#-------------------------------- C/OpenCV Code ------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        resize($port[input_image]$, $port[output_image]$, Size($prop[size_x]$, $prop[size_y]$));
    }
"""

        self.codes["deallocation"] = \
"""
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------