# -*- coding: utf-8 -*-
"""
This module contains the CTemplate class.
"""

from mosaicode.model.codetemplate import CodeTemplate

class Cfile(CodeTemplate):
    """
    This class contains methods related the CTemplate class.
    """

    def __init__(self):
        CodeTemplate.__init__(self)
        self.name = "opencv"
        self.language = "c"
        self.description = "c / opencv code template"
        self.extension = '.c'
        self.command = "export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/lib/;\n"
        self.command += "export PKG_CONFIG_PATH=/lib/pkgconfig/;\n"
        self.command += "g++ $filename$$extension$  -o $filename$ `pkg-config --cflags --libs opencv`\n"
        self.command += "LD_LIBRARY_PATH=/lib/ $dir_name$./$filename$"
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation"]

        self.code = r"""
        
// Auto-generated C Code - S2i Mosaicode
/*
*	In order to compile this source code run, in a terminal window, the following command:
*	gcc sourceCodeName.c `pkg-config --libs --cflags opencv` -o outputProgramName
*
*	the `pkg-config ... opencv` parameter is a inline command that returns the path to both
*	the libraries and the headers necessary when using opencv. The command also returns other necessary compiler options.
*/

#ifdef _CH_
#pragma package <opencv>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include "opencv2/core.hpp"
#include "opencv2/opencv.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/objdetect.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/features2d/features2d.hpp"

using namespace cv;
using namespace std;
$single_code[include]$
#define FRAMERATE 1000.0 / 25.0
$single_code[function]$

int main(int argc, char ** argv){
    char key = ' ';
    $code[declaration]$
    while((key = (char)waitKey(FRAMERATE)) != 27){
        $code[execution, connection]$
        $code[deallocation]$
    }
    
    destroyAllWindows();
    return 0;
}
"""
#----------------------------------------------------------------------
