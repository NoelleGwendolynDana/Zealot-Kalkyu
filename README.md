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


        self.numbers = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": " - ", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=2)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=2)
            self.buttons_frame.columnconfigure(x, weight=2)
        self.create_number_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def create_display_labels(self):
        self.equation_label = tk.Label(self.display_frame, text=self.equation, anchor = tk.NW, bg = "#B4D6C1", fg = "#000000", padx = 10, font = ("Verdana", 15))
        self.equation_label.pack(expand=True, fill='both')

        self.answer_label = tk.Label(self.display_frame, text=self.answer, anchor = tk.E, bg = "#B4D6C1", fg = "#000000", padx = 10, font = ("Verdana", 25, 'bold'))
        self.answer_label.pack(expand=True, fill='both')
        return self.equation_label, self.answer_label

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


        def clear(self):
                self.equation = ""
                self.answer = ""
                self.update_equation_label()
                self.update_answer_label()

         def delete(self):
                self.list1 = []
                self.list1[:0] = self.equation
                self.equation = "".join(self.list1[:-1])
                self.update_equation_label()

        def evaluate(self):
                try:
                    self.answer = str(eval(self.equation))

                except Exception as e:
                    self.answer = "Syntax Error!"
                finally:
                    self.update_answer_label()

