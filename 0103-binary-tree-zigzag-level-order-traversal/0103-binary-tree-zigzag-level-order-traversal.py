# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def bfs(node):
            res = []
            count = 0
            queue = deque()
            queue.append(node)
            while queue:
                curr_level = []
                element = len(queue)
                for _ in range(element):
                    e = queue.popleft()
                    curr_level.append(e.val)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)
                if count % 2 != 0:
                    curr_level.reverse()

                res.append(curr_level)
                count +=1
            return res
        return bfs(root)

                    



        