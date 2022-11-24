#   1480. Running Sum of 1D Array https://leetcode.com/problems/running-sum-of-1d-array/
# Prefix Sum Array https://www.geeksforgeeks.org/python-prefix-sum-list/
# Method 1 Using accumulate(iterable) method.
from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
# Method 2  Using list comprehension + sum() + list slicing 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[ : i + 1]) for i in range(len(nums))]
Method#3: Using For loop and list indexing O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        res[0] = nums[0]
        for i in range(1, len(nums)):
            res[i] = res[i-1] + nums[i]
        return res
# 1672. Richest Customer Wealth https://leetcode.com/problems/richest-customer-wealth/
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealth = 0
        
        for customer in accounts:
            cur_customer_wealth = 0
            for bank in customer:
                cur_customer_wealth+= bank
                
            maxwealth = max(maxwealth, cur_customer_wealth )
        return maxwealth
# Time complexities O(n x m) n- customers, m-banks
# Space complexity O(1) - we don't create another data structure
# 412. Fizz Buzz https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if (i%3 == 0) and (i%5 ==0):
                res.append('FizzBuzz')
            elif i%3 ==0:
                res.append('Fizz')
            elif i%5 ==0:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res
# Time complexity O(n), space Complexity O(1)- we don't create another data structure, operate only on input
# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:            
            if num %2 == 0:
                num = num / 2
                count +=1
            elif num % 2 !=0:
                obtain_odd = num -1
                num = num -1
                count +=1
                
        return count
 # Time complexity O(logn), space complexity O(1) n- number of steps
# Approach 2: Counting Bits complexity is the same
def numberOfSteps (self, num: int) -> int:
    binary = bin(num)[2:] #Remove the "0b" off the start with splice.
    ones = binary.count("1")
    total = len(binary)
    return ones + total - 1

                
            


