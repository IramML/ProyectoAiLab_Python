from views.welcome_view import WelcomeView
import tkinter as tk


def start():
    root = tk.Tk()
    root.withdraw()
    welcome = WelcomeView()
    welcome.show_window()
   
if __name__ == "__main__":
    start()