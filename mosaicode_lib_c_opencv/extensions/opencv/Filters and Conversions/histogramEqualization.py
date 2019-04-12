#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Histogram Equalization class.
"""

from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel

class HistogramEqualization(BlockModel):
	"""
	This class contains methods related the HistogramEqualization class.
	"""

	def __init__(self):
		BlockModel.__init__(self)

		self.language = "c"
		self.framework = "opencv"
		self.label = "Histogram Equalization"
		self.color = "50:125:50:150"
		self.group = "Filters and Conversions"
		self.ports = [{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "input_image",
						"label": "Input Image",
						"conn_type": "Input"},
						{"type": "mosaicode_lib_c_opencv.extensions.ports.image",
						"name": "output_image",
						"label": "Output Image",
						"conn_type":"Output"}
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