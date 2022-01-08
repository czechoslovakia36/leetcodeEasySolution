class Solution:
    def checkString(self, s: str) -> bool:
        s=s.lower()
        sA=s.find("a")
        sB=s.find("b")
        if sA>=0 and sB>=0:
            # print("ji")
            index_of_b= s.index("b")
            for i in range(index_of_b+1,len(s)):
                
                
                if s[i]=="a":
                    return False
                    break
                else:
                    continue
                # print("hi2")
                    
        else:
            return True
        
            
        if len(s)==1:
            return True
       
                        
        
        
        
        
        
        
        if s[-1]=="b":
            return True
        
        
    