#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Contrast class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Contrast(BlockModel):
	"""
	This class contains methods related the Contrast class.
	"""

	def __init__(self):
		BlockModel.__init__(self)
		
		self.language = "c"
		self.framework = "opencv"
		self.label = "Contrast"
		self.color = "50:125:50:150"
		self.group = "Filters and Conversions"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.int",
						"name": "contrast",
						"label": "Contrast",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
		]
		self.properties = [{"name": "contrast",
							"label": "Contrast",
							"type": MOSAICODE_INT,
							"value": 2,
							"step": 1
							}
		]

# --------------------------- C/OpenCV Code --------------------------- #

		self.codes["declaration"] = \
"""
	Mat $port[input_image]$;
	int $port[contrast]$ = $prop[contrast]$;
	Mat $port[output_image]$;
"""			

		self.codes["execution"] = \
"""
	if(!$port[input_image]$.empty()){
		$port[input_image]$.convertTo($port[output_image]$, -1, $port[contrast]$, 0);
	}
"""

		self.codes["deallocation"] = \
"""
	$port[input_image]$.release();
	$port[output_image]$.release();
"""

# --------------------------------------------------------------------- #