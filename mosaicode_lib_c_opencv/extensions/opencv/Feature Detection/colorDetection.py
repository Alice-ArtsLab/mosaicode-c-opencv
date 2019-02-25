#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Color Detection class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ColorDetection(BlockModel):
	"""
	This class contains methods related the ColorDetection class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Color Detection"
		self.color = "50:220:40:150"
		self.group = "Feature Detection"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type": "Output"}
		]
		self.properties = [{"name": "color",
                            "label": "Color",
                            "type": MOSAICODE_COMBO,
                            "value": "Red",
                            "values":["Red",
                                    "Blue",
                                    "Green",
                                    "Yellow",
                                    "Orange"
                            ]
                            }
		]

# ------------------------------------- C/OpenCV Code -------------------------------------

		self.codes["function"] = \
"""		
    Scalar get_scalar_color(const char * rgbColor){
    	if(strlen(rgbColor) < 13 || rgbColor[0] != '#')
        	return Scalar(0,0,0,0);

        char r[4], g[4], b[4];
        strncpy(r, rgbColor+1, 4);
        strncpy(g, rgbColor+5, 4);
        strncpy(b, rgbColor+9, 4);
        
        int ri, gi, bi = 0;
        ri = (int)strtol(r, NULL, 16);
        gi = (int)strtol(g, NULL, 16);
        bi = (int)strtol(b, NULL, 16);
        
        ri /= 257;
        gi /= 257;
        bi /= 257;
        
        return Scalar(bi, gi, ri, 0);
    }
"""

		self.codes["declaration"] = \
"""
	Mat $port[input_image]$;
	Mat $port[output_image]$;
    Mat temp_image$id$, mask$id$, high_mask$id$, low_mask$id$;
"""

		self.codes["execution"] = \
"""		
	if(!$port[input_image]$.empty()){
        cvtColor($port[input_image]$, temp_image$id$, COLOR_BGR2HSV);
        if("$prop[color]$" == "Red"){
            inRange(temp_image$id$, Scalar(161, 100, 100), Scalar(179, 255, 255), high_mask$id$);
            inRange(temp_image$id$, Scalar(0, 100, 100), Scalar(5, 255, 255), low_mask$id$);
            bitwise_or(low_mask$id$, high_mask$id$, mask$id$);            
        } else if("$prop[color]$" == "Blue"){
            inRange(temp_image$id$, Scalar(99, 100, 100), Scalar(126, 255, 255), mask$id$);
        } else if("$prop[color]$" == "Green"){
            inRange(temp_image$id$, Scalar(44, 100, 50), Scalar(75, 255, 255), mask$id$);
        } else if("$prop[color]$" == "Yellow"){
            inRange(temp_image$id$, Scalar(18, 0, 196), Scalar(36, 255, 255), mask$id$);
        } else if("$prop[color]$" == "Orange"){
            inRange(temp_image$id$, Scalar(7, 70, 50), Scalar(25, 255, 255), mask$id$);
        }
        bitwise_and($port[input_image]$, $port[input_image]$, $port[output_image]$, mask$id$);
	}
"""

		self.codes["deallocation"] = \
"""		
	$port[input_image]$.release();
	$port[output_image]$.release();
    temp_image$id$.release();
    mask$id$.release();
"""

# --------------------------------------------------------------------- #					