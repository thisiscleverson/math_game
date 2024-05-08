import tkinter as tk
from random import choices

from color import color_palette

class Display:
   def __init__(self, root: tk.Tk) -> None:
      self.display = tk.Text(root, width=10, height = 1, state='disabled')
      self.display.pack()
      self.display.config(
         font=('Helvetica', 40, 'bold'),
         highlightthickness=1, highlightcolor=color_palette.get("Button Blue9"),
      )

   def update_display(self, content:str) -> None:
      self.display.insert(tk.END,content)
   
   def clean_display(self) -> None:
      self.display.delete('1.0', tk.END)


class Button:
   def __init__(self, root: tk.Tk, content:str, color:str) -> None:
      self.button = tk.Button(root, text=content)
      self.button.pack(padx=10, pady=10)
      self.button.config(
         width=15,
         height=3,
         font=('Helvetica', 20, 'bold'),
         bg=color,
         fg='#ffffff'
      )

   def update_content_button(self, content:str) -> None:
      self.button.config(text=content)

   def __random_color(self) -> str:
      colors = ["red","blue", "orange"]
      return choices(colors)[0]



