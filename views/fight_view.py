import random
import threading
import time
from tkinter import Button, Canvas, Entry, Label, messagebox
from tkinter.ttk import LabelFrame
from config.config import Config
from PIL import Image, ImageTk
from data.pymon_local_repository import PymonLocalRepository
from data.users_csv_repository import UsersCSVRepository
from domain.user import User
from views.blank_view import BlankView


class FightView(BlankView):
    def __init__(self, pymon_enemy, pymon_level, is_history=True) -> None:
        super().__init__(size="300x400")
        self.timer = None
        self.is_history = is_history
        self.pymonRepository = PymonLocalRepository()
        self.usersRepository = UsersCSVRepository()
        self.pymon_enemy = pymon_enemy
        self.my_pymon_index = User.currentUser.pokepy_id - 1
        self.enemy_pymon_index = pymon_level - 1
        self.my_pymon = self.pymonRepository.get_pymons()[self.my_pymon_index]

        

        
        frame = LabelFrame(self.window, text="")
        frame.grid(row=0, column=0, columnspan=12, pady=20)

        my_pymon_image = self.get_image_by_index(frame, self.my_pymon_index)
        canvas_my_pokepy = Canvas(frame, width = 100, height = 100)
        canvas_my_pokepy.grid(row=1, column=0, columnspan=6, pady=0)
        canvas_my_pokepy.create_image(50,50, anchor='center', image=my_pymon_image) 
        canvas_my_pokepy.photo = my_pymon_image

        Label(frame, text=self.my_pymon.name).grid(row=2, column=0, columnspan=6, pady=0)
        self.my_pymon_label = Label(frame, text=str(self.my_pymon.health_points)+" HP")
        self.my_pymon_label.grid(row=3, column=0, columnspan=6, pady=0)

        enemy_pymon_image = self.get_image_by_index(frame, self.enemy_pymon_index)
        canvas_enemy_pokepy = Canvas(frame, width = 100, height = 100)
        canvas_enemy_pokepy.grid(row=1, column=6, columnspan=6, pady=0)
        canvas_enemy_pokepy.create_image(50,50, anchor='center', image=enemy_pymon_image) 
        canvas_enemy_pokepy.photo = enemy_pymon_image

        Label(frame, text=self.pymon_enemy.name).grid(row=2, column=6, columnspan=6, pady=0)
        self.enemy_pymon_label = Label(frame, text=str(self.pymon_enemy.health_points)+" HP")
        self.enemy_pymon_label.grid(row=3, column=6, columnspan=6, pady=0)
      

        

        habilities = self.my_pymon.habilities
        Button(frame, text=habilities[0].name, command=self.__use_hability_0).grid(row=4, column=0, columnspan=12, pady=0)
        Button(frame, text=habilities[1].name, command=self.__use_hability_1).grid(row=5, column=0, columnspan=12, pady=0)
        Button(frame, text=habilities[2].name, command=self.__use_hability_2).grid(row=6, column=0, columnspan=12, pady=0)
        Button(frame, text=habilities[3].name, command=self.__use_hability_3).grid(row=7, column=0, columnspan=12, pady=0)

        self.turnLabel = Label(frame, text="Es tu turno")
        self.turnLabel.grid(row=8, column=0, columnspan=12, pady=0)
        self.habilitiesUsedLabel = Label(frame, text="")
        self.habilitiesUsedLabel.grid(row=9, column=0, columnspan=12, pady=0)

    def __use_hability_0(self):
        hability = self.my_pymon.habilities[0]
        self.__use_hability_to_oponent(hability, self.my_pymon, self.pymon_enemy)
        self.__perform_cpu_enemy()

    def __use_hability_1(self):
        hability = self.my_pymon.habilities[1]
        self.__use_hability_to_oponent(hability, self.my_pymon, self.pymon_enemy)
        self.__perform_cpu_enemy()
        
    def __use_hability_2(self):
        hability = self.my_pymon.habilities[2]
        self.__use_hability_to_oponent(hability, self.my_pymon, self.pymon_enemy)
        self.__perform_cpu_enemy()
        
    def __use_hability_3(self):
        hability = self.my_pymon.habilities[3]
        self.__use_hability_to_oponent(hability, self.my_pymon, self.pymon_enemy)
        self.__perform_cpu_enemy()

    def __use_hability_to_oponent(self, hability, attacker, attacked):
        self.habilitiesUsedLabel.config(text=attacker.name+" usó ataque "+hability.name)
        attacked.receive_power(attacker, hability.use())
        self.my_pymon_label.config(text=str(self.my_pymon.health_points)+" HP")
        self.enemy_pymon_label.config(text=str(self.pymon_enemy.health_points)+" HP")

        if attacked.health_points <= 0:
            if attacked == self.pymon_enemy:
                messagebox.askokcancel("Victoria", "Has ganado")
                new_level = User.currentUser.level + 1
                self.usersRepository.upgrade_level(new_level)
                
                if self.is_history:
                    self.pop()
                else:
                    self.pop()
            else:
                messagebox.askokcancel("Fracaso", "Has perdido")


    def __perform_cpu_enemy(self):
        if self.timer != None:
            self.timer.cancel()
        turn = random.randint(1,2)
        if turn == 2:
            self.turnLabel.config(text="Turno de la CPU")
            hability = self.my_pymon.habilities[random.randint(0,3)]
            self.__use_hability_to_oponent(hability, self.pymon_enemy, self.my_pymon)
            
            self.timer = threading.Timer(2.0, self.__perform_cpu_enemy)
            self.timer.start()
        else:
            self.turnLabel.config(text="Es tu turno")

    def get_image_by_index(self, frame, image_index): 
        newsize = (100,100)
        if image_index == 0:
            Img = Image.open(Config.projectPath+"assets/"+"aquarder.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        elif image_index == 1:
            Img = Image.open(Config.projectPath+"assets/"+"electder.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        elif image_index == 2:
            Img = Image.open(Config.projectPath+"assets/"+"Firesor.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        elif image_index == 3:
            Img = Image.open(Config.projectPath+"assets/"+"mousebug.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        elif image_index == 4:
            Img = Image.open(Config.projectPath+"assets/"+"splant.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        elif image_index == 5:
            Img = Image.open(Config.projectPath+"assets/"+"rockdog.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        else:
            Img = Image.open(Config.projectPath+"assets/"+"Firesor.png")
            Img_resized = Img.resize(newsize)
            return ImageTk.PhotoImage(Img_resized, master = frame)
        