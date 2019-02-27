from mosaicode.model.port import Port

class Rects(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "RCTS"
        self.color = "#00F"
        self.multiple = False
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
        self.code = "$input$ = $output$;\n"