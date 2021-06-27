# GUI

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

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg="#FFFFFF")
        frame.pack(expand=True, fill="both")
        return frame

    def create_operator_buttons(self):
        index = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=index, column=4, sticky=tk.NSEW)
            index += 1


