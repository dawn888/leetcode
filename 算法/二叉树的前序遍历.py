# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self,root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.preorderTraversal2(root,[])

    def preorderTraversal2(self,root,res):
        if root is None:
            return res
        res.append(root.val)
        self.preorderTraversal2(root.left,res)
        self.preorderTraversal2(root.right,res)
        return res


if __name__ == '__main__':
    a = TreeNode(1)
    a.left = None
    a.right = TreeNode(2)
    a.right.left=TreeNode(3)
    solution=Solution()
    print(solution.preorderTraversal(a))



