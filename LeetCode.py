# 1328. Break a Palindrome https://leetcode.com/problems/break-a-palindrome/
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b'
# 1010. Pairs of Songs With Total Durations Divisible by 60
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
#Approach 1: Brute Force
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs, n = 0, len(time)
        for i in range(n):
            # j starts with i+1 so that i is always to the left of j
            # to avoid repetitive counting
            for j in range(i + 1, n):
                pairs += (time[i] + time[j]) % 60 == 0
        return pairs
#Approach 2: Modulo and Count
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        ans, cnt = 0, [0] * 60
        for t in time: cnt[t % 60] += 1
        for i in range(1, 30): ans += cnt[i] * cnt[60 - i]
        return ans + cnt[0] * (cnt[0] - 1) // 2 + cnt[30] * (cnt[30] - 1) // 2
# 1836. Remove Duplicates From an Unsorted Linked List
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        count = Counter()
        curr = head
        while curr:
            count[curr.val] += 1
            curr = curr.next

        sentinel = ListNode(-1, head)
        curr = sentinel
        while curr and curr.next:
            if count[curr.next.val] > 1:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return sentinel.next
# 1041. Robot Bounded In Circle https://leetcode.com/problems/robot-bounded-in-circle/
# https://github.com/leetcode/solution_assets/blob/master/solution_assets/1041_robot_bounded_in_circle/robot_trajectory.ipynb
class Solution(object):
    def isRobotBounded(self, instructions):
        x = y = 0
        direction = 0
        possible_moves = {0: [0,1], 1: [1,0], 2: [0,-1], 3: [-1,0]}
        for instruction in instructions:
            if instruction == 'L':
                direction = (direction + 3)% 4
            elif instruction == 'R':
                direction = (direction + 1)% 4
            else:
                x = x + possible_moves[direction][0]
                y = y + possible_moves[direction][1]
        return (x==0 and y ==0) or direction !=0
# 696. Count Binary Substrings https://leetcode.com/problems/count-binary-substrings/
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        res = 0
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        for i in range(1, len(groups)):
            res += min(groups[i - 1], groups[i])
        return res
# 1356. Sort Integers by The Number of 1 Bits https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution(object):
    def sortByBits(self, arr):
        return sorted(arr, key = lambda num : (sum((num >> i) & 1 for i in range(32)), num))


def sortByBits(self, arr: List[int]) -> List[int]:
    buckets = [[] for _ in range(15)]
    res = []
    for n in arr:
        nn = n
        ones = 0

        while n:
            n = n & (n - 1)
            ones += 1
        buckets[ones].append(nn)

    for buck in buckets:
        buck.sort()

        for n in buck:
            res.append(n)

    return res
# 1209. Remove All Adjacent Duplicates in String II https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        counter_stack = []
        for val in s:
            if not stack or stack[-1]!=val:
                stack.append(val)
                counter_stack.append(1)
            elif stack[-1]==val:
                counter_stack[-1]+=1
            if counter_stack[-1]==k:
                counter_stack.pop()
                stack.pop()
        return ''.join([stack[i]*counter_stack[i] for i in range(len(stack))])
# 647. Palindromic Substrings
class Solution(object):
    def countSubstrings(self, s):
        # def countSubstrings(self, s: str) -> int:
        ps = [[i] for i in range(len(s))]

        for i in range(1, len(s)):
            c = s[i]
            for start in ps[i - 1]:
                if start - 1 >= 0 and s[start - 1] == c:
                    ps[i].append(start - 1)
            if s[i - 1] == c:
                ps[i].append(i - 1)

        return sum([len(y) for y in ps])
# 166. Fraction to Recurring Decimal https://leetcode.com/problems/fraction-to-recurring-decimal/
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return "0"
        negative_sign = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        result = ["-"] if negative_sign else []
        result.append(str(numerator // denominator))
        numerator %= denominator

        seen_numerator = {}
        if numerator == 0:
            return "".join(result)

        result.append(".")
        while numerator != 0:
            if numerator in seen_numerator:
                result.append(")")
                small_pos = seen_numerator[numerator]
                return "".join(result[:small_pos]) + "(" + "".join(result[small_pos:])
            seen_numerator[numerator] = len(result)
            numerator *= 10
            val = numerator // denominator
            numerator %= denominator
            result.append(str(val))
        return "".join(result)
# 1395. Count Number of Teams https://leetcode.com/problems/count-number-of-teams/
class Solution(object):
    def numTeams(self, rating):
        asc = dsc = 0
        for i,v in enumerate(rating):
            llc = rgc = lgc = rlc =0
            for l in rating[:i]:
                if l < v:
                    llc += 1
                if l > v:
                    lgc += 1
            for r in rating[i+1:]:
                if r > v:
                    rgc += 1
                if r < v:
                    rlc += 1
            asc += llc * rgc
            dsc += lgc * rlc
        return asc + dsc
# 457. Circular Array Loop https://leetcode.com/problems/circular-array-loop/
class Solution(object):
    def circularArrayLoop(self, nums):
        for i , num in enumerate(nums):
            mark = 3000+i
            # the number in array is in [-1000,1000], so I add a random integer greater than 2000
            while nums[i]<2000 and nums[i]*num>0 and nums[i]%len(nums):
           # just compare nums[i] with 2000, we can get the same result as the type conversion
                num = nums[i]
                nums[i] = mark
                i = (i+num)%len(nums)
            if nums[i]==mark:
                return True
        return False
# 387. First Unique Character in a String https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution(object):
    def firstUniqChar(self, s):
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
# 1413. Minimum Value to Get Positive Step by Step Sum https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
class Solution(object):
    def minStartValue(self, nums):
        min_val_sum = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            min_val_sum = min(min_val_sum, curr_sum)
        return 1 if min_val_sum >= 0 else -(min_val_sum) + 1
# 443. String Compression https://leetcode.com/problems/string-compression/
class Solution(object):
    def compress(self, chars):
        if len(chars) == 1:
            return len(chars)

        charsLen = len(chars)
        count = 1
        for i in range(charsLen):
            val = chars.pop(0)
            if not chars or val != chars[0] or i == charsLen - 1:
                chars.append(val)
                if count > 1:
                    for x in str(count): chars.append(x)
                count = 1
            else:
                count += 1
        print(chars)
        return len(chars)
# 532. K-diff Pairs in an Array https://leetcode.com/problems/k-diff-pairs-in-an-array/
from collections import Counter

class Solution:
    def findPairs(self, nums, k):
        result = 0

        counter = Counter(nums)

        for x in counter:
            if k > 0 and x + k in counter:
                result += 1
            elif k == 0 and counter[x] > 1:
                result += 1
        return result
# 657. Robot Return to Origin https://leetcode.com/problems/robot-return-to-origin/
class Solution(object):
    def judgeCircle(self, moves):
        if not moves:
            return True

        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False
# 338. Counting Bits https://leetcode.com/problems/counting-bits/
class Solution(object):
    def countBits(self, n):
        ans = [0] * (n + 1)
        for x in range(1, n + 1):
            ans[x] = ans[x & (x - 1)] + 1
        return ans
