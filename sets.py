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