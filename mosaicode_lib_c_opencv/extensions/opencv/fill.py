#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Fill class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Fill(BlockModel):
    """
    This class contains methods related the Fill class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"

        # Appearance
        self.help = "Preenche toda a imagem de uma cor."
        self.label = "Fill image"
        self.color = "50:100:200:150"
        self.ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"input_image",
                       "label":"Input Image",
                       "conn_type":"Input"},
                      {"type":"mosaicode_c_opencv.extensions.ports.image",
                       "name":"output_image",
                       "label":"Output Image",
                       "conn_type":"Output"}]

        self.group = "General"
        
        self.properties = [{"name": "rect_color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value":"#DDDDDD"
                            }
                           ]
'''
        # ------------------------------C/OpenCv code--------------------------
        self.codes["declaration"] = \
            'IplImage * $port[input_image]$ = NULL;\n' + \
            'IplImage * $port[output_image]$ = NULL;\n'  

        self.codes["function"] = \
            red = rect_color[1:5]
            green = rect_color[5:9]
            blue = rect_color[9:13]

            red = int(red, 16) / 257
            green = int(green, 16) / 257
            blue = int(blue, 16) / 257
                
            return \
                'if($port[input_image]$){\n' + \
                '\$port[output_image]$ = cvCloneImage($port[input_image]$);\n' + \
                '\tCvScalar color = cvScalar' + \
                '(' + str(blue) + ',' + str(green) + ',' + str(red) + ',0);\n' + \
                '\tcvSet($port[input_image]$, color, NULL);\n' + \
                '}\n'

        self.codes["deallocation"] = \
            'cvReleaseImage(&$port[input_image]$);\n' + \
            'cvReleaseImage(&$port[output_image]$);\n' 

# -----------------------------------------------------------------------------
'''
