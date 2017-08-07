from mosaicode.model.port import Port

class Int(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "INT"
        self.color = "#F00"
        self.multiple = False
        self.code = "block$sink$_int_i$sink_port$ = block$source$_int_o$source_port$;// INT connection\n"
        self.input_codes["declaration"] = "int block$id$_int_i$port_number$ = 0;\n"
        self.output_codes["declaration"] = "int block$id$_int_o$port_number$ = 0;\n"
        self.code_parts = ["include", "function", "declaration", "execution", "deallocation", "cleanup"]

