from tkinter import Tk, Toplevel

class BlankView:
    def __init__(self, size="200x200") -> None:
        self.first_run = True
        self.window = Toplevel()
        self.window.geometry(size)

    def show_window(self):
        if self.first_run:
            self.window.mainloop()
        else:
            self.window.deiconify()
        
    def show_new_window(self, view):
        view.show_window()

    def pop_and_present(self, view):
        self.first_run = False
        ViewsStack.windows.append(self)
        self.window.withdraw()
        view.show_window()


    def resume():
        print("resume")

    def pop(self):
        view_object = ViewsStack.windows.pop()
        view_object.show_window()
        view_object.resume()
        self.window.destroy()
       
       

class ViewsStack:
    windows = []
    