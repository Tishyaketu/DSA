# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
          if node is None:
            return False
          if is_symmetrical(node,subRoot):
            return True
          return dfs(node.left) or dfs(node.right)
        def is_symmetrical(node1,node2):
          if node1 is None or node2 is None: return node1 is None and node2 is None
          return (node1.val==node2.val) and is_symmetrical(node1.left,node2.left) and is_symmetrical(node1.right,node2.right)
        return dfs(root)