import tkinter as tk
from pages import HomePage, GamePage, GamerOverPage

class MyApp(tk.Tk):
   def __init__(self):
      super().__init__()

      self.title("Jogo de Matemática")
      self.geometry('300x550')
      self.resizable(False, False)

      self.home_page = HomePage(self)
      self.game_page = GamePage(self)
      self.gamer_over_page = GamerOverPage(self)

      self.home_page.pack(expand=True, fill=tk.BOTH)


if __name__ == "__main__":
   app = MyApp()
   app.mainloop()