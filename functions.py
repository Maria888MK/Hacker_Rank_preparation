############################################ Fibonaci #######################################################
"""
ou have to generate a list of the first  fibonacci numbers, 0 being the first number.
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.
input:
5
output:
[0, 1, 1, 8, 27]
"""
cube = lambda x: x**3

def fibonacci(n):
    if(n == 0):
        lst = []
    elif(n == 1):
        lst = [0]
    else:
        lst = [0, 1]
        for i in range(2,n):
                lst.append(lst[-2] + lst[-1])
    return lst




if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))