#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Sobel class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class LiveMode(BlockModel):
	"""
	This class contains methods related the FaceDetection class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Live Mode"
		self.color = "50:100:200:150"
		self.group = "Image Source"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type": "Output"}
		]

# --------------------------- C/OpenCV Code --------------------------- #

		self.codes["declaration"] = \
"""
	Mat $port[output_image]$;
	VideoCapture capture$id$(0);
"""

		self.codes["execution"] = \
"""		
	if(!capture$id$.isOpened())
        return -1;
	capture$id$ >> $port[output_image]$;
"""

		self.codes["deallocation"] = \
"""		
	$port[output_image]$.release();
"""

# --------------------------------------------------------------------- #					