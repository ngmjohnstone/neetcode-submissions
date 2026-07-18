# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        new_tree = TreeNode(val=root.val)
        l = root.left
        r = root.right
        while l and r:
            new_tree.right = l
            new_tree.left = r
            l = root.left.left
            r = root.right.right

        return new_tree