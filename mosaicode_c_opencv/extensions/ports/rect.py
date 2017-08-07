from mosaicode.model.port import Port

class Rect(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "RCT"
        self.color = "#00F"
        self.multiple = False
        self.code = "block$sink$_rect_i$sink_port$ = block$source$_rect_o$source_port$;// RECT connection\n"
        self.input_codes["declaration"] = "CvRect block$id$_rect_i$port_number$ = cvRect( 0, 0, 1, 1);\n"
        self.output_codes["declaration"] = "CvRect block$id$_rect_o$port_number$ = cvRect( 0, 0, 1, 1);\n"
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation", "cleanup"]

