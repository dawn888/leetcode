# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorderTraversal2(root,[])

    def inorderTraversal2(self,root,res):
        if root is None:
            return res
        self.inorderTraversal2(root.left,res)
        res.append(root.val)
        self.inorderTraversal2(root.right,res)
        return res



if __name__ == '__main__':
    a = TreeNode(1)
    a.left = None
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)
    solution = Solution()
    print(solution.inorderTraversal(a))