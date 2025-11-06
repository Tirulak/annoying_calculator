import math
import os
import sys
import time
import random


def fake_error_trace():
    print("Traceback (most recent call last):")
    print('  File "calc.py", line 666, in <module>')
    print("    perform_arithmetic()")
    print("  File \"calc.py\", line 13, in perform_arithmetic")
    print("    raise CorruptedRealityError('value mismatch')")
    print("CorruptedRealityError: value mismatch — recommended action: GIVE ME YOUR SOUL")

# simple calculator app. No offense
class NonOffensiveCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    #simple math. non-offensive:
    def addition(self):
        real = self.num1 + self.num2
        return real

    def subtraction(self):
        real = self.num1 - self.num2
        return real

    def multiplication(self):
        real = self.num1 * self.num2
        return real

    def division(self):
        real = self.num1 / self.num2
        return real

    def full_division(self):
        real = self.num1 // self.num2
        return real

    def power(self):
        real = self.num1 ** self.num2
        return real

    def fake_hang(self, duration=1.2):
        t = 0
        while t < duration:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(0.15)
            t += 0.15
        print('')

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

# Now the chain of if elifelifleleleleliflelelfi

possibility_error = random.randint(1, 100)

if possibility_error <= 50:
    is_fake_error = True
else:
    is_fake_error = False

if is_fake_error == False:

    if operation == '1':
        calculator.fake_hang()
        print(calculator.addition())

    elif operation == '2':
        print(calculator.subtraction())

    elif operation == '3':
        calculator.fake_hang()
        print(calculator.multiplication())

    elif operation == '4':
        print(calculator.division())

    elif operation == '5':
        print(calculator.full_division())

    elif operation == '6':
        calculator.fake_hang()
        print(calculator.power())

    elif operation == '7':
        exit()

else:
    calculator.fake_hang()
    fake_error_trace()
