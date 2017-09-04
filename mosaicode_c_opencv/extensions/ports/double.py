from mosaicode.model.port import Port

class Double(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "DOUBLE"
        self.color = "#000"
        self.multiple = False
        self.code = "$input$ = $output$;\n"

