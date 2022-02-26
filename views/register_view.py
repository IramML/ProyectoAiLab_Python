from tkinter import Button, Entry, Label, messagebox
from data.users_csv_repository import UsersCSVRepository
from views.blank_view import BlankView
from views.select_mode_view import SelectModeView


class RegisterView(BlankView):
    def __init__(self) -> None:
        super().__init__(size="200x220")

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

        labelPasswordRe = Label(self.window, text="Repetir contraseña")
        labelPasswordRe.pack(pady=2)

        self.entryPasswordRe = Entry(self.window, show="*")
        self.entryPasswordRe.pack()

        loginButton = Button(self.window, text="Registrarse", command=self.__register)
        loginButton.pack(pady=8)

    def __register(self):
        username = self.entryUser.get()
        password = self.entryPassword.get()
        passwordRepeat = self.entryPasswordRe.get()

        if password != passwordRepeat:
            messagebox.showerror("Error", "Las contraseñas no son las coinciden")
            return

        response = self.usersRepository.create_user(username, password)
        if response == 'success':
            self.pop_and_present(SelectModeView())
        elif response == 'taken':
            messagebox.showerror("Usuario tomado", "El usuario ya fue tomado")