# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:24:24 2020

@author: Hugo Katzer
"""


def FizzBuzz2():
    for num in range(10000):
        output = ""
        if (num % 3 == 0):
            output = output + "Fizz"
        if (num % 5 == 0):
            output = output + "Buzz"
        if (output == ""):
            output = num
        print(output)

FizzBuzz2()