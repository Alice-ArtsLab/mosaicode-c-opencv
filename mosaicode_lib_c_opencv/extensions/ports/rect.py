from mosaicode.model.port import Port

class Rect(Port):

    def __init__(self):
        Port.__init__(self)
        self.language = "c"
        self.label = "RCT"
        self.color = "#00F"
        self.multiple = False
        self.code = "block$sink$_rect_i$sink_port$ = block$source$_rect_o$source_port$;// RECT connection\n"
