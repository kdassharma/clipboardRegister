import time
import pyperclip

class ClipboardRegister:

    def __init__(self):
        self.clipboard = pyperclip.paste()

    def get_clipboard(self):
        return self.clipboard
        
    def poll(self):
        while True:
            time.sleep(1)
            curr = pyperclip.paste()
            if self.clipboard != curr:
                self.clipboard = curr
                print(self.clipboard)

if __name__ == "__main__":
    print("Starting clipboard register")
    c = ClipboardRegister()
    print("Polling clipboard")
    c.poll()