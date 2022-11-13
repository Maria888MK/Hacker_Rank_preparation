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
####################################### Find a string ##################################################
"""the user enters a string and a substring. You have to print the number of times 
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