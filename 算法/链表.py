# Definition for singly-linked list.
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class ListoPerate:
    def __init__(self,root):
        self.root=root
    # 表首端加入元素
    def addNodedfirst(self,l2):
        if self.root ==None:
            self.root=ListNode(l2)
        else:
            addnode=ListNode(l2)
            addnode.next=self.root
            self.root=addnode
            return self.root
    # 表尾端加入元素
    # 在链表的最后插入元素，必须先找到链表的最后一个结点。其实首先是一个扫描循环，找到相应结点后把包含新元素的结点插入在其后
    def addNodeLast(self,l2):
        if self.root==None:
            self.root=ListNode(l2)
        else:
            cur=self.root
            while cur.next:
                cur=cur.next
            cur.next=ListNode(l2)
        return self.root

    # 选定一个位置插入数据：先找到要删元素所在节点的前一结点，设用变量pre指向，然后修改pre的next域，使之指向被删结点的下一结点
    # 删除表中的元素
    def rmNode(self,l):
        nonenode=ListNode(None)
        nonenode.next=self.root
        self.root=nonenode
        pre=self.root
        while pre.next:
            if pre.next.val==l:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return self.root

    def printnode(self):
        cur=self.root
        while cur:
            print(cur.val)
            cur=cur.next
        return self.root



if __name__ == '__main__':
    #创建空链表
    listnode=ListNode(None)
    listoperate = ListoPerate(listnode)
    #加入元素－表首端插入
    #listoperate.addNodedfirst(1)
    #listoperate.addNodedfirst(2)
    #listoperate.addNodedfirst(3)
    #listoperate.addNodedfirst(4)
    #listoperate.addNodedfirst(5)
    #listoperate.addNodedfirst(6)
    #listoperate.addNodedfirst(7)
    #listoperate.printnode()
    #加入元素－尾端插
    #listoperate.addNodeLast('a')
    #listoperate.addNodeLast('b')
    #listoperate.addNodeLast('c')
    #listoperate.addNodeLast('d')
    #listoperate.addNodeLast('e')
    #listoperate.addNodeLast('f')
    #listoperate.addNodeLast('g')
    listoperate.addNodeLast(1)
    listoperate.addNodeLast(2)
    listoperate.addNodeLast(6)
    listoperate.addNodeLast(3)
    listoperate.addNodeLast(4)
    listoperate.addNodeLast(5)
    listoperate.addNodeLast(6)
    listoperate.rmNode(6)
    listoperate.printnode()












