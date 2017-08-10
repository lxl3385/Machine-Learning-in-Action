#! ~/mainML/
""" test the funcation of avg"""
# -*- coding: utf-8 -*-

N = 5
sum = 0
count = 0
while count < N:
    number = float(input("Enter number: "))
    sum = sum + number
    count = count + 1
average = sum / N
print("N = {}, Sum = {}".format(N, sum))
print("Average = {:.2f}".format(average))