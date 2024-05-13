import tkinter as tk
from color import Color



class Display(tk.Label):
   def __init__(self, master:tk.Tk = None, **kwargs) -> None:
      super().__init__(master, **kwargs)

      self.config(
         width=15,
         height=3,
         font=('Helvetica', 25, 'bold'),
         bg=Color.WHITE,
         fg=Color.ORANGE
      )

   def change_text(self, new_text):
      self.config(text=new_text)


class Button(tk.Button):
   def __init__(self, master:tk.Tk = None, **kwargs) -> None:
      super().__init__(master, **kwargs)

      self.values = None

      self.config(
         width=15,
         height=3,
         font=('Helvetica', 20, 'bold'),
         fg='#ffffff'
      )

   def change_text(self, new_text):
      self.config(text=new_text)

   def set_color(self, color:str) -> None:
      self.config(bg=color)

   def set_values(self, values):
      self.values = values
   
   def get_values(self):
      return self.values
