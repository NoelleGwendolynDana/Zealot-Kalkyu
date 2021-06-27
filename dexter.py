#GUI 
# bottom part

def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text = "C", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text = "DEL", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.delete)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_equal_button(self):
        button = tk.Button(self.buttons_frame, text = "=", bg = "#207567", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_ans_button(self):
        button = tk.Button(self.buttons_frame, text = "ANS", bg = "#4E9C81", fg = "#FFEBD2", font = ("Verdana", 15, "bold"), borderwidth=0, command=self.ans)
        button.grid(row=0, column=3, sticky=tk.NSEW)