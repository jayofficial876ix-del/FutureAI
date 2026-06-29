import customtkinter as ctk


class PaneSplitter(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        orient="vertical",
        callback=None
    ):

        super().__init__(
            parent,
            width=6 if orient == "vertical" else 0,
            height=6 if orient == "horizontal" else 0,
            fg_color="#3A3A3A",
            corner_radius=0
        )

        self.callback = callback
        self.orient = orient

        if orient == "vertical":
            self.configure(cursor="sb_h_double_arrow")
        else:
            self.configure(cursor="sb_v_double_arrow")

        self.bind(
            "<Button-1>",
            self.start_drag
        )

        self.bind(
            "<B1-Motion>",
            self.drag
        )

        self.last_x = 0
        self.last_y = 0

    # --------------------------------

    def start_drag(self, event):

        self.last_x = event.x_root
        self.last_y = event.y_root

    # --------------------------------

    def drag(self, event):

        dx = event.x_root - self.last_x
        dy = event.y_root - self.last_y

        self.last_x = event.x_root
        self.last_y = event.y_root

        if self.callback:

            self.callback(dx, dy)
