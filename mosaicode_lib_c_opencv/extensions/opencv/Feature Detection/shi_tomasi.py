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
		self.label = "Shi Tomasi Corner Detector"
		self.color = "50:220:40:150"
		self.group = "Feature Detection"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type":"Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
		]
		self.properties = [{"name": "max_corners",
							"label": "Max corners",
							"type": MOSAICODE_INT,
							"value": 23,
							"step": 1,
							"lower": 1
							}
		]

# --------------------------- C/OpenCV Code --------------------------- #

		self.codes["declaration"] = \
"""
	Mat $port[input_image]$;
	Mat $port[output_image]$;
	Mat Mat_tmp_$id$;
	RNG rng(12345);
"""			

		self.codes["execution"] = \
"""
	if(!$port[input_image]$.empty()){
		cvtColor($port[input_image]$, Mat_tmp_$id$, COLOR_BGR2GRAY);
		$port[output_image]$ = $port[input_image]$.clone();
		vector<Point2f> corners;
		goodFeaturesToTrack(Mat_tmp_$id$, corners, $prop[max_corners]$, 0.01, 10, Mat(), 3, false, 0.04);
		for(int i = 0; i < corners.size(); i++){ 
			circle($port[output_image]$, corners[i], 5, Scalar(rng.uniform(0,255), rng.uniform(0,255), rng.uniform(0,255)), -1, 8, 0); 
		}
	}
"""

		self.codes["deallocation"] = \
"""
	$port[input_image]$.release();
	$port[output_image]$.release();
	Mat_tmp_$id$.release();
"""

# --------------------------------------------------------------------- #