# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            
            node.left, node.right = node.right, node.left
        dfs(root)
        return root

------------------------------------------------------------
2nd :
------------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        dummy = root.right
        root.right = root.left
        root.left = dummy

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
