####################################### Average ##############################################################
"""
Ms. Gabriel Williams is a botany professor at District College. One day, she asked her
student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
input:
10
161 182 161 154 176 170 167 171 170 174
output:
169.375
"""
def average(array):
    array = set(array)
    total_number = len(array)
    avg = sum(array) / total_number
    return avg


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
####################################### Symmetric Difference ###########################################
"""
Given 2 sets of integers,  and , print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
input:
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
output:
5
9
11
12
"""
size_m = int(input())
m =  set(list(map(int, input().split())))
size_n = int(input())
n =  set(list(map(int, input().split())))
diff_m = set(sorted(m.difference(n)))
diff_n = set(sorted(n.difference(m)))
all_diff = set(sorted(diff_m.union(diff_n)))
result = list(sorted(all_diff))
for i in range(len(result)):
    print(result[i])
####### second soluution #########
m =int(input())
a = set(map(int,input().split()))

n=int(input())
b=set(map(int,input().split()))

c= sorted((a.difference(b)).union(b.difference(a)))
for x in c:
    print(x)
####################################### Distinct Countries ###########################################
"""
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the total number of distinct
 country stamps in her collection. She asked for your help. You pick the stamps one by one from a 
 stack of  country stamps.Find the total number of distinct country stamps.
input:
7
UK
China
USA
France
New Zealand
UK
France 
output:
5
"""
n =int(input())
countries = []
for i in range(n):
    countries.append(list(map(str, input().split('\n'))))
countries = [i[0] for i in countries] #get rid of nested lists
dist_countries = len(set(countries))
print(dist_countries)
####################### Second solution ####################
n = int(input())
my_set = set()
for i in range(n):
    s = input()
    my_set.add(s)
print(len(my_set)
####################################### input cmd&remove elements ###########################################
""" 
You have a non-empty set , and you have to execute  commands given in  lines.
The commands will be pop, remove and discard.
input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
output:
4
"""
n = int(input())
s = set(map(int, input().split()))

N = int(input())

for i in range(N):
    command = input().split()
    if 'pop' in command:
        s.pop()
    elif 'remove' in command:
        s.remove(int(command[-1]))
    elif 'discard' in command:
        s.discard(int(command[-1]))
        
    
print(sum(s))
####################################### union section ###########################################
"""
The students of District College have subscriptions to English and French newspapers.
Some students have subscribed only to English, some have subscribed to only French 
and some have subscribed to both newspapers.
You are given two sets of student roll numbers. One set has subscribed to the English
newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of
students who have subscribed to at least one newspaper.
input:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
output:
13
"""
n_eng = int(input())
eng =set(map(int,input().split()))
b_fr = int(input())
fr =set(map(int,input().split()))
result = eng.union(fr)
print(len(result))

####################################### inter section ###########################################
""" task descriptionis the same as above 
ur task is to find the total number of students who have subscribed to both newspapers.
"""
n = int(input())
n_eng = set(map(int, input().split()))
b = int(input())
b_fr = set(map(int, input().split()))
result = n_eng.intersection(b_fr)
print(len(result))
####################################### difference ###########################################
""" task description is the same as above
 Your task is to find the total number of students who have subscribed to only English newspapers.

"""
n = int(input())
n_eng = set(map(int, input().split()))
b = int(input())
b_fr = set(map(int, input().split()))
result = n_eng.difference(b_fr)
print(len(result))
####################################### symmetric difference ###########################################
""" task description is the same as above
Your task is to find the total number of students who have subscribed to either the English
or the French newspaper but not both.
"""    
n = int(input())
n_eng = set(map(int, input().split()))
b = int(input())
b_fr = set(map(int, input().split()))
result = n_eng.symmetric_difference(b_fr)
print(len(result))
