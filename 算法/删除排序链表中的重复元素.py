# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head.next
        if not head:
            return head
        while q:
            if q.val==p.val:
                p.next = q.next
                q = q.next
            else:
                p = p.next
                q = q.next
        return head


solution = Solution()
l1=[1,1,2]
l1=ListNode(l1)
a=solution.deleteDuplicates(l1)
