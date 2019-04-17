#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Canny class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Canny(BlockModel):
    """
    This class contains methods related the Canny class.
    """

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Canny"
        self.color = "0:138:64:245"
        self.framework = "opencv"
        self.group = "Gradients, Edges and Corners"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                          "name":"input_image",
                          "conn_type":"Input",
                          "label":"Input Image"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_apertureSize",
                          "label":"Aperture Size"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold1",
                          "label":"Threshold 1"},
                          {"type":"mosaicode_lib_c_opencv.extensions.ports.int",
                          "conn_type":"Input",
                          "name":"input_threshold2",
                          "label":"Threshold 2"},
                         {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                          "label":"Output Image"}]
        self.properties = [{"label": "Aperture Size",
                            "name": "apertureSize",
                            "type": MOSAICODE_INT,
                            "lower": 3,
                            "upper": 7,
                            "value":5,
                            "step": 1
                            },
                           {"label": "Threshold 1",
                            "name": "threshold1",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 100,
                            "value": 16,
                            "step": 1
                            },
                           {"label": "Threshold 2",
                            "name": "threshold2",
                            "type": MOSAICODE_INT,
                            "lower": 1,
                            "upper": 100,
                            "value": 33,
                            "step": 1
                            }
                           ]

# ----------------------------------- C/OpenCV Code -------------------------------------
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    int $port[input_apertureSize]$ = $prop[apertureSize]$;
    int $port[input_threshold1]$ = $prop[threshold1]$;
    int $port[input_threshold2]$ = $prop[threshold2]$;
"""    

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        if($port[input_apertureSize]$ < 1) $port[input_apertureSize]$ = 1;
        if($port[input_threshold1]$ < 1) $port[input_threshold1]$ = 1;
        if($port[input_threshold2]$ < 1) $port[input_threshold2]$ = 1;
        if($port[input_apertureSize]$ > 10) $port[input_apertureSize]$ = 10;
        if($port[input_threshold1]$ > 100) $port[input_threshold1]$ = 100;
        if($port[input_threshold2]$ > 100) $port[input_threshold2]$ = 100;
        $port[output_image]$ = $port[input_image]$.clone();
        Mat tmp_$id$($port[input_image]$.rows,$port[input_image]$.cols,CV_8U);
        if($port[input_image]$.channels() == 3){
            cvtColor($port[input_image]$, tmp_$id$, COLOR_RGB2GRAY);
        }else{
            tmp_$id$ = $port[input_image]$ = Mat::zeros($port[input_image]$.cols, $port[input_image]$.rows, CV_8UC1);
        }
        Canny(tmp_$id$, tmp_$id$, $port[input_threshold1]$, $port[input_threshold2]$, $port[input_apertureSize]$);
        if($port[input_image]$.channels() == 3){
            cvtColor(tmp_$id$, $port[output_image]$,COLOR_GRAY2RGB);
        }else{
            $port[output_image]$ = tmp_$id$.clone();
        }
    }
"""

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    $port[output_image]$.release();
"""

# -----------------------------------------------------------------------------
