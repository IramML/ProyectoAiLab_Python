from tkinter import Button, Entry, Label, messagebox
from data.users_csv_repository import UsersCSVRepository
from views.blank_view import BlankView
from views.select_mode_view import SelectModeView


class LoginView(BlankView):
    def __init__(self) -> None:
        super().__init__()

        self.usersRepository = UsersCSVRepository()

        label = Label(self.window, text="Pokepy")
        label.pack(pady=8)

        labelUser = Label(self.window, text="Usuario")
        labelUser.pack(pady=2)

        self.entryUser = Entry(self.window)
        self.entryUser.pack()

        labelPassword = Label(self.window, text="Contraseña")
        labelPassword.pack(pady=2)

        self.entryPassword = Entry(self.window, show="*")
        self.entryPassword.pack()

        loginButton = Button(self.window, text="Iniciar Sesión", command=self.__login)
        loginButton.pack(pady=8)

    def __login(self):
        username = self.entryUser.get()
        password = self.entryPassword.get()

        response = self.usersRepository.login_user(username, password)

        if response == 'success':
            self.pop_and_present(SelectModeView())
        elif response == 'no_user':
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
        