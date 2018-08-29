# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.postorderTraversal2(root,[])

    def postorderTraversal2(self,root,res):
        if root is None:
            return res
        self.postorderTraversal2(root.left, res)
        self.postorderTraversal2(root.right, res)
        res.append(root.val)
        return res

if __name__ == '__main__':
    a = TreeNode(1)
    a.left = None
    a.right = TreeNode(2)
    a.right.left = TreeNode(3)
    solution = Solution()
    print(solution.postorderTraversal(a))
