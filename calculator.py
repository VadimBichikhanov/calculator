import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = tk.Entry(master, width=20, font=('Arial', 16), justify='right')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.on_button_click(x)
            tk.Button(master, text=button, width=5, height=2, font=('Arial', 14), command=command).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, key):
        if key == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif key == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()