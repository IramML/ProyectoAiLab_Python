from tkinter import Button, Label
from domain.user import User

from views.blank_view import BlankView
from views.game_finished import GameFinishedView
from views.history_mode_view import HistoryModeView
from views.training_mode_view import TrainingModeView

class SelectModeView(BlankView):

    def __init__(self, mode='to_choose') -> None:
        super().__init__()
        
        label = Label(self.window, text="Pokepy")
        label.pack(pady=8)

        trainingButton = Button(self.window, text="Modo entrenamiento", command=self.__open_training)
        trainingButton.pack(pady=8)

        historyButton = Button(self.window, text="Modo historia", command=self.__open_history)
        historyButton.pack(pady=8)

        if mode == 'history':
            self.__open_history()

    def __open_training(self):
        self.pop_and_present(TrainingModeView())

    def __open_history(self):
        if User.currentUser.level >= 7:
            self.pop_and_present(GameFinishedView())
        else:    
            self.pop_and_present(HistoryModeView())