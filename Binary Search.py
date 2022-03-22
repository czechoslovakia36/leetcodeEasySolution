class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for item in nums:
            if item==target:
                result= nums.index(item)
                return result
            
        return -1
                
        
        
