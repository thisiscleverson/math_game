import tkinter as tk
from random import randint
from color import Color
from widgets import *
from math_question import MathQuestion


class FinalScore:
   def __init__(self) -> None:
      self.score = 0
   
   def set_score(self, new_score) -> None:
      if self.score < new_score:
         self.score = new_score
   
   def get_score(self) -> int:
      return self.score

final_score = FinalScore()



class HomePage(tk.Frame):
   def __init__(self, master:tk.Tk) -> None:
      super().__init__(master)

      self.config(bg=Color.CYAN)

      title = tk.Label(self, text="MATEMÁTICA CORRETA")
      title.config(
         font=('Poetsen One', 15, 'bold'),
         bg=Color.CYAN,
         fg=Color.LIGHT_YELLOW
      )
      title.pack(ipady=30)

      button = tk.Button(self, text="Iniciar", command=self.show_Game_Page)
      button.config(
         width=15,
         height=3,
         font=('Helvetica', 20, 'bold'),
         bg=Color.ORANGE,
         fg=Color.WHITE,
      )
      button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
   
   def show_Game_Page(self) -> None:
      self.master.home_page.pack_forget()  # Esconde a HomePage
      self.master.game_page.pack(expand=True, fill=tk.BOTH)  # Mostra a GamePage
      self.master.game_page.start_game()
      self.master.game_page.start_timer()



class GamePage(tk.Frame):
   def __init__(self, master: tk.Tk) -> None:
      super().__init__(master)

      self.math_question = MathQuestion()

      self.__score = 0
      self.__remaining = 5

      self.score_label = tk.Label(self, text=f'Pontuação: {self.__score}')
      self.score_label.config(
         font=('Helvetica', 20, 'bold'),
         fg=Color.ORANGE
      )
      self.score_label.pack(padx=40, pady=10)

      self.timer_label = tk.Label(self, text="")
      self.timer_label.config(
         font=('Helvetica', 20, 'bold'),
         fg=Color.ORANGE
      )
      self.timer_label.pack(pady=5)

      self.display = Display(self)
      self.display.pack()

      self.buttons = []  # Lista para armazenar os botões
      button_colors = [Color.BLUE, Color.ORANGE, Color.GREEN]  # Cores dos botões

      # Criando os três botões
      for i in range(3):
         button = Button(self, command=lambda idx=i: self.button_active(idx))
         button.set_color(button_colors[i])
         button.pack(padx=10, pady=10)
         self.buttons.append(button)

      #self.start_game()

   def draw_button_with_correct_answer(self) -> None:
      index = randint(0, 2)  # Índice aleatório para o botão correto

      correct_answer = self.math_question.get_right_answer()
      incorrect_answers = []

      for i in range(3):
         if i == index:
            self.buttons[i].change_text(correct_answer)
            self.buttons[i].set_values(correct_answer)
         else:
            if randint(0, 1) == 0:
               incorrect_answers.append(correct_answer + randint(1, 10))
            else:
               incorrect_answers.append(correct_answer * randint(2, 6))

      for i in range(3):
         if i != index:
            incorrect_answer = incorrect_answers.pop()
            self.buttons[i].change_text(incorrect_answer)
            self.buttons[i].set_values(incorrect_answer)

   def start_game(self) -> None:
      self.math_question.generate_question()
      self.display.change_text(self.math_question.get_question())
      self.draw_button_with_correct_answer()
      print(self.math_question.get_right_answer())

   def button_active(self, idx:int) -> None:
      values = self.buttons[idx].get_values()
      print(values)
      is_correct = self.math_question.check_answer_is_correct(values)

      if is_correct:
         self.__score += 1
         self.reset_timer()
         self.__chace_score_label()
         self.start_game()
      else:
         final_score.set_score(self.__score)
         self.show_gamer_over_page()
   
   def __chace_score_label(self) -> None:
      self.score_label.config(text=f'Pontuação: {self.__score}')
   
   def start_timer(self) -> None:
      if self.__remaining >= 0:
         self.timer_label.config(text=str(self.__remaining))
         self.after(1000, self.start_timer)
      else:
         final_score.set_score(self.__score)
         self.show_gamer_over_page()

      self.__remaining -= 1

   def reset_timer(self) -> None:
      self.__remaining = 5
   
   def reset_score(self) -> None:
      self.__score = 0

   def show_gamer_over_page(self) -> None:
      self.master.gamer_over_page.chace_score_label()
      self.master.game_page.pack_forget()
      self.master.gamer_over_page.pack(expand=True, fill=tk.BOTH)



class GamerOverPage(tk.Frame):
   def __init__(self, master:tk.Tk) -> None:
      super().__init__(master)

      self.config(bg=Color.CYAN)

      title = tk.Label(self, text="Game Over!")
      title.config(
         font=('Helvetica', 20, 'bold'),
         bg=Color.CYAN,
         fg=Color.ORANGE
      )
      title.pack(ipadx=20, padx=10, pady=10)

      self.score_label = tk.Label(self, text=f'Melhor \nPontuação:')
      self.score_label.config(
         font=('Helvetica', 20, 'bold'),
         bg=Color.CYAN,
         fg=Color.WHITE
      )
      self.score_label.pack(padx=40, pady=10)


      button_try_again = tk.Button(self, text="jogar Novamente", command=self.show_Game_Page)
      button_try_again.config(
         width=15,
         height=3,
         font=('Helvetica', 20, 'bold'),
         bg=Color.LIGHT_YELLOW,
         fg=Color.WHITE,
      )
      button_try_again.pack(padx=10, pady=10)

      button_quit = tk.Button(self, text="Sair", command=lambda:self.master.quit())
      button_quit.config(
         width=15,
         height=3,
         font=('Helvetica', 20, 'bold'),
         bg=Color.RED,
         fg=Color.WHITE,
      )
      button_quit.pack(padx=10, pady=10)
   
   def show_Game_Page(self) -> None:
      self.master.gamer_over_page.pack_forget()  # Esconde a HomePage
      self.master.game_page.pack(expand=True, fill=tk.BOTH)  # Mostra a GamePage

      self.master.game_page.reset_score()
      self.master.game_page.reset_timer()
      self.master.game_page.start_game()
      self.master.game_page.start_timer()
      
   def chace_score_label(self) -> None:
      self.score_label.config(text=f'Melhor \nPontuação: {final_score.get_score()}')