#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Show class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Show(BlockModel):
    """
    This class contains methods related the Show class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.language = "c"
        self.framework = "opencv"
        self.help = "Mostra uma imagem da cadeia de processamento de imagens."
        self.label = "Show Image"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"}
                         ]
        self.group = "General"
        self.properties = [{"label": "Window Title",
                            "name": "title",
                            "type": MOSAICODE_STRING,
                            "value":"My Image"
                            },
                           {"label": "Window Type",
                            "name": "window_type",
                            "type": MOSAICODE_COMBO,
                            "values": ["WINDOW_AUTOSIZE",
                                       "WINDOW_NORMAL"],
                            "value":"WINDOW_AUTOSIZE"
                            }
                           ]

# ----------------------------C/OpenCv code-------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    if(strcmp(\"WINDOW_NORMAL\", \"$prop[window_type]$\") == 0)
        namedWindow(\"$prop[title]$\", WINDOW_NORMAL);
    else
        namedWindow(\"$prop[title]$\", WINDOW_AUTOSIZE);
"""

        self.codes["execution"] = \
"""
    if(!$port[input_image]$.empty()){
        imshow(\"$prop[title]$\", $port[input_image]$);
    }
"""
        
        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
"""            

# -----------------------------------------------------------------------------