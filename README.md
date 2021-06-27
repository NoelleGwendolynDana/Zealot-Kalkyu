# Zealot-Kalkyu
Basic calculator 

import tkinter as tk

def add_to_expression(self, value):
        self.equation += str(value)
        self.update_equation_label()
        
def append_operator(self, operator):
        self.equation += str(operator)
        self.update_equation_label()
        
def create_special_buttons(self):
        self.create_clear_button()
        self.create_delete_button()
        self.create_equal_button()
        self.create_ans_button()
