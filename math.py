##################################### Polar coordinates ############################################
"""
You are given a complex . Your task is to convert it to polar coordinates.
input:
1+2j
output:
 2.23606797749979
 1.1071487177940904
"""
import cmath
z=complex(input())
print(abs(z))
print(cmath.phase(z))
##################################### Div Mod ######################################################
"""
Read in two integers, a and b, and print three lines.
The first line is the integer division  (While using Python2 remember to import division from __future__).
The second line is the result of the modulo operator: .
The third line prints the divmod of a and b.
input:
177
10
output:
17
7
(17, 7)
"""
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print(divmod(a,b))
############ Second solution ####################
a = int(input())
b = int(input())
print("{} \n{} \n{}".format(a // b, a % b, divmod(a, b)))
##################################### Power - Mod Power ######################################################
"""
You are given three integers: a, b, and m. Print two lines.
On the first line, print the result of pow(a,b). On the second line, print the result of pow(a,b,m).
input:
3
4
5
output:
81
1
"""
a = int(input())
b = int(input())
m = int(input())
print("{} \n{}".format(pow(a,b), pow(a,b,m)))
##################################### Integers Come In All Sizes ######################################################
"""
Read four numbers a,b ,c ,d , and , and print the result of a^b +c^d .
input:
9
29
7
27
output:
4710194409608608369201743232

"""