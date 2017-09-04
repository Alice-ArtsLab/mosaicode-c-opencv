from mosaicode.model.port import Port

class Point(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "POINT"
        self.color = "#0FF"
        self.multiple = False
        self.code = "$input$ = $output$;\n"

