from mosaicode.model.port import Port

class Rect(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "RCT"
        self.color = "#00F"
        self.multiple = False
<<<<<<< HEAD:mosaicode_c_opencv/extensions/ports/rect.py
        self.var_name = "b_$id$_$conn_type$_$port_number$"
        self.code = "$input$ = $output$;\n"
=======
        self.code = "block$sink$_rect_i$sink_port$ = block$source$_rect_o$source_port$;// RECT connection\n"
>>>>>>> 87a6ee2e71fd3c9109e8972fc940e17d33a91064:mosaicode_lib_c_opencv/extensions/ports/rect.py
