# GUI

def create_number_buttons(self):
        for number, coordinate in self.numbers.items():
            button = tk.Button(self.buttons_frame, text = number, bg= "#358873", fg= "#FFEBD2", font = ("Verdana", 10, "bold"), borderwidth=0, command=lambda x=number: self.append_operator(x)) 
            button.grid(row=coordinate[0], column=coordinate[1], sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.numbers:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))