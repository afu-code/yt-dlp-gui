import tkinter as tk
from .app import YTDownloaderGUI

def run_app():
    root = tk.Tk()
    app = YTDownloaderGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
