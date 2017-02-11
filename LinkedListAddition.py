class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)

        iNode3 = l3
        carry = 0

        while l1 or l2 or carry == 1:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            sum = v1 + v2 + carry
            carry = int(sum / 10)
            iNode3.next = ListNode(sum % 10)
            iNode3 = iNode3.next

        return l3.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)

obj = Solution()
obj.addTwoNumbers(l1, l2)