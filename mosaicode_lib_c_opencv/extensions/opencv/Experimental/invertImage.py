#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the InvertImage class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class InvertImage(BlockModel):
	"""
	This class contains methods related the InvertImage class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Invert Image"
		self.color = "255:217:25:245"
		self.group = "Experimental"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Match Object Image",
						"conn_type":"Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
		]

# ---------------------------- C/OpenCV Code -------------------------------

		self.codes["declaration"] = \
"""
	Mat $port[input_image]$;
	Mat $port[output_image]$;
"""		

		self.codes["execution"] = \
"""
	if(!$port[input_image]$.empty()){
		flip($port[input_image]$, $port[output_image]$, 1);
	}
"""		
		self.codes["deallocation"] = \
"""
	$port[input_image]$.release();
	$port[output_image]$.release();
"""		

# --------------------------------------------------------------------------