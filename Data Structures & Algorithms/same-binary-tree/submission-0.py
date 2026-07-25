# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True

        if not p or not q or p.val != q.val:
            return False
        
        res_l = self.isSameTree(p.left, q.left)
        res_r = self.isSameTree(p.right, q.right)

        return (res_l and res_r)
