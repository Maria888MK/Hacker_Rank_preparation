########################################### Input ################################################
"""
The first line contains the space separated values of x and k .
The second line contains the polynomial P.
input:
1 4
x**3 + x**2 + x + 1
output:
True
"""
x, k = input().split()
x,k = int(x),int(k)
polynomial = input()
result = eval(polynomial) #perform_calculation
if result== k:
    print(True)
else:
    print(False)
########################################### Any, All - Palindromic integer ######################################
"""
You are given a space separated list of integers. If all the integers are positive, 
then you need to check if any integer is a palindromic integer.
input:
5
12 9 61 5 14 
output:
True
"""
N = int(input())
s = list(map(int, input().split()))

if all(val > 0 for val in s) and any(((str(i)==str(i)[::-1]) for i in s)):
        print(True)
else:
    print(False)
########################################### Python Evaluation #################################################
"""
You are given an expression in a line. Read that line as a string variable, such as var, 
and print the result using eval(var).
input:
print(2 + 3)
output:
5
"""
eval(input())
########################################### Zipped #################################################
"""
Your task is to compute the average scores of each student
input:
Your task is to compute the average scores of each student
output:
90.0 
91.0 
82.0 
90.0 
85.5
"""
N, X = map(int,input().split())

subjects = [list(map(float, input().split())) for _ in range(X)]
for grade in zip(*subjects):
    print(sum(grade)/len(grade))