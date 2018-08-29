# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1=ListNode(l1)
        l2=ListNode(l2)
        head=cur=ListNode(0)
        while l1 and l2:
             if l1.val>l2.val:
                 cur.next=l2
                 l2=l2.next
             else:
                 cur.next = l1
                 l1 = l1.next
             cur=cur.next
        cur.next = l1 or l2
        return (head.next)






solution = Solution()
l1=[1,2,4]
l2=[1,3,4]
solution.mergeTwoLists(l1,l2)
