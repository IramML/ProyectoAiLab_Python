from tkinter import Button, Label, PhotoImage
from config.config import Config
from domain.user import User

from views.blank_view import BlankView
from views.login_view import LoginView
from views.pre_fight_view import PreFightView
from views.register_view import RegisterView

class WelcomeView(BlankView):

    def __init__(self) -> None:
        super().__init__()
        
        label = Label(self.window, text="Pokepy")
        label.pack(pady=8)

        loginButton = Button(self.window, text="Iniciar Sesión", command=self.__login)
        loginButton.pack(pady=8)

        registerButton = Button(self.window, text="Registrarse", command=self.__register)
        registerButton.pack(pady=8)
        

    def __login(self):
        self.pop_and_present(LoginView())

    def __register(self):
        self.pop_and_present(RegisterView())