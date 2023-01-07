import time
import pyperclip

class ClipboardRegister:

    def __init__(self, filepath):
        self.clipboard = pyperclip.paste()
        self.filepath = filepath

    def get_clipboard(self):
        return self.clipboard

    def poll(self):
        with open(self.filepath, "w") as f:
            while True:
                time.sleep(1)
                curr = pyperclip.paste()
                if self.clipboard != curr:
                    self.clipboard = curr
                    f.write("\n" + self.clipboard)
                    f.flush()  # Write to file immediately

    def clear(self, seconds):
        time.sleep(seconds)
        with open(self.filepath) as f:
            f.truncate(0)

if __name__ == "__main__":
    filepath = __file__.replace(".py",".txt")
    print(f"Starting clipboard register, writing to {filepath}")
    c = ClipboardRegister(filepath)
    print("Polling clipboard")
    c.poll()

    # c.clear(86400) # Clear after 24 hours, figure out how to make it multi-threaded
