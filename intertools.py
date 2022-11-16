##################################### Cartesian Product ######################################################
"""
You are given a two lists A and  B. Your task is to compute their cartesian product A X B.
input:
 1 2
 3 4
output:
 (1, 3) (1, 4) (2, 3) (2, 4)
"""
from itertools import product
A = set(map(int, input().split()))
B = set(map(int , input().split()))
cart_prod = list(product(A, B))
for i in cart_prod:
    print(i, end=" ") # output result in one line
