# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(node):
            res = []
            queue = deque()
            queue.append(node)

            while queue:
                elements = len(queue)
                current_level = []
                for _ in range(elements):
                    e = queue.popleft()
                    current_level.append(e.val)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)
                res.append(current_level)
            return res
        return  bfs(root)


            