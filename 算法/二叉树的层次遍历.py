# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#广度
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        q=[root]
        while len(q) != 0:
            new_q = []
            res.append([node.val for node in q])
            for node in q:
                if node.left:
                    print(node.left.val)
                    new_q.append(node.left)
                if node.right:
                    print(node.right.val)
                    new_q.append(node.right)
            q=new_q
        return res

#深度
class Solution1:
    def levelOrder(self, root):
        res=[]
        self.dfs(root,0,res)
        return res

    def dfs(self,root,depth,res):
        if root==None:
            return res
        if len(res)<depth+1:
            res.append([])

        res[depth].append(root.val)
        print(res, "depth:", depth, res[depth])
        self.dfs(root.left,depth+1,res)
        self.dfs(root.right,depth+1,res)

if __name__ == '__main__':
    a = TreeNode(3)
    a.left = TreeNode(9)
    a.right = TreeNode(20)
    a.right.left = TreeNode(15)
    a.right.right = TreeNode(7)
    solution = Solution1()
    print(solution.levelOrder(a))