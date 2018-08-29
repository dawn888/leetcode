# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        if head is None or head.next is None:
            is_cycle = False
        else:
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    is_cycle = True
                    break
                is_cycle = False
        return is_cycle


if __name__ == '__main__':
    cur=ListNode(1)

