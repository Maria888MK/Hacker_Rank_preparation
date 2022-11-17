################################################ Counter ########################################################
"""
ryan  is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.
Your task is to compute how much money  earned.
input:
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
output:
200
"""
import itertools, collections
from collections import Counter
X = int(input())
sizes_lst =list(map(int, input().split()))
N = int(input())
earning = 0
for lines in range(N):
    s_size, cost = map(int, input().split())
    if s_size in sizes_lst:
        earning += cost
        sizes_lst.remove(s_size)
print(earning)
############# Second solution ###################
# Read input
num_shoes = int(input())
stock = list(map(int, input().split()))
num_customers = int(input())
customers = []
for i in range(num_customers):
    customers.append(tuple(map(int, input().split())))
# --------------------------------
# Calculate income
# --------------------------------
income = 0
for size, price in customers:
    if size in stock:
        stock.remove(size)
        income += price

print(income)
################################################ DefaultDict  ########################################################
"""
Group A contains 'a', 'b', 'a' Group B contains 'a', 'c'

For the first word in group B, 'a', it appears at positions  and  in group A. The second word, 'c', does not appear
 in group A, so print -1.
input:
STDIN   Function
-----   --------
5 2     group A size n = 5, group B size m = 2
a       group A contains 'a', 'a', 'b', 'a', 'b'
a
b
a
b
a       group B contains 'a', 'b'
b
Expected output:
1 2 4
3 5
"""
from collections import defaultdict

A = defaultdict(list)
n, m = map(int, input().split())

for i in range(1, n+1):
    A[input()].append(str(i))

for _ in range(m):
    val = input()
    if val in A:
        print(" ".join(A[val]))
    else:
        print(-1)
########################################### Collections.OrderedDict() ################################################
"""
You are the manager of a supermarket.
You have a list of N items together with their prices that consumers bought on a particular day.
Your task is to print each item_name and net_price in order of its first occurrence.
item_name = Name of the item.
net_price = Quantity of the item sold multiplied by the price of each item.
input:
9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
output:
BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
"""
from collections import OrderedDict

purchased_items = OrderedDict()
N = int(input())
for i in range(N):
    item_name, price = input().rsplit(' ', 1)
    if item_name in purchased_items:
        purchased_items[item_name] += int(price)
    else:
        purchased_items[item_name] = int(price)
for item in purchased_items:
    print(item, purchased_items[item])
########################################### Collections.namedtuple() ################################################
"""Your task is to help Dr. Wesley calculate the average marks of the students.
Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)
input:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6 
output:
78.00
"""
from collections import namedtuple
n = int(input())
Student_marks = namedtuple('Student_marks', input().split())
sum = 0
for i in range(n):
    s = Student_marks(*input().split())
    sum += int(s.MARKS)
print("{:.2f}".format(sum/n)) #round  to 2 decimal places.
########################################### Collections.deque() ################################################
"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
output:
1 2
"""
from collections import deque
N = int(input())
d = deque()
for _ in range(N):
    cmd = input().strip().split(" ")
    if cmd[0]== 'append':
        d.append(int(cmd[1]))
    if cmd [0] == 'appendleft':
        d.appendleft(cmd[1])
    if cmd[0] == 'pop':
        d.pop()
    if cmd[0] == 'popleft':
        d.popleft()
print(' '.join(map(str, d))) #printout without []
########################## Second solution ########################
from collections import deque
d = deque()
for _ in range(int(input())):
    cmd, *args = input().split()
    getattr(d, cmd)(*args)
[print(x, end=' ') for x in d]