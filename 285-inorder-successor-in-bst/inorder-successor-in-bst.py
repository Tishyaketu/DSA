# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inOrder(self,node: TreeNode, arr: List[TreeNode]) -> List[TreeNode]:
      if node.left==None and node.right==None:
        arr.append(node)
        return arr
      if node.left is not None:
        arr = self.inOrder(node.left,arr)
      arr.append(node)
      if node.right is not None:
        arr = self.inOrder(node.right,arr)
      return arr
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        inOrderArray = self.inOrder(root,[])
        for i in range(len(inOrderArray)):
          if inOrderArray[i] == p and i!=len(inOrderArray)-1: return inOrderArray[i+1]
        return None