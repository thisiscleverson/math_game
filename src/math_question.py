from typing import Tuple
from random import randint, choices
from abc import ABC, abstractmethod


class Question(ABC):
   def generate_question(self) -> Tuple[str, int]:
      pass


class MathQuestion:
   def __init__(self) -> None:
      self.__math_operations = ("SUM", "SUBTRACTION", "MULTIPLICATION", "DIVISION")
      self.right_answer = None
      self.question     = None

      sum_question            = SumQuestion()
      subtraction_question    = SubtractionQuestion()
      multiplication_question = MultiplicationQuestion()
      division_question       = DivisionQuestion() 

      self.__math_question_generators = {
         "SUM": sum_question.generate_question,
         "SUBTRACTION": subtraction_question.generate_question,
         "MULTIPLICATION": multiplication_question.generate_question,
         "DIVISION": division_question.generate_question
      }

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
      self.question, self.right_answer = self.__math_question_generators[math_operation]()


class SumQuestion(Question):
   def generate_question(self) -> Tuple[str, int]:
      number1  = randint(1,10)
      number2  = randint(1,10)

      question = f'{number1} + {number2} = ?'
      right_answer = number1 + number2

      return (question, right_answer)


class SubtractionQuestion(Question):
   def generate_question(self) -> Tuple[str, int]:
      while True:
         number1 = randint(10, 100)
         number2 = randint(1, 10)

         if (number1 - number2) > 0:
            break
      
      question = f'{number1} - {number2} = ?'
      right_answer = number1 - number2

      return (question, right_answer)


class MultiplicationQuestion(Question):
   def generate_question(self) -> Tuple[str, int]:
      number1 = randint(1,10)
      number2 = randint(1,10)

      question = f'{number1} x {number2} = ?'
      right_answer = number1 * number2

      return (question, right_answer)


class DivisionQuestion(Question):
   def generate_question(self) -> Tuple[str,int]:
      while True:
         number1 = randint(2,10)
         number2 = randint(2,10)

         if number1 % number2 == 0:
            break
      
      question = f'{number1} ÷ {number2} = ?'
      right_answer = number1 // number2

      return (question, right_answer)