class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        res=[]
        for i in range(0,m):
            res.append(nums1[i])
        for j in range(0,n):
            res.append(nums2[j])

        res.sort()

        nums1.clear()
        nums1.extend(res)
        
        