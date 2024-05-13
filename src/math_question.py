from typing import Tuple
from random import randint, choices


class MathQuestion:
   def __init__(self) -> None:
      self.__math_operations = ("SUM", "SUBTRACTION", "MULTIPLICATION", "DIVISION")
      self.right_answer = None
      self.question = None

      self.sum_question            = SumQuestion()
      self.subtraction_question    = SubtractionQuestion()
      self.multiplication_question = MultiplicationQuestion()
      self.division_question       = DivisionQuestion() 

   def __choose_math_operation(self) -> str:
      return choices(self.__math_operations)[0]

   def get_right_answer(self) -> int:
      return self.right_answer

   def get_question(self) -> str:
      return self.question
   
   def check_answer_is_correct(self, answer) -> bool:
      return self.right_answer == answer

   def generate_question(self) -> str:
      math_operation = self.__choose_math_operation()

      if math_operation == "SUM":
         question, right_answer = self.sum_question.generate_question()
         self.right_answer = right_answer
         self.question = question

      elif math_operation == "SUBTRACTION":
         question, right_answer = self.subtraction_question.generate_question()
         self.right_answer = right_answer
         self.question = question

      elif math_operation == "MULTIPLICATION":
         question, right_answer = self.multiplication_question.generate_question()
         self.right_answer = right_answer
         self.question = question

      elif math_operation == "DIVISION":
         question, right_answer = self.division_question.generate_question()
         self.right_answer = right_answer
         self.question = question

class SumQuestion:
   def generate_question(self) -> Tuple[str, int]:
      number1  = randint(1,10)
      number2  = randint(1,10)

      question = f'{number1} + {number2} = ?'
      right_answer = number1 + number2

      return (question, right_answer)


class SubtractionQuestion:
   def generate_question(self) -> Tuple[str, int]:
      while True:
         number1 = randint(10, 100)
         number2 = randint(1, 10)

         if (number1 - number2) > 0:
            break
      
      question = f'{number1} - {number2} = ?'
      right_answer = number1 - number2

      return (question, right_answer)


class MultiplicationQuestion:
   def generate_question(self) -> Tuple[str, int]:
      number1 = randint(1,10)
      number2 = randint(1,10)

      question = f'{number1} x {number2} = ?'
      right_answer = number1 * number2

      return (question, right_answer)


class DivisionQuestion:
   def generate_question(self) -> Tuple[str,int]:
      while True:
         number1 = randint(2,10)
         number2 = randint(2,10)

         if number1 % number2 == 0:
            break
      
      question = f'{number1} ÷ {number2} = ?'
      right_answer = number1 // number2

      return (question, right_answer)
