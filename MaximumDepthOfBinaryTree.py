# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def dfs(self, node, depth):
        if node == None:
            return depth
        return max(self.dfs(node.left, depth), self.dfs(node.right, depth)) + 1
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)

#2y, 68ms, beats 69.42% of pythonsubmissions.