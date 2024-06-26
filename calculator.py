import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self.root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        buttons_frame = tk.Frame(self.root, width=400, height=500, bg="grey")
        buttons_frame.pack()

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=1, pady=1)

        clear_button = tk.Button(buttons_frame, text='C', fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear)
        clear_button.grid(row=0, column=0, padx=1, pady=1, columnspan=3)

    def on_button_click(self, char):
        if char == '=':
            self.calculate()
        else:
            self.expression += str(char)
            self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
