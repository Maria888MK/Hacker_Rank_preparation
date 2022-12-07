#   Find Numbers with Even Number of Digits https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3237/
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_nb = 0
        for i in range(len(nums)):
            number= len(str(nums[i]))
            if number %2==0:
                even_nb +=1
        return even_nb
  # Squares of a Sorted Array https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3240/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [i*i for i in nums]
        result.sort()
        return result
