from tkinter import Button, Entry, Label, PhotoImage, messagebox
from tkinter.ttk import LabelFrame
from PIL import Image, ImageTk
from config.config import Config
from data.users_csv_repository import UsersCSVRepository
from views.blank_view import BlankView


class PokepyViewDetail(BlankView):
    def __init__(self, pokepy, is_training=False) -> None:
        super().__init__(size="550x540")
        self.is_training = is_training

        self.usersRepository = UsersCSVRepository()

        frame = LabelFrame(self.window, text="")
        frame.grid(row=0, column=0, columnspan=7, pady=20)
        
        Label(frame, text=pokepy.name+": Tipo "+pokepy.fighter_type.to_string()).grid(row=1, column=0, columnspan=7, pady=20)
        adventages = ""
        for adventage in pokepy.fighter_type.get_advantages():
            adventages += adventage.to_string() + " "
        weakness = ""
        for weakWith in pokepy.fighter_type.get_weakness():
            weakness += weakWith.to_string() + " "
        normalWith = ""
        for normal in pokepy.fighter_type.get_normal():
            normalWith += normal.to_string() + " "
        Label(frame, text="Ventaja con: "+adventages).grid(row=2, column=0, columnspan=7, pady=4)
        Label(frame, text="Desventaja con: "+weakness).grid(row=3, column=0, columnspan=7, pady=4)
        Label(frame, text="Normal con: "+normalWith).grid(row=4, column=0, columnspan=7, pady=4)
        hability1 = pokepy.habilities[0]
        hability2 = pokepy.habilities[1]
        hability3 = pokepy.habilities[2]
        hability4 = pokepy.habilities[3]
        Label(frame, text="Habilidad |norm|At vent|At vent|post norm|post vent|post desv|").grid(row=5, column=0, columnspan=7, pady=4)
        Label(frame, text=hability1.name+"   |  "+str(hability1.normal_damange)+" pt  |    "+str(hability1.advantage_damange)+" pt    |    "+str(hability1.disventage_damange)+" pt    |    "+str(hability1.normal_boost_damange)+" pt    |     "+str(hability1.advantage_boost_damange)+" pt    |    "+str(hability1.disventage_boost_damange)+" pt    |").grid(row=6, column=0, columnspan=7, pady=2)
        Label(frame, text=hability2.name+"   |  "+str(hability2.normal_damange)+" pt  |    "+str(hability2.advantage_damange)+" pt    |    "+str(hability2.disventage_damange)+" pt    |    "+str(hability2.normal_boost_damange)+" pt    |     "+str(hability2.advantage_boost_damange)+" pt    |    "+str(hability2.disventage_boost_damange)+" pt    |").grid(row=7, column=0, columnspan=7, pady=2)
        Label(frame, text=hability3.name+"   |  "+str(hability3.normal_damange)+" pt  |    "+str(hability4.advantage_damange)+" pt    |    "+str(hability4.disventage_damange)+" pt    |    "+str(hability3.normal_boost_damange)+" pt    |     "+str(hability3.advantage_boost_damange)+" pt    |    "+str(hability3.disventage_boost_damange)+" pt    |").grid(row=8, column=0, columnspan=7, pady=2)
        Label(frame, text=hability4.name+"   | Potenciador de campo, 1 vez cada 3 turnos. Tiene una duración de 2 turnos.  |").grid(row=9, column=0, columnspan=7, pady=2)



        
