class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

testSol = Solution()
# test = ListNode(1)
# test.next = ListNode(1)
# test.next.next = ListNode(3)
# test.next.next.next = ListNode(1)
# test.next.next.next.next = ListNode(1)
test = "babajbdabaaaab"

print(testSol.myPow(2,6))