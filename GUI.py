import tkinter as tk
import sys

class ConsoleOutput(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.text_widget = tk.Text(self, bg='black', fg='white', font=("Helvetica", 12))
        self.text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        sys.stdout = self

    def write(self, message):
        self.text_widget.insert(tk.END, message)

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Jarvis Assistant")

        self.console = ConsoleOutput(self.root)
        self.console.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def start(self):
        self.root.mainloop()
