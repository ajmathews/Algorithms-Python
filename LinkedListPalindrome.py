# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        if fast is not None:
            slow = slow.next

        rever = self.reverse(slow)

        while rever is not None:
            if rever.val != head.val:
                return False

            rever = rever.next
            head = head.next

        return True

    def reverse(self, head):
        rev = None
        prev = None

        while head is not None:
            rev = ListNode(head.val)
            rev.next = prev
            prev = rev
            head = head.next

        return rev



testSol = Solution()
test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(1)
test.next.next.next.next = ListNode(1)

print(testSol.isPalindrome(test))