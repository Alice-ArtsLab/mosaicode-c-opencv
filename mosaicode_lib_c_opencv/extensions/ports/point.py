from mosaicode.model.port import Port

class Point(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "POINT"
        self.color = "#0FF"
        self.multiple = False
        self.var_name = "b_$id$_$conn_type$_$port_number$"
        self.code = "$input$ = $output$;\n"