class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_1=0
        count_2=0
        n=len(nums1)
        m=len(nums2)
        for i in range(n):
            for j in range(m):
                if nums1[i]==nums2[j]:
                    count_1+=1
                    break

        for j in range(m):
            for i in range(n):
                if nums2[j] == nums1[i]:
                    count_2+=1
                    break

        return(count_1,count_2)


        