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

        self.language = "c"
        self.framework = "opencv"

        # Appearance
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
                            "values": ["Window Size",
                                       "Image Size"],
                            "value":"Image Size"
                            }
                           ]

# ----------------------------C/OpenCv code-------------------------

        self.codes["declaration"] = "Mat $port[input_image]$;\n" + \
            "if (strcmp(\"Window Size\", \"$prop[window_type]$\") == 0)\n" + \
            "namedWindow(\"$prop[title]$\",WINDOW_NORMAL);\n" + \
            "else\n" + \
            "namedWindow(\"$prop[title]$\",WINDOW_AUTOSIZE);\n"

        self.codes["execution"] = "\nif(!$port[input_image]$.empty()){\n" + \
            "imshow(\"$prop[title]$\",$port[input_image]$);\n" + \
            "if (strcmp(\"Window Size\", \"$prop[window_type]$\") == 0)\n" + \
            "cvSetWindowProperty(\"$prop[title]$\", " + \
            "CV_WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN);\n" + \
            "}\n"

        self.codes["deallocation"] = "$port[input_image]$.release();"

# -----------------------------------------------------------------------------