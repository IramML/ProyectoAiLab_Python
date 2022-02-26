from tkinter import Button, Entry, Label, messagebox
from tkinter.ttk import LabelFrame
from config.config import Config
from data.pymon_local_repository import PymonLocalRepository
from data.users_csv_repository import UsersCSVRepository
from views.blank_view import BlankView
from views.choose_pymon_view import ChoosePymonView
from views.pokepy_detail_view import PokepyViewDetail
from views.pre_fight_view import PreFightView
from PIL import Image, ImageTk


class TrainingModeView(BlankView):
    def __init__(self) -> None:
        super().__init__()
        self.pymonSelected = 0
        self.pymonRepository = PymonLocalRepository()
        self.usersRepository = UsersCSVRepository()
        
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

        frame = LabelFrame(self.window, text="Escoge un pokepy")
        frame.grid(row=0, column=0, columnspan=3, pady=20)

        im1 = ImageTk.PhotoImage(Im_1, master = frame)
        im2 = ImageTk.PhotoImage(Im_2, master = frame)
        im3 = ImageTk.PhotoImage(Im_3, master = frame)
        im4 = ImageTk.PhotoImage(Im_4, master = frame)
        im5 = ImageTk.PhotoImage(Im_5, master = frame)
        im6 = ImageTk.PhotoImage(Im_6, master = frame)

        Label(frame, text="Aquarder").grid(row=1, column=0, columnspan=1, pady=20)
        Label(frame, text="Electder").grid(row=1, column=1, columnspan=1, pady=20)
        Label(frame, text="Firesor").grid(row=1, column=2, columnspan=1, pady=20)

        aquarderButton = Button(frame, command=self.__choose_1, image=im1,text="Aquarder", height=100, width=100)
        aquarderButton.grid(row=2, column=0, columnspan=1, pady=0)
        aquarderButton.photo = im1
        electderButton = Button(frame, command=self.__choose_2, image=im2)
        electderButton.grid(row=2, column=1, columnspan=1, pady=0)
        electderButton.photo = im2
        firesorButton = Button(frame, command=self.__choose_3, image=im3)
        firesorButton.grid(row=2, column=2, columnspan=1, pady=0)
        firesorButton.photo = im3

        Button(frame, command=self.__detail_1, text="Detalles").grid(row=3, column=0, columnspan=1, pady=0)
        Button(frame, command=self.__detail_2, text="Detalles").grid(row=3, column=1, columnspan=1, pady=0)
        Button(frame, command=self.__detail_3, text="Detalles").grid(row=3, column=2, columnspan=1, pady=0)
        
        Label(frame, text="Mousebug").grid(row=4, column=0, columnspan=1, pady=20)
        Label(frame, text="Splant").grid(row=4, column=1, columnspan=1, pady=20)
        Label(frame, text="Rockdog").grid(row=4, column=2, columnspan=1, pady=20)

        mousebugButton = Button(frame, command=self.__choose_4, image=im4)
        mousebugButton.grid(row=5, column=0, columnspan=1, pady=0)
        mousebugButton.photo = im4
        splantButton = Button(frame, command=self.__choose_5, image=im5)
        splantButton.grid(row=5, column=1, columnspan=1, pady=0)
        splantButton.photo = im5
        rockdogButton = Button(frame, command=self.__choose_6, image=im6)
        rockdogButton.grid(row=5, column=2, columnspan=1, pady=0)
        rockdogButton.photo = im6

        Button(frame, command=self.__detail_4, text="Detalles").grid(row=6, column=0, columnspan=1, pady=0)
        Button(frame, command=self.__detail_5, text="Detalles").grid(row=6, column=1, columnspan=1, pady=0)
        Button(frame, command=self.__detail_6, text="Detalles").grid(row=6, column=2, columnspan=1, pady=0)

        self.pokepySelectedLabel = Label(frame, text="Seleccionado: Aquarder")
        self.pokepySelectedLabel.grid(row=7, column=0, columnspan=3, pady=20)
        Button(frame, text="Iniciar", command=self.__start).grid(row=8, column=0, columnspan=3, pady=10)

    def __choose_1(self):
        self.pymonSelected = 1
        self.pokepySelectedLabel.config(text = "Seleccionado: Aquarder")
    def __choose_2(self):
        self.pymonSelected = 3
        self.pokepySelectedLabel.config(text = "Seleccionado: Electder")
    def __choose_3(self):
        self.pymonSelected = 2
        self.pokepySelectedLabel.config(text = "Seleccionado: Firesor")
    def __choose_4(self):
        self.pymonSelected = 4
        self.pokepySelectedLabel.config(text = "Seleccionado: Mousebug")
    def __choose_5(self):
        self.pymonSelected = 5
        self.pokepySelectedLabel.config(text = "Seleccionado: Splant")
    def __choose_6(self):
        self.pymonSelected = 6
        self.pokepySelectedLabel.config(text = "Seleccionado: Rockdog")

    def __detail_1(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[0]))
    def __detail_2(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[2]))
    def __detail_3(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[1]))
    def __detail_4(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[3]))
    def __detail_5(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[4]))
    def __detail_6(self):
        self.show_new_window(PokepyViewDetail(pokepy=self.pymonRepository.get_pymons()[5]))

    def __start(self):
        self.usersRepository.choose_history_pymon(self.pymonSelected)
        
        self.pop_and_present(PreFightView(is_history=False))