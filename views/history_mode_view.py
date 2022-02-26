from tkinter import Button, Entry, Label, messagebox
from domain.user import User
from views.blank_view import BlankView
from views.choose_pymon_view import ChoosePymonView
from views.pre_fight_view import PreFightView


class HistoryModeView(BlankView):
    def __init__(self) -> None:
        super().__init__()

        if User.currentUser.pokepy_id == None:
            self.pop_and_present(ChoosePymonView(is_history=True, is_choose_personal=True))
        else:
            self.pop_and_present(PreFightView())


        