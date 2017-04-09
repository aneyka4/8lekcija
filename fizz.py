# -*- coding: utf-8 -*-
cifra = int(raw_input("Vnesi število med 1 in 100: "))
num = 1

while num <= cifra:
    if (num % 5 == 0 and num % 3 == 0):
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
    if num == "cifra":
        break
    num = (num + 1)