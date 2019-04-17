from mosaicode.model.port import Port

class Point(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "POINT"
        self.color = "#3F4235"
        self.multiple = False
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
        self.code = "$input$ = $output$;\n"