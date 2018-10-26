#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the AddBorder class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Histogram(BlockModel):
    """
    This class contains methods related the AddBorder class.
    """
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)

        self.language = "c"
        self.framework = "opencv"
        self.label = "Histogram"
        self.color = "150:180:210:150"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                    "name":"input_image",
                    "conn_type":"Input",
                    "label":"Input Image"},
                    {"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                    "name":"output_image",
                    "conn_type":"Output",
                    "label":"Output Image"}]
        self.group = "Experimental"
        self.properties = [{"name": "width",
                            "label": "Width",
                            "type": MOSAICODE_INT,
                            "lower": 256,
                            "upper": 1000,
                            "step": 1,
                            "value": 512
                            },
                           {"name": "height",
                            "label": "Height",
                            "type": MOSAICODE_INT,
                            "lower": 256,
                            "upper": 1000,
                            "step": 1,
                            "value": 400
                            }]

#-------------------------------- C/OpenCV Code -------------------------------------                           
    
        self.codes["declaration"] = \
"""        
    Mat $port[input_image]$;
    Mat $port[output_image]$;
    int histogram_$id$[256];
    Mat histogramImage_$id$($prop[height]$, $prop[width]$, CV_8UC1, Scalar(255, 255, 255));
"""        

        self.codes["execution"] = \
"""        
    if(!$port[input_image]$.empty()){
        for(int i = 0; i < 255; i++){
            histogram_$id$[i] = 0;
        }
        for(int i = 0; i < $port[input_image]$.rows; i++){
            for(int j = 0; j < $port[input_image]$.cols; j++){
                histogram_$id$[(int)$port[input_image]$.at<uchar>(i,j)]++;
            }
        }

        int max, bin_w = round((double) $prop[width]$/256);
        for(int i = 0; i < 256; i++){
            if(max < histogram_$id$[i]){
                max = histogram_$id$[i];
            }
        }
        for(int i = 0; i < 255; i++){
            histogram_$id$[i] = ((double)histogram_$id$[i]/max)*histogramImage_$id$.rows;
        }
        for(int i = 0; i < 255; i++){
            line(histogramImage_$id$, Point(bin_w*(i), $prop[height]$), Point(bin_w*(i), $prop[height]$ - histogram_$id$[i]), Scalar(0,0,0), 1, 8, 0);
        }
        $port[output_image]$ = histogramImage_$id$.clone();
    }
"""    

        self.codes["deallocation"] = \
"""        
    $port[input_image]$.release();
    histogramImage_$id$.release();
"""

# -----------------------------------------------------------------------------