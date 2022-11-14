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