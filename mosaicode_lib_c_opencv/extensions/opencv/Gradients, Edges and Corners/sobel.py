#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Sobel class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Sobel(BlockModel):
    """
    This class contains methods related the Sobel class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        # Appearance
        self.language = "c"
        self.framework = "opencv"
        self.help = "Operação de filtragem que utiliza uma máscara " + \
            "Sobel para realçar cantos e bordas da imagem."
        self.label = "Sobel"
        self.color = "250:180:80:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"},
                        {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"output_image",
                        "label":"Output Image",
                        "conn_type":"Output"}]
        self.group = "Gradients, Edges and Corners"
        self.properties = [{"name": "order",
                            "label": "Derivate Order",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 6,
                            "step": 1,
                            "value": 3
                            }
                           ]

# ------------------------------- C/OpenCv Code ------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Mat block$id$_img_t, grad_x;
    double minVal, maxVal;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        cvtColor($port[input_image]$, block$id$_img_t, CV_RGB2GRAY);
        Sobel(block$id$_img_t, grad_x, CV_32F, 1, 0);
        minMaxLoc(grad_x, &minVal, &maxVal);
        grad_x.convertTo($port[output_image]$, CV_8U, 255.0/(maxVal - minVal), -minVal * 255.0/(maxVal - minVal));
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[output_image]$.release();
    $port[input_image]$.release();
    block$id$_img_t.release();
"""            

# -----------------------------------------------------------------------------