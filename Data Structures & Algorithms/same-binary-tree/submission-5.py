# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both null
        if not p and not q:
            return True
        # check each value in both p and q and if they differ return false
        if not p or not q or p.val != q.val:
            return False
            
        
        
        

        # check left and right side of tree for samesies recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        