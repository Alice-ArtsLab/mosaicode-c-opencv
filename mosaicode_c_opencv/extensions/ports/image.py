from mosaicode.model.port import Port

class Image(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "IMG"
        self.color = "#F0F"
        self.multiple = False
        self.var_name = "block$id$_$conn_type$$port_number$"
        self.code = "$input$ = cvCloneImage($output$);\n"
