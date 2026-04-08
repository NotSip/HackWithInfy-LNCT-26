# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def bfs(node):
            res = []
            queue = deque()
            queue.append(node)
            while queue:
                ele = len(queue)
                curr_level = []
                for _ in range(ele):
                    e = queue.popleft()
                    curr_level.append(e)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)
                res.append(curr_level)
            return len(res)
        return bfs(root)
        