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

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Save Image"
        self.color = "50:100:200:150"
        self.group = "General"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                        "name":"input_image",
                        "label":"Input Image",
                        "conn_type":"Input"}
                        ]
        self.properties = [{"name": "filename",
                            "label": "File Name",
                            "type": MOSAICODE_SAVE_FILE
                            }
                           ]

#------------------------------------ C/OpenCv Code --------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
"""

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        imwrite("$prop[filename]$", $port[input_image]$);
    }            
"""

        self.codes["deallocation"] = \
"""
    $port[input_image]$.release();
"""

# ----------------------------------------------------------------------------------------