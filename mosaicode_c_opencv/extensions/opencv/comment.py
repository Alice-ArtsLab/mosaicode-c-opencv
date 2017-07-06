#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Comment class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.blockmodel import BlockModel


class Comment(BlockModel):
    """
    This class contains methods related the Comment class.
    """

    # -------------------------------------------------------------------------
    def __init__(self):
        BlockModel.__init__(self)
        self.comment = ""

        # Appearance
        self.help = "Insert a comment"
        self.label = "Comment"
        self.color = "50:100:200:150"
        self.group = "General"

        self.properties = [{"name": "Comment",
                            "label": "comment",
                            "type": MOSAICODE_COMMENT
                            }
                           ]

        # ----------------C/OpenCv code--------------------------------
        self.codes[1] = '/* $comment$ */ \n'


        self.language = "c"
        self.framework = "opencv"
# -----------------------------------------------------------------------------
