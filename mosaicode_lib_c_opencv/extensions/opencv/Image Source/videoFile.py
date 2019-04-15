#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the VideoFile class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class VideoFile(BlockModel):
    """
    This class contains methods related the VideoFile class.
    """

    def __init__(self):
        BlockModel.__init__(self)
        self.label = "Video File"
        self.color = "0:213:255:255"
        self.language = "c"
        self.framework = "opencv"
        self.ports = [{"type":"mosaicode_lib_c_opencv.extensions.ports.image",
                           "name":"output_image",
                          "conn_type":"Output",
                           "label":"Output Image"}]
        self.group = "Image Source"
        self.properties = [{"name": "filename",
                            "label": "File Name",
                            "type": MOSAICODE_OPEN_FILE,
                            "value": "/usr/share/mosaicode/images/vLeft.mpg"
                            },
                           {"name": "key",
                            "label": "Reset Key",
                            "type": MOSAICODE_STRING,
                            "size":1,
                            "value": "a"
                            }
                           ]

# -------------------C/OpenCv code------------------------------------

        self.codes["declaration"] = \
"""        
    CvCapture * block$id$_capture = NULL;
    IplImage * block$id$_frame = NULL;
    block$id$_capture = cvCreateFileCapture("$prop[filename]$");
    IplImage * $port[output_image]$ = NULL;
"""

        self.codes["execution"] = \
"""        
    if(key == \'$prop[key]$\'){
        cvSetCaptureProperty(block$id$_capture, CV_CAP_PROP_POS_AVI_RATIO , 0);
    }
    cvGrabFrame(block$id$_capture);
    block$id$_frame = cvRetrieveFrame (block$id$_capture);
    if(!block$id$_frame){
        cvSetCaptureProperty(block$id$_capture, CV_CAP_PROP_POS_AVI_RATIO , 0);
        continue;
    }
    $port[output_image]$ = cvCloneImage(block$id$_frame);
"""
        self.codes["deallocation"] = \
"""
    cvReleaseImage(&$port[output_image]$);
"""        
        self.codes["cleanup"] = \
"""
        cvReleaseCapture(&block$id$_capture);\n'
"""
        
# -----------------------------------------------------------------------------
