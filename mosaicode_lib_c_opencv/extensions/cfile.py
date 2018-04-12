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
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation", "cleanup"]

        self.code = r"""
// Auto-generated C Code - S2i Mosaicode
/*
*	In order to compile this source code run, in a terminal window, the following command:
*	gcc sourceCodeName.c `pkg-config --libs --cflags opencv` -o outputProgramName
*
*	the `pkg-config ... opencv` parameter is a inline command that returns the path to both
*	the libraries and the headers necessary when using opencv. The command also returns other necessary compiler options.
*/

// header:

#ifdef _CH_
#pragma package <opencv>
#endif

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
<<<<<<< HEAD:mosaicode_c_opencv/extensions/cfile.py
#include "opencv2/core.hpp"
#include "opencv2/opencv.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/objdetect.hpp"

using namespace cv;
using namespace std;

=======
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/cfile.py
$single_code[include]$

#define FRAMERATE 1000.0 / 25.0

$single_code[function]$

int main(int argc, char ** argv){
        char key = ' ';
        //declaration block
        $code[declaration]$
        while((key = (char)cvWaitKey(FRAMERATE)) != 27){
            //execution block
            $code[execution, connection]$

            //deallocation block
            $code[deallocation]$

        } // End of while
    $code[cleanup]$

return 0;

} //closing main()
"""
#----------------------------------------------------------------------
