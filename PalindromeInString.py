class Solution(object):
    def isPalindrome(self, s):
        """
        :type head: ListNode
        :rtype: bool
        """

        chars = list(s)

        if len(s) <= 1:
            return len(s)
        maxSize = 1

        for index, char in enumerate(chars):

            # For the odd palindromes aba
            temp = self.helper(s, index, index)
            if maxSize < len(temp):
                maxSize = len(temp)

            # for the even palindromes abba
            temp = self.helper(s, index, index+1)
            if maxSize < len(temp):
                maxSize = len(temp)

        return maxSize

    # This searches for palindromes in the strings keep l and r as the starting point
    def helper(self, st, l, r):
        while l >= 0 and r < len(st) and st[l] == st[r]:
            l -= 1
            r += 1

        return st[l+1:r]

testSol = Solution()
# test = ListNode(1)
# test.next = ListNode(1)
# test.next.next = ListNode(3)
# test.next.next.next = ListNode(1)
# test.next.next.next.next = ListNode(1)
test = "babajbdabaaaab"

print(testSol.isPalindrome(test))