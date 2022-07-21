class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num_string=int("".join(str(x) for x in num))
        total=num_string+k
        total=str(total)
        
        final= [x for x in total]
        
        return final
