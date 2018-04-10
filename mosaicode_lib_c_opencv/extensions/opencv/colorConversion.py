#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the ColorConversion class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class ColorConversion(BlockModel):
    """
    This class contains methods related the ColorConversion class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Realiza a conversão de cores entre diferentes " + \
            "padrões de imagens coloridas e tons de cinza."
        self.label = "Color Conversion"
        self.color = "50:125:50:150"
        self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "input_image",
                       "label": "Input Image",
                       "conn_type": "Input"},
                      {"type": "mosaicode_lib_c_opencv.extensions.ports.image",
                       "name": "output_image",
                       "label": "Output Image",
                       "conn_type": "Output"}]

        self.group = "Filters and Color Conversion"

        self.properties = [{"name": "conversion_type",
                            "label": "Conversion Type",
                            "type": MOSAICODE_COMBO,
                            "value": 'COLOR_RGB2GRAY',
                            "values": [
                                'COLOR_RGB2GRAY',
                                'COLOR_RGB2YCrCb',
                                'COLOR_YCrCb2RGB',
                                'COLOR_RGB2HSV',
                                'COLOR_HSV2BGR',
                                'COLOR_RGB2HLS',
                                'COLOR_HLS2RGB',
                                'COLOR_RGB2XYZ',
                                'COLOR_XYZ2RGB',
                                'COLOR_RGB2Lab',
                                'COLOR_Lab2RGB',
                                'COLOR_RGB2Luv',
                                'COLOR_Luv2RGB'
                            ]
                            }
                           ]

        # -----------------C/OpenCv code ---------------------------

        self.codes["declaration"] =  \
            'Mat $port[input_image]$;\n' + \
            'Mat $port[output_image]$;\n' + \
            'Mat block$id$_img_t;\n'

        self.codes["execution"] = \
            '\nif(!$port[input_image]$.empty()){\n' + \
            '$port[output_image]$ = $port[input_image]$.clone();\n' + \
            'Mat block$id$_img_t(Size($port[input_image]$.cols, ' + \
            '$port[input_image]$.rows), CV_8U);\n' + \
            'cvtColor($port[input_image]$, ' + \
            'block$id$_img_t, $prop[conversion_type]$);\n' + \
            '$port[output_image]$ = block$id$_img_t.clone();\n}\n'

        self.codes["deallocation"] = \
            'block$id$_img_t.release();\n' + \
            '$port[input_image]$.release();\n' + \
            '$port[output_image]$.release();\n'

# -----------------------------------------------------------------------------
