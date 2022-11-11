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
# input:
# 5
# 2 3 6 6 5
# expected output: 5
if __name__ == '__main__':
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