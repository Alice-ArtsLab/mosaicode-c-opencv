from mosaicode.model.port import Port

class Image(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "IMG"
        self.color = "#F0F"
        self.multiple = False
        self.code = "// IMG connection\n"
        self.code += "block$sink$_img_i$sink_port$ = cvCloneImage(block$source$_img_o$source_port$);\n"
        self.input_codes["declaration"] = "IplImage * block$id$_img_i$port_number$ = NULL;\n"
        self.output_codes["declaration"] = "IplImage * block$id$_img_o$port_number$ = NULL;\n"
        self.input_codes["deallocation"] = "cvReleaseImage(&block$id$_img_i$port_number$);\n"
        self.output_codes["deallocation"] = "cvReleaseImage(&block$id$_img_o$port_number$);\n"
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation", "cleanup"]

