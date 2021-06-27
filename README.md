# Zealot-Kalkyu
# Basic calculator 


import tkinter as tk

class Kalkyu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x500")
        self.window.resizable(True, True)
        self.window.title("K")
        self.equation = ""
        self.answer = ""
        self.display_frame = self.create_display_frame()
        self.label = self.create_display_labels()
