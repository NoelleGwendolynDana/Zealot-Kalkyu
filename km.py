#GUI
# like sa first part, i-delete ang comment after

import tkinter as tk

# GUI

class Kalkyu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500")
        self.window.resizable(True, True)
        self.window.title("K")
        self.equation = ""
        
        self.answer = ""



# last part

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Kalkyu()
    calc.run()