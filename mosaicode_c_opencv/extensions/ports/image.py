from mosaicode.model.port import Port

class Image(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "IMG"
        self.color = "#F0F"
        self.multiple = False
        self.code = "block$sink$_i$sink_port$ = cvCloneImage(block$source$_o$source_port$);\n"
        self.var_name = "block$id$_$conn_type$$port_number$"
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation", "cleanup"]

