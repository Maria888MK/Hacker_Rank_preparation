"""Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary
to complete the is_leap function."""

####################################### Leap year #####################################################
# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
    return False

year = int(input())
print(is_leap(year))
###### Second solution #######
def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
year = int(input())
print(is_leap(year))
##################################### Runner- up #######################################################
"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up."""
"""input:
5
2 3 6 6 5
expected output: 5
"""
# if __name__ == '__main__':
n = int(input())
arr = set(map(int, input().split()))
winner = max(arr)
arr.remove(winner)
runner_up = max(arr)
print(runner_up)
###### Second solution ####### O(N)
n = int(input())
a = [int(x) for x in input().split()]
largest = secondlargest = -100
for x in a:
    if x > largest:
        tmp = largest
        largest = x
        secondlargest = tmp
    elif x > secondlargest and x != largest:
        secondlargest = x
print(secondlargest)
##################################### Hashing - tuples #################################################
"""Given an integer, n, and n space-separated integers as input, create a tuple,t , of those n integers. 
Then compute and print the result of hash(t).
input:
2
1 2
output:
3713081631934410656"""
n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))
###### Second solution #######
print(input() == 0 or hash(tuple(map(int, input().split()))))
##################################### Finding the percentage ###########################################
"""Print the average of the marks array for the student name provided, showing 2 places after the decimal.
input
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
output
56.00"""
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for name, scores in student_marks.items():
        if name == query_name:
            average = sum(scores)/len(scores)
    print("{:0.2f}".format(average))
###### Second solution #######
from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
query_scores = student_marks[query_name] #Extract the query_scores into a list:
total_scores = sum(query_scores)
avg = Decimal(total_scores/3)
print(round(avg,2))
################################# Nested list - second lowest grade ################################
"""Given the names and grades for each student in a class of  students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
output:
Berry
Harry
"""
from operator import itemgetter
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    lowest = min(records, key=lambda x: x[1])
    records.remove(lowest) # remove element equal to min
    min_in_records = min(records,key=itemgetter(1))[1]
    second_lowest = [x for x in records if x[1] == min_in_records]
    for i in sorted(second_lowest):
        print (i[0])
###### Second solution #######
if __name__ == '__main__':
    # Initiate lists
    name_list = []
    score_list = []
    results = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list.append(name)
        score_list.append(score)
        # the second lowest score in the results list
    for name, score in zip(name_list, score_list):
        if score == sorted(set(score_list))[1]:
            results.append(name)
            # Print the name in the sorted list
    for result in sorted(results):
        print(result)
################################# List - perform commands ##########################################
"""Initialize your list and read in the value of n followed by n lines of commands where 
each command will be of the 7 types listed above. Iterate through each command in order 
and perform the corresponding operation on your list.
input:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    lst = []
    N = int(input())
    for _ in range(N):
        s=input().strip().split(" ")
        if s[0]=="insert":
            lst.insert(int(s[1]),int(s[2]))
        if s[0]=="print":
            print(lst)
        if s[0]=="remove":
            lst.remove(int(s[1]))
        if s[0]=="append":
            lst.append(int(s[1]))
        if s[0]=="sort":
            lst.sort()
        if s[0]=="pop":
            lst.pop()
        if s[0]=="reverse":
            lst.reverse()
################################# List comprehentions - all possible coordinates ####################
"""
input:
1
1
1
2
output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n ]
print(result)
