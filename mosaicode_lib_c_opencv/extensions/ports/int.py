from mosaicode.model.port import Port

class Int(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "INT"
        self.color = "#F00"
        self.multiple = False
        self.code = "$input$ = $output$;\n"
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"

