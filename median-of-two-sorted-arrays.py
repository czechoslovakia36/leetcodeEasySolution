class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged_sorted=sorted(merged)
        mid=len(merged_sorted)/2
        
        if len(merged_sorted)%2==0:
            add=merged_sorted[int(mid)]+merged_sorted[int(mid)-1]
            return add/2
        else:
            return merged_sorted[int(mid)]
        
        
        
