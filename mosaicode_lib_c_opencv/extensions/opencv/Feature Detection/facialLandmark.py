#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the FacialLandmark class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class FacialLandmark(BlockModel):
	"""
	This class contains methods related the FacialLandmark class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Facial Landmark"
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
                            "type": MOSAICODE_COLOR,
                            "value": "#DDDDDD"
                            },
                            {"label": "Radius",
                            "name": "radius",
                            "type": MOSAICODE_INT,
                            "value": 3,
                            "step": 1,
                            "upper": 20,
                            "lower": 1
                            }
		]

# ------------------------------------- C/OpenCV Code -------------------------------------

		self.codes["function"] = \
"""		
    Scalar get_scalar_color$id$(const char * rgbColor){
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
    Mat tmp_$id$;
    vector<Rect> faces_$id$;
    vector< vector<Point2f> > landmarks_$id$;
	CascadeClassifier face_cascade_$id$;
    Ptr<Facemark> facemark_$id$ = FacemarkLBF::create();
"""

		self.codes["execution"] = \
"""		
	if(!$port[input_image]$.empty()){
		Scalar color = get_scalar_color$id$("$prop[color]$");
		face_cascade_$id$.load("/usr/share/mosaicode/extensions/c-opencv/databases/haarcascade_frontalface_alt.xml");
		facemark_$id$->loadModel("/usr/share/mosaicode/extensions/c-opencv/databases/lbfmodel.yaml");
        cvtColor($port[input_image]$, tmp_$id$, COLOR_BGR2GRAY);
        face_cascade_$id$.detectMultiScale(tmp_$id$, faces_$id$);
        $port[output_image]$ = $port[input_image]$.clone();
		if(facemark_$id$->fit($port[input_image]$, faces_$id$, landmarks_$id$)){
            for(int i = 0; i < faces_$id$.size(); i++){
                for(int j = 0; j < landmarks_$id$[i].size(); j++)
                    circle($port[output_image]$, landmarks_$id$[i][j], $prop[radius]$, color, FILLED);
            }
		}
	}
"""

		self.codes["deallocation"] = \
"""		
	$port[input_image]$.release();
	$port[output_image]$.release();
    tmp_$id$.release();
"""

# --------------------------------------------------------------------- #					