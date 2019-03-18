#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Brightness class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class Brightness(BlockModel):
	"""
	This class contains methods related the Brightness class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Brightness"
		self.color = "50:125:50:150"
		self.group = "Filters and Color Conversion"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.int",
						"name": "brightness",
						"label": "Brightness",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
		]
		self.properties = [{"name": "brightness",
							"label": "Brightness",
							"type": MOSAICODE_INT,
							"value": 50,
							"step": 1
							}
		]

# --------------------------- C/OpenCV Code --------------------------- #

		self.codes["declaration"] = \
"""
	Mat $port[input_image]$;
	int $port[brightness]$ = $prop[brightness]$;
	Mat $port[output_image]$;
"""			

		self.codes["execution"] = \
"""
	if(!$port[input_image]$.empty()){
		$port[input_image]$.convertTo($port[output_image]$, -1, 1, $port[brightness]$);
	}
"""

		self.codes["deallocation"] = \
"""
	$port[input_image]$.release();
	$port[output_image]$.release();
"""

# --------------------------------------------------------------------- #