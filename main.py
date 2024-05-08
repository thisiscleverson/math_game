import tkinter as tk
from widgets import *
from color import color_palette


def main() -> None:
   root = tk.Tk()
   display  = Display(root)
   button1  = Button(root, '1', color_palette.get("Golden Dream"))
   button2  = Button(root, '2', color_palette.get("Cadmium Orange"))
   button3  = Button(root, '3', color_palette.get("Button Blue"))


   root.mainloop()


if __name__ == "__main__":
   main()