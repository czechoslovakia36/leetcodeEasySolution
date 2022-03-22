class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp=[]
        index=0
        count=0
        
        while index<len(nums):
            if nums[index]==0:
                nums.pop(index)
                index=index-1
                count+=1
                
                                
            index+=1
        print(nums)
        print(count)        
        while count>0:
            nums.append(0)
            count-=1
                
            
