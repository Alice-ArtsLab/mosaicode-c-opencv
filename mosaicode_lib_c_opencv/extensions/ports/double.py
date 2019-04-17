from mosaicode.model.port import Port

class Double(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "DOUBLE"
        self.color = "#292B23"
        self.multiple = False
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
        self.code = "$input$ = $output$;\n"