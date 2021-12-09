class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in nums:
            index_of_item=nums.index(item)
            if index_of_item==0:
                for index in range(index_of_item+1,len(nums)):
                    if item+nums[index_of_item+index]==target:
                        output=[index_of_item,index]
                        return output
            else:
                # index_of_item=nums.index(item)
                for index in range(index_of_item+1,len(nums)):
                    if item+nums[index]==target:
                        output=[index_of_item,index]
                        return output
                        
                        


# 0--1,2,3,4 true ---- 1,2,3,4
# 1--2,3,4, true --- 2,3,4 ------(numbs[2])
# 2--3,4 true --3,4
# 3--4 true --4
# 4--
#  range(index+1,len(arr))

# 0 --- 1,2,3...
# 1--- 2,3,4...
# 2---3,4,5.....
                
        