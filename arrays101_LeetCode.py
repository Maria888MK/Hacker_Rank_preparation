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
#    Duplicate Zeros https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
  class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i< len(arr):
            if arr[i]==0:
                # arr[i:i]=0
                arr.insert(i,0)
                arr.pop()
                i +=2
            else:
                i +=1
# Merge Sorted Arrays https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        nums1 = nums1+nums2
        for i in range(len(nums1)):
            if 0 in nums1:
                nums1.remove(0)
            already_sorted = True  # Bubble Sort

            for j in range(len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                    already_sorted = False

            if already_sorted:
                break

        print(nums1)
      # Merge and sort approach:
    class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]= nums2[i]
        nums1.sort
        # time complexity O(n+m)log(n+m)
        # space complexity O(n)
       # Two pointers approach
     class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m] # copy all the elements of list
        # pointers for two arrays:nums1_copy and nums2 
        p1 = 0
        p2 = 0
        for i in range(n+m):
            if p2>=n or (p1<m and nums1_copy[p1]<=nums2[p2]):
                nums1[i] = nums1_copy[p1]
                p1 +=1
            else:
                nums1[i] = nums2[p2]
                p2 +=1 # Time complexity O(n+m)
                # Space complexity O(m)
    
