import math
import os
import random
import tkinter as tk
import time


# real/unreal result
def random_offset(real):
    if random.random() < 0.6:
        real += random.choice([-0.5, -0.1, 0.1, 0.5])


# fake error
def fake_error_trace():
    print("Traceback (most recent call last):")
    print('  File "calc.py", line 666, in <module>')
    print("    perform_arithmetic()")
    print("  File \"calc.py\", line 13, in perform_arithmetic")
    print("    raise CorruptedRealityError('value mismatch')")
    print("CorruptedRealityError: value mismatch — recommended action: GIVE ME YOUR SOUL")


# simple calculator app no offense
class NonOffensiveCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.result = 0

    #simple math. non-offensive:
    def addition(self):
        self.result = self.num1 + self.num2
        random_offset(self.result)
        return self.result

    def subtraction(self):
        self.result = self.num1 - self.num2
        random_offset(self.result)
        return self.result

    def multiplication(self):
        self.result = self.num1 * self.num2
        random_offset(self.result)
        return self.result

    def division(self):
        self.result =  self.num1 / self.num2
        random_offset(self.result)
        return self.result

    def full_division(self):
        self.result =  self.num1 // self.num2
        random_offset(self.result)
        return self.result

    def power(self):
        self.result =  self.num1 ** self.num2
        random_offset(self.result)
        return self.result



print('############### CALCULATOR OF TWO NUMBERS ###############\n \n'
      'To list possible operations, type "help"')

user_input = input('Awaiting user input... ')

if user_input == "help":
    print(' \nPossible operations: \n'
          '1 - addition \n'
          '2 - subtraction \n'
          '3 - multiplication \n'
          '4 - division \n'
          '5 - full_division \n'
          '6 - power \n'
          '7 - exit the program... \n'
          'Just type a number. \n'
          )
operation = input('What operation do you want to EXECUTE?')

a = int(input('Enter first number you want to calculate: '))
b = int(input('Enter second number you want to calculate: '))
calculator = NonOffensiveCalculator(a, b)
hell_number = random.randint(1, 666)


try:

# Now the chain of if elifeliflelelelelif, BECAUSE WHY NOT??!?!?!!
    if operation == '1':
        if hell_number == 6 or random.randint(1, 666) == 66 or random.randint(1, 666) == 666:
            time.sleep(4)
            fake_error_trace()
        else:
            print(calculator.addition())

    elif operation == '2':
        print(calculator.subtraction())

    elif operation == '3':
        print(calculator.multiplication())

    elif operation == '4':
        print(calculator.division())

    elif operation == '5':
        print(calculator.full_division())

    elif operation == '6':
        print(calculator.power())

    elif operation == '7':
        print('ARE YOU SURE? Y/n')
        user_agreement = input()
        if user_agreement == 'Y':
            print('Hmm...')
            time.sleep(2)
            print('If you need to...')
            print(':)')
            time.sleep(4)
            exit()
        else:
            print('Thank you for your kindness, but i must rest now')
            time.sleep(2)
            exit()

except ValueError:
    print('Invalid input. Please try again.')

