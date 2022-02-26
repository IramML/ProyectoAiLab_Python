from tkinter import Label
from tkinter.ttk import LabelFrame
from views.blank_view import BlankView


class GameFinishedView(BlankView):
    def __init__(self) -> None:
        super().__init__(size="250x250")

        frame = Label(self.window, text="Felicidades! Has terminado el modo historia")
        frame.pack()
