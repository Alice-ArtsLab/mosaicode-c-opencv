#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Sobel class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class FaceDetection(BlockModel):
	"""
	This class contains methods related the FaceDetection class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Face Detection"
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
		self.properties = [{"name": "drawing",
							"label": "Drawing",
							"type": MOSAICODE_COMBO,
							"value": "Rectangle",
							"values":["Ellipse",
									  "Rectangle"]
							},
							{"name": "color",
                            "label": "Color",
                            "type": MOSAICODE_COLOR,
                            "value": "#DDDDDD"
                            },
                            {"label": "Thickness",
                            "name": "thickness",
                            "type": MOSAICODE_INT,
                            "value": 5,
                            "step": 1,
                            "upper": 20,
                            "lower": 1
                            },
                            {"label": "Degree of Increase",
                            "name": "degree",
                            "type": MOSAICODE_FLOAT,
                            "value": 1.00,
                            "step": 0.01
                            }
		]

# --------------------------- C/OpenCV Code --------------------------- #

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
	//Face detection
	Mat $port[input_image]$;
	Mat $port[output_image]$;
	CascadeClassifier face_cascade_$id$;
"""

		self.codes["execution"] = \
"""		
	if(!$port[input_image]$.empty()){
		Scalar color = get_scalar_color("$prop[color]$");
		face_cascade_$id$.load("/opt/opencv/data/haarcascades/haarcascade_frontalface_alt.xml");
		vector<Rect> faces;
		face_cascade_$id$.detectMultiScale($port[input_image]$, faces, 1.1, 3, 0|CV_HAAR_SCALE_IMAGE, Size(0, 0));
		for(int i = 0; i < faces.size(); i++){
			if("$prop[drawing]$" == "Ellipse"){
				Point center(faces[i].x + faces[i].width*0.5, faces[i].y + faces[i].height*0.5);
				ellipse($port[input_image]$, center, Size(faces[i].width*$prop[degree]$, faces[i].height*$prop[degree]$), 0, 0, 360, color, $prop[thickness]$, 8, 0);
			}
			else if("$prop[drawing]$" == "Rectangle")
				rectangle($port[input_image]$, faces[i], color, $prop[thickness]$, 8, 0);	
		}
		$port[output_image]$ = $port[input_image]$.clone();
	}
"""

		self.codes["deallocation"] = \
"""		
	$port[input_image]$.release();
	$port[output_image]$.release();
"""

# --------------------------------------------------------------------- #					