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
        self.help = "Mostra uma imagem da cadeia de processamento de imagens."
        self.label = "Show Image"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
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

        self.codes["declaration"] = "IplImage * $port[input_image]$ = NULL;\n" + \
                "if (strcmp(\"Window Size\", \"$prop[window_type]$\") == 0)\n" + \
                "cvNamedWindow(\"$prop[title]$\",CV_WINDOW_NORMAL);\n" + \
                "else\n" + \
                "cvNamedWindow(\"$prop[title]$\",CV_WINDOW_AUTOSIZE);\n"

        self.codes["execution"] = "\nif($port[input_image]$){\n" + \
            "cvShowImage(\"$prop[title]$\",$port[input_image]$);\n" + \
            "if (strcmp(\"Window Size\", \"$prop[window_type]$\") == 0)\n" + \
            "cvSetWindowProperty(\"$prop[title]$\", " + \
            "CV_WND_PROP_FULLSCREEN, CV_WINDOW_FULLSCREEN);\n" + \
            "}\n"

        self.codes["deallocation"] = "cvReleaseImage(&$port[input_image]$);"


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
