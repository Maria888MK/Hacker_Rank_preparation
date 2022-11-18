########################################## Phone Number #############################################
"""
You are given some input, and you are required to check whether they are valid mobile numbers.
A valid mobile number is a ten digit number starting with a 7,8 or 9 .
input:
2
9587456281
1252478965
output:
YES
NO
"""
import re
n = int(input())
for i in range(n):
    ph_number = input()
    match = re.search('^[7-9]\d{9}$', ph_number)
    if match:
        print('YES')
    else:
        print('NO')
########################################## Re.split() #############################################
"""
Your task is to complete the regex_pattern defined below, which will be used to re.split() all 
of the , and . symbols in .
It’s guaranteed that every comma and every dot in  is preceeded and followed by a digit.
input:
100,000,000.000
output:
100
000
000
000
"""
import re
regex_pattern = r"[,.]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, input())))
######################################### Detect Floating Point Number #############################
'''
You are given a string N .
Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
input:
4
4.0O0
-1.00
+4.54
SomeRandomStuff
output:
False
True
True
False
'''
import re
T = int(input())

for _ in range(T):
    match = re.search(r"^[\+\-]?[0-9]*\.[0-9]+$", input())
    # ^[\+\-]?[0-9]*\.[0-9]+$"
    if match:
        print('True')
    else:
        print('False')