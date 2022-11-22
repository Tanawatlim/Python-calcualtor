from tkinter import *

metallic_grey = "#58676D"
dark_grey = "#545454"
yellow = "#ffb640"
white = "#FFFFFF"

font_style_1 = ("Arial", 18)
font_style_2 = ("Arial", 36)

HEIGHT = 2
WIDTH = 5


class Calculator:
    def __init__(self):
        self.screen = Tk()
        self.screen.geometry("312x546")
        self.screen.title("Calculator")

        self.tracker = ""
        self.result = ""
        self.result_frame = self.create_result_frame()

        self.total_label, self.label = self.create_display_label()
        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()

    def create_result_frame(self):
        frame = Frame(self.screen)
        frame.pack(fill="both")
        return frame

    def create_buttons_frame(self):
        frame = Frame(self.screen)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_label(self):
        total_label = Label(self.result_frame, text=self.tracker, anchor='e', padx=24, pady=24, bg=dark_grey,
                            fg=white, font=font_style_1)
        total_label.pack(expand=True, fill="both")

        label = Label(self.result_frame, text=self.result, anchor='e', padx=24, pady=24, bg=dark_grey,
                      fg=white, font=font_style_2)
        label.pack(expand=True, fill="both")

        return total_label, label

    def update_label(self):
        self.label.config(text=self.result)

    def update_total_label(self):
        self.total_label.config(text=self.tracker)

    def add_expression(self, value):
        self.result += str(value)
        self.update_label()

    def add_operator(self, operator):
        self.result += operator
        self.tracker += self.result
        self.result = ""
        self.update_total_label()
        self.update_label()

    def equal_button(self):
        self.tracker += self.result
        self.update_total_label()
        self.result = str(eval(self.tracker))

        self.tracker = ""
        self.update_label()

    def clear(self):
        self.result = ""
        self.tracker = ""
        self.update_total_label()
        self.update_label()

    def create_buttons(self):
        # Number button
        button_num0 = Button(self.buttons_frame, text="0", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("0"))
        button_num0.config(height=HEIGHT, width=WIDTH)

        button_num00 = Button(self.buttons_frame, text="00", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.add_expression("00"))
        button_num00.config(height=HEIGHT, width=WIDTH)

        button_num1 = Button(self.buttons_frame, text="1", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("1"))
        button_num1.config(height=HEIGHT, width=WIDTH)

        button_num2 = Button(self.buttons_frame, text="2", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("2"))
        button_num2.config(height=HEIGHT, width=WIDTH)

        button_num3 = Button(self.buttons_frame, text="3", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("3"))
        button_num3.config(height=HEIGHT, width=WIDTH)

        button_num4 = Button(self.buttons_frame, text="4", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("4"))
        button_num4.config(height=HEIGHT, width=WIDTH)

        button_num5 = Button(self.buttons_frame, text="5", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("5"))
        button_num5.config(height=HEIGHT, width=WIDTH)

        button_num6 = Button(self.buttons_frame, text="6", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("6"))
        button_num6.config(height=HEIGHT, width=WIDTH)

        button_num7 = Button(self.buttons_frame, text="7", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("7"))
        button_num7.config(height=HEIGHT, width=WIDTH)

        button_num8 = Button(self.buttons_frame, text="8", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("8"))
        button_num8.config(height=HEIGHT, width=WIDTH)

        button_num9 = Button(self.buttons_frame, text="9", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_expression("9"))
        button_num9.config(height=HEIGHT, width=WIDTH)

        # operator buttons
        button_plus = Button(self.buttons_frame, text="+", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                             font=font_style_1, command=lambda: self.add_operator("+"))
        button_plus.config(height=HEIGHT, width=WIDTH)
        button_minus = Button(self.buttons_frame, text="-", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.add_operator("-"))
        button_minus.config(height=HEIGHT, width=WIDTH)
        button_multi = Button(self.buttons_frame, text="x", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.add_operator("*"))
        button_multi.config(height=HEIGHT, width=WIDTH)
        button_div = Button(self.buttons_frame, text="÷", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                            font=font_style_1, command=lambda: self.add_operator("/"))
        button_div.config(height=HEIGHT, width=WIDTH)

        button_percent = Button(self.buttons_frame, text="%", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                                font=font_style_1, command=lambda: self.add_operator("%"))
        button_percent.config(height=HEIGHT, width=WIDTH)
        button_power = Button(self.buttons_frame, text="^", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.add_operator("**"))
        button_power.config(height=HEIGHT, width=WIDTH)

        # clear button
        button_clear = Button(self.buttons_frame, text="C", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.clear())
        button_clear.config(height=HEIGHT, width=WIDTH)

        # option buttons
        button_dot = Button(self.buttons_frame, text=".", bg=metallic_grey, fg=white, bd=1, relief=SUNKEN,
                            font=font_style_1, command=lambda : self.add_operator("."))
        button_dot.config(height=HEIGHT, width=WIDTH)
        button_equal = Button(self.buttons_frame, text="=", bg=yellow, fg=white, bd=1, relief=SUNKEN,
                              font=font_style_1, command=lambda: self.equal_button())
        button_equal.config(height=HEIGHT, width=WIDTH)

        # display row 0
        button_clear.grid(row=0, column=0)
        button_percent.grid(row=0, column=1)
        button_power.grid(row=0, column=2)
        button_div.grid(row=0, column=3)

        # display row1
        button_num7.grid(row=1, column=0)
        button_num8.grid(row=1, column=1)
        button_num9.grid(row=1, column=2)
        button_multi.grid(row=1, column=3)

        # display row2
        button_num4.grid(row=2, column=0)
        button_num5.grid(row=2, column=1)
        button_num6.grid(row=2, column=2)
        button_minus.grid(row=2, column=3)

        # display row 3
        button_num1.grid(row=3, column=0)
        button_num2.grid(row=3, column=1)
        button_num3.grid(row=3, column=2)
        button_plus.grid(row=3, column=3)

        # display row 4
        button_num0.grid(row=4, column=0)
        button_num00.grid(row=4, column=1)
        button_dot.grid(row=4, column=2)
        button_equal.grid(row=4, column=3)

    def run(self):
        self.screen.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
