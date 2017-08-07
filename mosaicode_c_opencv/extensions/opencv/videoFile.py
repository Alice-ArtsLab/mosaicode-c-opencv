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
    # -------------------------------------------------------------------------

    def __init__(self):
        BlockModel.__init__(self)
        self.help = "Realiza a aquisição de uma imagem a partir " + \
            "de algum dispositivo," + \
            "seja este uma mídia ou um dispositivo " + \
            "de aquisição de imagens (câmera, scanner)."
        self.label = "Video File"
        self.color = "50:100:200:150"
        self.out_ports = [{"type":"mosaicode_c_opencv.extensions.ports.image",
                           "name":"output_image",
                           "label":"Output Image"}]
        self.group = "Image Source"

        self.properties = [{"name": "File Name",
                            "label": "filename",
                            "type": MOSAICODE_OPEN_FILE,
                            "value": "/usr/share/mosaicode/images/vLeft.mpg"
                            },
                           {"name": "Reset Key",
                            "label": "key",
                            "type": MOSAICODE_STRING,
                            "value": "a"
                            }
                           ]

        # -------------------C/OpenCv code------------------------------------
        self.codes["declaration"] = \
            'CvCapture * block$id$_capture = NULL;\n' + \
            'IplImage * block$id$_frame = NULL;\n' + \
            'block$id$_capture = cvCreateFileCapture("$filename$");\n' + \
            'IplImage * block$id$_img_o0 = NULL; //Capture\n'

        self.codes["execution"] = \
            '// Video Mode \n' + \
            'if(key == \'$key$\'){\n' +\
            '\tcvSetCaptureProperty(block$id$_capture, ' + \
            'CV_CAP_PROP_POS_AVI_RATIO , 0);\n' + \
            '}\n' + \
            'cvGrabFrame(block$id$_capture);\n' + \
            'block$id$_frame = cvRetrieveFrame (block$id$_capture);\n' + \
            'if(!block$id$_frame){\n' +\
            '\tcvSetCaptureProperty(block$id$_capture, ' + \
            'CV_CAP_PROP_POS_AVI_RATIO , 0);\n' + \
            '\tcontinue;\n' + \
            '}\n' + \
            'block$id$_img_o0 = cvCloneImage(block$id$_frame);\n'

        self.codes["deallocation"] = "cvReleaseImage(&block$id$_img_o0);\n"

        self.codes["cleanup"] = 'cvReleaseCapture(&block$id$_capture);\n'



        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
