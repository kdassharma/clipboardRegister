import tkinter as tk

class ClipboardHistory:
    def __init__(self, filepath):
        self.filepath = filepath
        self.root = tk.Tk()

        # Create a Scrollbar widget
        scrollbar = tk.Scrollbar(self.root)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a Text widget and associate it with the Scrollbar
        self.text = tk.Text(self.root, yscrollcommand=scrollbar.set)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.text.yview)

        self.update_text()  # Start updating the text
        self.root.mainloop()

    def update_text(self):
        with open(self.filepath, "r") as f:
            contents = f.read()
        self.text.delete(1.0, tk.END)  # Clear current text
        self.text.insert(tk.END, contents)  # Insert new text
        
        # Get the current scroll position
        # current_scroll_position = self.text.yview()[0]
        # self.text.see(current_scroll_position)  # Set the scroll position
        self.text.see(tk.END)  # Scroll to the bottom

        self.root.after(1000, self.update_text)  # Schedule next update

if __name__ == "__main__":
    filepath = "ClipboardRegister.txt"
    app = ClipboardHistory(filepath)