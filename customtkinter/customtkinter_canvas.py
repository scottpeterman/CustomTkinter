import tkinter


class CTkCanvas(tkinter.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.aa_circle_canvas_ids = []

    def get_char_from_radius(self, radius):
        if radius >= 10:
            char = "B"
        elif radius >= 6:
            char = "D"
        elif radius >= 3:
            char = "H"
        else:
            char = "H"

        return char

    def create_aa_circle(self, x_pos, y_pos, radius, angle=0, fill="white", tags="", anchor=tkinter.CENTER) -> str:
        # create a circle with a font element
        circle_1 = self.create_text(x_pos, y_pos, text=self.get_char_from_radius(radius), anchor=anchor, fill=fill,
                                    font=("CustomTkinter_shapes_font", -radius * 2), tags=tags, angle=angle)
        self.addtag_withtag("ctk_aa_circle_font_element", circle_1)
        self.aa_circle_canvas_ids.append(circle_1)

        return circle_1

    def coords(self, tag_or_id, *args):

        if type(tag_or_id) == str and "ctk_aa_circle_font_element" in self.gettags(tag_or_id):
            coords_id = self.find_withtag(tag_or_id)[0]  # take the lowest id for the given tag
            super().coords(coords_id, *args[:2])

            if len(args) == 3:
                super().itemconfigure(coords_id, font=("CustomTkinter_shapes_font", -int(args[2]) * 2), text=self.get_char_from_radius(args[2]))

        elif type(tag_or_id) == int and tag_or_id in self.aa_circle_canvas_ids:
            super().coords(tag_or_id, *args[:2])

            if len(args) == 3:
                super().itemconfigure(tag_or_id, font=("CustomTkinter_shapes_font", -args[2] * 2), text=self.get_char_from_radius(args[2]))

        else:
            super().coords(tag_or_id, *args)

    def itemconfig(self, tag_or_id, *args, **kwargs):
        kwargs_except_outline = kwargs.copy()
        if "outline" in kwargs_except_outline:
            del kwargs_except_outline["outline"]

        if type(tag_or_id) == int:
            if tag_or_id in self.aa_circle_canvas_ids:
                super().itemconfigure(tag_or_id, *args, **kwargs_except_outline)
            else:
                super().itemconfigure(tag_or_id, *args, **kwargs)
        else:
            configure_ids = self.find_withtag(tag_or_id)
            for configure_id in configure_ids:
                if configure_id in self.aa_circle_canvas_ids:
                    super().itemconfigure(configure_id, *args, **kwargs_except_outline)
                else:
                    super().itemconfigure(configure_id, *args, **kwargs)


