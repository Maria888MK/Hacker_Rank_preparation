#################################################### Integer divisions ################################################
"""
You are given two values a and b .
Perform integer division and print a/b.
input:
3
1 0
2 $
3 1
output:
Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""
for _ in range(int(input())):

    try:
        a, b = map(int, input().split())
        print(int(a / b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)
#################################################### Incorrect Regex ###############################################
"""
You are given a string  S.
Your task is to find out whether S is a valid regex or not.
input:
2
.*\+
.*+
output:
True
False
"""
import re
for _ in range(int(input())):
    try:
        re.compile(input())
    except re.error:
        print("False")
    else:
        print('True')