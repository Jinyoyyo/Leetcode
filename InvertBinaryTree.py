# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #return self.invertTreeWithoutRecursive(root)
        self.solve(root)
        return root
    
    def swap(self, a, b):
        return (b,a)
    
    def solve(self, node):
        if node == None:
            return
        self.solve(node.left)
        self.solve(node.right)
        node.left, node.right = self.swap(node.left, node.right)
    
    def invertTreeWithoutRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            node.left, node.right = self.swap(node.left, node.right)
        return root
        #4y, 48 ms, beats 61.30% of pythonsubmissions.

    def invertTreeWithoutRecursive(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            stack.append(node.left)
            stack.append(node.right)
            node.left, node.right = self.swap(node.left, node.right)
        return root
        #1y, 48 ms, beats 61.30% of pythonsubmissions.
