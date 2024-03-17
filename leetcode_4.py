class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        if (len(res))%2==0:
            return (res[(len(res)//2)-1] + res[len(res)//2])/2
        else:
            return res[len(res)//2]