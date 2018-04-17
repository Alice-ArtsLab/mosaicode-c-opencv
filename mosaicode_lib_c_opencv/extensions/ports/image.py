from mosaicode.model.port import Port

class Image(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.hint = "IMG"
        self.color = "#F0F"
        self.multiple = False
        self.var_name = "$block[label]$_$block[id]$_$port[name]$"
        self.code = "if (!$output$.empty()) $input$ = $output$.clone();\n"
