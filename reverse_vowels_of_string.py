class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # s=s.lower()
        
        vowels=['a','e','i','o','u',"A","E","I","O","U"]
        
        filler=""
        
        list_word=[word for word in s]
        
        for item in list_word:
            if item in vowels:
                filler+=item
        filler=filler[::-1]
        print(filler)
#         Convert string to list
        s=list(s)
        
        index_count=0
        
        for index in range(len(s)):
            if s[index]  in vowels:
                s[index]=filler[index_count]
                index_count=index_count+1
                
        # print(s)
        
        
        return "".join(s)
        
