# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # helper function for checking if same tree   
    def sameTree(self, p, q):
        # if not p and q return True
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        # check both sides for sameTree
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if no subRoot that means we already have a subtree in root
        if not subRoot:
            return True
        # if theres no root there cant be a subtree
        if not root:
            return False
        
        # if root and subroot are same tree then there is a subtree
        if self.sameTree(root, subRoot):
            return True
        
        # else if none of those then check for subtree finding for either side left or right. check left/right sides against subRoot tree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


    
    

        
        