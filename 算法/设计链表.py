class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head=None



    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """

        if self.head is None:
            return  -1
        if index==0:
            return self.head.val
        else:
            i=1
            cur=self.head
            while cur.next:
                if index==i:
                    result=cur.next.val
                    cur = cur.next
                    return  result
                else:
                    cur = cur.next
                i=i+1
            return  -1



    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        pre=ListNode(val)
        pre.next=self.head
        self.head=pre
        return  self.head


    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        cur=self.head
        if self.head is None:
            self.head=ListNode(val)
        else:
            while cur.next:
                cur=cur.next
            cur.next=ListNode(val)
        return self.head

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        length=self.length()
        if index==0:
            self.head=self.addAtHead(val)
            return self.head
        if index==length:
            self.head=self.addAtTail(val)
            return self.head
        if index>length:
            self.head=self.head
        else:
            i=1
            pre=self.head
            while pre.next:
                if index==i:
                    addnode=ListNode(val)
                    addnode.next=pre.next
                    pre.next = addnode
                else:
                    pre = pre.next
                i=i+1
            return self.head

    def length(self):
        if self.head is None:
            len=0
        else:
            cur=self.head
            len=0
            while cur:
                len=len+1
                cur=cur.next
        return len

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index==0:
            self.head=self.head.next
        length = self.length()
        if index!=0 and index<length:
            i=1
            cur=self.head
            while cur:
                if index==i:
                    cur.next=cur.next.next
                    cur = cur.next
                else:
                    cur=cur.next
                i=i+1
            return  self.head
        else:
            return '索引无效'




    def printnode(self):
        cur=self.head
        while cur:
            print(cur.val)
            cur=cur.next
        return self.head




    def printnode(self):
        cur=self.head
        while cur:
            print(cur.val)
            cur=cur.next
        return self.head


if __name__ == '__main__':
   #["MyLinkedList", "addAtHead", "addAtHead", "deleteAtIndex", "addAtIndex", "addAtTail", "addAtIndex", "addAtTail",
   #  "addAtHead", "addAtHead", "addAtHead", "addAtTail", "addAtTail", "addAtHead", "addAtTail", "addAtTail",
   #  "addAtHead", "addAtTail", "deleteAtIndex", "addAtTail", "addAtTail", "get", "addAtIndex", "addAtHead", "get",
   #  "get", "addAtHead", "get", "addAtIndex", "addAtTail", "addAtIndex", "addAtHead", "addAtHead", "addAtHead", "get",
   #  "addAtHead", "addAtIndex", "addAtTail", "addAtHead", "addAtIndex", "get", "addAtTail", "addAtTail", "addAtIndex",
   #  "addAtIndex", "addAtHead", "addAtHead", "get", "addAtTail", "addAtIndex", "addAtIndex", "addAtHead",
   #  "deleteAtIndex", "addAtIndex", "addAtHead", "deleteAtIndex", "addAtTail", "deleteAtIndex", "addAtTail",
   #  "addAtHead", "addAtTail", "addAtTail", "addAtHead", "addAtTail", "addAtIndex", "deleteAtIndex", "addAtHead",
   #  "addAtHead", "addAtHead", "addAtTail", "get", "addAtIndex", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex",
   #  "get", "addAtHead", "get", "get", "addAtTail", "deleteAtIndex", "addAtTail", "addAtIndex", "addAtHead",
   #  "addAtIndex", "addAtTail", "get", "addAtIndex", "addAtIndex", "addAtHead", "addAtHead", "get", "get", "get",
   #  "addAtIndex", "addAtHead", "addAtIndex", "addAtHead", "addAtTail", "addAtIndex", "get"]
   # [[], [38], [45], [2], [1, 24], [36], [3, 72], [76], [7], [36], [34], [91], [69], [37], [38], [4], [66], [38], [14],
   #  [12], [32], [5], [7, 5], [74], [7], [13], [11], [8], [10, 9], [19], [3, 76], [7], [37], [99], [10], [12], [1, 20],
   #  [29], [42], [21, 52], [11], [44], [47], [6, 27], [31, 85], [59], [57], [4], [99], [13, 83], [10, 34], [48], [9],
   #  [22, 64], [69], [33], [5], [18], [87], [42], [1], [35], [31], [67], [36, 46], [23], [64], [81], [29], [50], [23],
   #  [36, 63], [8], [19], [98], [22], [28], [42], [24], [34], [32], [25], [53], [55, 76], [38], [23, 98], [27], [18],
   #  [44, 27], [16, 8], [70], [15], [9], [27], [59], [40, 50], [15], [11, 57], [80], [50], [23, 37], [12]]
    mylinkedlist=MyLinkedList()
    mylinkedlist.addAtHead(38)
    mylinkedlist.addAtHead(45)
    mylinkedlist.deleteAtIndex(2)
    # mylinkedlist.addAtHead(4)
    # mylinkedlist.addAtHead(5)
    # mylinkedlist.addAtHead(6)
    # print('在尾部添加元素－－－－－－－－－')
    # mylinkedlist.addAtTail(7)
    # mylinkedlist.printnode()
    # print('长度－－－－－－－－－')
    # #获取某个索引元素
    # #mylinkedlist.get(7)
    # print(mylinkedlist.length())
    # #插入元素
    # print('插入元素－－－－－－－－－')
    # mylinkedlist.addAtIndex(1,2)
    # mylinkedlist.printnode()
    # print('删除索引是xx的元素－－－－－－－－－')
    # mylinkedlist.deleteAtIndex(1)
    # mylinkedlist.printnode()

