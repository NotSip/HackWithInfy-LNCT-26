# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        def bfs(node):
            res = []
            final_res=[]
            queue = deque()
            queue.append(node)
            while queue:
                ele = len(queue)
                current_level=[]
                for _ in range(ele):
                    e = queue.popleft()
                    current_level.append(e.val)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)
                res.append(current_level)
            for i in res:
                final_res.append(i[-1])
            return final_res
        return bfs(root)

        

            
            
            


        