class Solution:
    
    def sameTree(self, p, q):

        # if p and q are empty, we return true
        if not p and not q:
            return True
        # if values differ return false 
        if not p or not q or p.val != q.val:
            return False
        # check both sides for sames
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # if not subRoot -> true
        if not subRoot:
            return True
        if not root:
            return False
        # counts as subtree
        if self.sameTree(root, subRoot):
            return True
        
        # else
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)