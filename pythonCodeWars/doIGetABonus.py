# https://www.codewars.com/kata/do-i-get-a-bonus/train/python
def bonus_time(salary, bonus):
  if bonus:
    return '$' + str(salary * 10)
  else:
    return '$' + str(salary)