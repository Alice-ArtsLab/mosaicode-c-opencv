from mosaicode.model.port import Port

class Double(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "DOUBLE"
        self.color = "#000"
        self.multiple = False
        self.var_name = "b_$id$_$conn_type$_$port_number$"
        self.code = "$input$ = $output$;\n"

