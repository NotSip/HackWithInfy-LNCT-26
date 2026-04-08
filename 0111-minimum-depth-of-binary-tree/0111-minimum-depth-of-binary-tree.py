# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node == None:
                return 0
            if node.left and node.right:
                left_depth = dfs(node.left)
                right_depth = dfs(node.right)
                return 1 + min(left_depth,right_depth)
            else:
                if node.left:
                    left_depth = dfs(node.left)
                    return 1 + left_depth
                elif node.right:
                    right_depth = dfs(node.right)
                    return 1 + right_depth
                else:
                    return 1

        return dfs(root)
        