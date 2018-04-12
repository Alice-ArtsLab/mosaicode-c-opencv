from mosaicode.model.port import Port

class Rect(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "RCT"
        self.color = "#00F"
        self.multiple = False
        self.var_name = "b_$id$_$conn_type$_$port_number$"
        self.code = "$input$ = $output$;\n"
