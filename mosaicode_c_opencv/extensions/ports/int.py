from mosaicode.model.port import Port

class Int(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "INT"
        self.color = "#F00"
        self.multiple = False
        self.code = "$input$ = $output$;\n"
        self.var_name = "block$id$_$conn_type$$port_number$"

