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
##################################### Intertools combinations ################################
"""
You are given a string s .
Your task is to print all possible combinations, up to size k , of the string in lexicographic 
sorted order.
input:
HACK 2
output:
A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations
s, k = input().split()
s = sorted(str(s).upper())
k = int(k)
for i in range(k):
    comb = (combinations(s,i+1))
    print(*sorted(map(''.join, comb)), sep="\n")
######################## Intertools combinations with replacement ################################
"""description of the task is above
input:
HACK 2
output:
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
"""
from itertools import combinations_with_replacement
s, k = input().split()
s = sorted(str(s).upper())
k = int(k)
comb = sorted(combinations_with_replacement(s,k))
l = map(''.join,comb)
print(*l, sep='\n')
######################## Intertools permutation ################################
"""
You are given a string S .
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.
input:
HACK 2
output:
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
"""
from itertools import permutations
s, k =input().split()
k = int(k)
s = sorted(str(s).upper())
permutation = sorted(permutations(s,k))
l = map(''.join,permutation)
print(*l, sep='\n')
############## Second solution ##################
from itertools import permutations as p
x,y=input().split()
a=sorted(list(p(list(x),int(y))))
for i in a:
    print(''.join(i))
