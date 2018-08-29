class Node:
    def __init__(self,value=None,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

def preTrvarse(root):
    if root==None:
        return
    print(root.value)
    preTrvarse(root.left)
    preTrvarse(root.right)


def midTrarse(root):
    if root==None:
        return
    midTrarse(root.left)
    print(root.value)
    midTrarse(root.right)

def afterTrase(root):
    if root==None:
        return
    afterTrase(root.left)
    afterTrase(root.right)
    print(root.value)

if __name__ == '__main__':
    a=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))
    print('前序')
    preTrvarse(a)
    print('中序')
    midTrarse(a)
    print('后序')
    afterTrase(a)



