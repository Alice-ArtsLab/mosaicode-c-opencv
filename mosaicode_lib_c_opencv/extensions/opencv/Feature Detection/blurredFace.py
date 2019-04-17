#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the BlurredFace class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class BlurredFace(BlockModel):
    """
    This class contains methods related the BlurredFace class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Blurred Face"
        self.color = "0:204:34:215"
        self.group = "Feature Detection"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"input_image",
                      "label":"Input Image",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"input_integer1",
                      "label":"Input Integer 1",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                      "name":"input_integer2",
                      "label":"Input Integer 2",
                      "conn_type":"Input"},
                      {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                      "name":"output_image",
                      "label":"Output Image",
                      "conn_type":"Output"}
                      ]
        self.properties = [{"name": "integer1",
                            "label": "Sigma A",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 8
                            },
                           {"name": "integer2",
                            "label": "Sigma B",
                            "type": MOSAICODE_INT,
                            "lower": 0,
                            "upper": 99,
                            "step": 1,
                            "value": 8
                            }
                           ]

#-------------------------------- C/OpenCv Code ------------------------------------

        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    Mat tmp$id$;
    int $port[input_integer1]$ = $prop[integer1]$;
    int $port[input_integer2]$ = $prop[integer2]$;
    CascadeClassifier cascade_$id$("/usr/share/mosaicode/extensions/c-opencv/databases/haarcascade_frontalface_alt2.xml");
    vector<Rect> faces_$id$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
        $port[input_integer1]$ = ($port[input_integer1]$ %2 == 0)? $port[input_integer1]$ + 1 : $port[input_integer1]$;
        $port[input_integer2]$ = ($port[input_integer2]$ %2 == 0)? $port[input_integer2]$ + 1 : $port[input_integer2]$;
        cascade_$id$.detectMultiScale($port[input_image]$, faces_$id$, 1.1, 3, 0|CV_HAAR_SCALE_IMAGE, Size(0, 0));
        for(int i = 0; i < faces_$id$.size(); i++){
            rectangle($port[input_image]$, faces_$id$[i], Scalar(0, 0, 0), 1, 8, 0);
            Rect region(faces_$id$[i].x, faces_$id$[i].y, faces_$id$[i].width, faces_$id$[i].height);
            tmp$id$ = $port[input_image]$(region);
            GaussianBlur(tmp$id$, tmp$id$, Size(0,0), $port[input_integer1]$, $port[input_integer2]$);
            tmp$id$.copyTo($port[output_image]$(Rect(faces_$id$[i].x, faces_$id$[i].y, faces_$id$[i].width, faces_$id$[i].height)));  
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
    tmp$id$.release();
"""    

# -----------------------------------------------------------------------------
