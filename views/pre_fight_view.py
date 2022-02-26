from tkinter import Button, Canvas, Entry, Label, PhotoImage, messagebox
from tkinter.ttk import LabelFrame
from config.config import Config
from PIL import Image, ImageTk
from data.pymon_local_repository import PymonLocalRepository
from domain.user import User

from views.blank_view import BlankView
from views.fight_view import FightView


class PreFightView(BlankView):
    def __init__(self, is_history=True) -> None:
        super().__init__()
        self.pymonRepository = PymonLocalRepository()
        Im1 = Image.open(Config.projectPath+"assets/"+"aquarder.png")
        Im2 = Image.open(Config.projectPath+"assets/"+"electder.png")
        Im3 = Image.open(Config.projectPath+"assets/"+"Firesor.png")
        Im4 = Image.open(Config.projectPath+"assets/"+"mousebug.png")
        Im5 = Image.open(Config.projectPath+"assets/"+"splant.png")
        Im6 = Image.open(Config.projectPath+"assets/"+"rockdog.png")
        newsize = (100,100)
        Im_1 = Im1.resize(newsize)
        Im_2 = Im2.resize(newsize)
        Im_3 = Im3.resize(newsize)
        Im_4 = Im4.resize(newsize)
        Im_5 = Im5.resize(newsize)
        Im_6 = Im6.resize(newsize)

        frame = LabelFrame(self.window, text="Oponente")
        frame.grid(row=0, column=0, columnspan=3, pady=20)
        self.images = [ImageTk.PhotoImage(Im_1, master = frame), ImageTk.PhotoImage(Im_2, master = frame), ImageTk.PhotoImage(Im_3, master = frame), ImageTk.PhotoImage(Im_4, master = frame), ImageTk.PhotoImage(Im_5, master = frame), ImageTk.PhotoImage(Im_6, master = frame)]

        self.current_level = int(User.currentUser.level)
        self.current_enemy_index = self.current_level - 1
        self.pymonEnemy = self.pymonRepository.get_pymons()[self.current_enemy_index]
        
        self.canvas = Canvas(frame, width = 100, height = 100)
        self.canvas.grid(row=1, column=0, columnspan=3, pady=0)
        self.canvas.create_image(50,50, anchor='center', image=self.images[self.current_enemy_index]) 
        self.canvas.photo = self.images[self.current_enemy_index]
        self.enemy_label = Label(frame, text=self.pymonEnemy.name)
        self.enemy_label.grid(row=2, column=0, columnspan=3, pady=0)

        Button(frame, text="Comenzar", command=self.__fight).grid(row=3, column=0, columnspan=3, pady=0)


    def resume(self):
        self.current_level = int(User.currentUser.level)
        self.current_enemy_index = self.current_level - 1
        self.pymonEnemy = self.pymonRepository.get_pymons()[self.current_enemy_index]
        self.canvas.delete("all")
        self.canvas.create_image(50,50, anchor='center', image=self.images[self.current_enemy_index]) 
        self.canvas.photo = self.images[self.current_enemy_index]
        self.enemy_label.config(text=self.pymonEnemy.name)

    def __fight(self):

        self.pop_and_present(FightView(self.pymonEnemy, self.current_level))