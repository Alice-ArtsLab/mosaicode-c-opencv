#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Shape Detection class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class ShapeDetection(BlockModel):
	"""
	This class contains methods related the ShapeDetection class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Shape Detection"
		self.color = "50:220:40:150"
		self.group = "Feature Detection"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type": "Output"},
                        {"type": "mosaicode_lib_c_opencv.extensions.ports.point",
						"name": "output_points",
						"label": "Output Point",
						"conn_type": "Output"}
		]
		self.properties = [{"name": "triangle_color",
                            "label": "Triangle color",
                            "type": MOSAICODE_COLOR,
                            "value": "#BBBBBB"
                            },
                            {"name": "square_color",
                            "label": "Square color",
                            "type": MOSAICODE_COLOR,
                            "value": "#CCCCCC"
                            },
                            {"name": "polygon_color",
                            "label": "Polygon color",
                            "type": MOSAICODE_COLOR,
                            "value": "#DDDDDD"
                            },
                            {"name": "semi_color",
                            "label": "Semicircle color",
                            "type": MOSAICODE_COLOR,
                            "value": "#EEEEEE"
                            },
                            {"name": "circle_color",
                            "label": "Circle color",
                            "type": MOSAICODE_COLOR,
                            "value": "#FFFFFF"
                            },
                            {"label": "Thickness",
                            "name": "thickness",
                            "type": MOSAICODE_INT,
                            "value": 2,
                            "step": 1,
                            "upper": 20,
                            "lower": 1
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
	vector<vector<Point> > $port[output_points]$;
    vector<Point> approx_$id$;
"""

		self.codes["execution"] = \
"""		
	if(!$port[input_image]$.empty()){
        $port[output_image]$ = $port[input_image]$.clone();
		cvtColor($port[input_image]$, $port[input_image]$, COLOR_BGR2GRAY);
        threshold($port[input_image]$, $port[input_image]$, 127, 255, CV_THRESH_BINARY);
        findContours($port[input_image]$, $port[output_points]$, RETR_TREE, CHAIN_APPROX_SIMPLE);
        for(int i = 0; i < $port[output_points]$.size(); i++){
            approxPolyDP($port[output_points]$[i], approx_$id$, 0.02*arcLength($port[output_points]$[i], true), true);
            if(approx_$id$.size() == 3){
                drawContours($port[output_image]$, $port[output_points]$, i, get_scalar_color("$prop[triangle_color]$"), $prop[thickness]$, 8);
            }
            if(approx_$id$.size() == 4){
                drawContours($port[output_image]$, $port[output_points]$, i, get_scalar_color("$prop[square_color]$"), $prop[thickness]$, 8);
            }
            if(approx_$id$.size() >= 5 && approx_$id$.size() < 9){
                drawContours($port[output_image]$, $port[output_points]$, i, get_scalar_color("$prop[polygon_color]$"), $prop[thickness]$, 8);
            }
            if(approx_$id$.size() == 9){
                drawContours($port[output_image]$, $port[output_points]$, i, get_scalar_color("$prop[semi_color]$"), $prop[thickness]$, 8);
            }
            if(approx_$id$.size() > 11){
                drawContours($port[output_image]$, $port[output_points]$, i, get_scalar_color("$prop[circle_color]$"), $prop[thickness]$, 8);
            }
        }
	}
"""

		self.codes["deallocation"] = \
"""		
	$port[input_image]$.release();
	$port[output_image]$.release();
"""

# --------------------------------------------------------------------- #					