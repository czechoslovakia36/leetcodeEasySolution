class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        be_string=str(x)
        # print(be_string)
        # print(type(be_string))
        # print(be_string[::-1])
        # print(be_string)
        
        if (be_string == be_string[::-1]):
            return True
        else:
            return False
        
        