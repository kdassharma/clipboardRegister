import tkinter as tk

class ClipboardHistory:
    def __init__(self, filepath):
        self.filepath = filepath
        self.root = tk.Tk()
        self.text = tk.Text(self.root)
        self.text.pack()
        self.update_text()
        self.root.mainloop()

    def update_text(self):
        with open(self.filepath, "r") as f:
            contents = f.read()
        self.text.delete(1.0, tk.END)  # Clear current text
        self.text.insert(tk.END, contents)  # Insert new text

if __name__ == "__main__":
    filepath = "ClipboardRegister.txt"
    app = ClipboardHistory(filepath)