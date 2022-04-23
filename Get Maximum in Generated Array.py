class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums=[]
#         filling array with random values

        for values in range(0,n+1):
            nums.append(values)
        print(nums)    
        
        
        for i in range (2,n+1):
          if i%2==0:
            nums[i]=nums[int(i/2)]
          else:
            value=i-int(i/2)
            nums[i]= nums[int(i/2)]+nums[value]               
            
                
        return max(nums)
        
      
