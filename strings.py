"""You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa."""
####################################### Swap case #####################################################
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
####################################### Split & Join ##################################################
"""You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
input:
this is a string   
output:
this-is-a-string
"""
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
####################################### Greeting ##################################################
"""You are given the firstname and lastname of a person on two different lines. 
Your task is to read them and print the following:
Hello firstname lastname! You just delved into python.
"""
def print_full_name(first, last):
    print('Hello {} {}! You just delved into python.'.format(first_name,last_name))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
####################################### Find a string ##############################################
"""
the user enters a string and a substring. You have to print the number of times 
that the substring occurs in the given string. String traversal will take place 
from left to right, not from right to left.
input:
ABCDCDC
CDC
output:
2
"""


def count_substring(string, sub_string):
    results = 0
    sub_len = len(sub_string)
    for i in range(len(string)):
        if string[i:i + sub_len] == sub_string:
            results += 1
    return results

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
####################################### String Validators ##############################################
"""
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, 
digits, lowercase and uppercase characters
input:
qA2
Output:
True
True
True
True
True
"""
if __name__ == '__main__':
    s = input()
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
################ Second solution ##################
    if __name__ == '__main__':
        s = input()
        for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
            print(any(method(i) for i in s))
####################################### Text Alignment - logo #######################################
"""
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
input:5
output:
   H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
####################################### Text Wrap  ################################################
"""
You are given a string s  and width w.
Your task is to wrap the string into a paragraph of width  w.
input:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
output:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
"""
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
####################################### Mutations  ################################################
"""
Read a given string, change the character at a given index and then print the modified string.
input:
abracadabra  
5 k  
output:
abrackdabra
"""
############# Solution 1 - convert the string to a list and then change the value ###########
def mutate_string(string, position, character):
    l = list(string)
    l[position]= character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
######### Solution 2 - slice the string and join it back ################
def mutate_string(string, position, character):
    string = string [:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
####################################### Designer Door Mat  ##########################################
"""
Mat size must be N X M. (N is an odd natural number, and M is 3*N times .)
input: 9 27
output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
N, M = map(int,input().split())
for i in range(1,N,2):
    print (('.|.'*i).center(M,'-'))
print(("WELCOME").center(M,'-'))
for i in range(N-2,-1,-2):
    print (('.|.'*i).center(M,'-'))
####################################### String Formatting  ##########################################
'''
Given an integer,n , print the following values for each integer  from  to :
Decimal
Octal
Hexadecimal (capitalized)
Binary
input:17
output:
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''
def print_formatted(number):

    w = len(str(bin(number)).replace('0b',''))
    for i in range(1, number+1):
        b = bin(int(i)).replace('0b','').rjust(w, ' ')
        o = oct(int(i)).replace('0o','', 1).rjust(w, ' ')
        h = hex(int(i)).replace('0x','').upper().rjust(w, ' ')
        j = str(i).rjust(w, ' ')
        print (j, o, h, b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
####################################### Alphabet Rangoli ##########################################
"""
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form 
of Indian folk art based on creation of patterns.) 
input:5
output:
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string
def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
####################################### Capitalize ##########################################
"""
Given a full name, your task is to capitalize the name appropriately.
input:chris alan
output:Chris Alan
"""

# Complete the solve function below.
def solve(s):
    s =s.split(" ")
    result = []
    for i in s:
        capitalized = str(i).capitalize()
        result.append(capitalized)
    return ' '.join(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
