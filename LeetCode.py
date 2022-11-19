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