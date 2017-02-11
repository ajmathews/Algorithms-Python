# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        slow, fast = head, head

        for i in range(0, n):
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        print(slow.val)


testSol = Solution()
test = ListNode(1)
test.next = ListNode(1)
test.next.next = ListNode(3)
test.next.next.next = ListNode(1)
test.next.next.next.next = ListNode(8)

print(testSol.removeNthFromEnd(test, 1))