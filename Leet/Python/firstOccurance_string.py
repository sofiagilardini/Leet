class Solution: 
    def strStr(self, haystack: str, needle: str) -> int: 

        h_len = len(haystack)
        n_len = len(needle)

        if h_len < n_len:
            return -1
        
        for i in range(h_len - n_len + 1):
            if haystack[i:i+n_len] == needle:
                return i
        else: 
            return -1
        
sol = Solution()

print(sol.strStr("graciasdenada", "denada"))
        

# technically correct but very inefficient 

# class Solution: 
#     def strStr(self, haystack: str, needle: str) -> int: 

#         flag = False

#         for i in range(len(haystack)):
#             if haystack[i] == needle[0]:
#                 k = i
                
#                 while k + len(needle) < len(haystack):
#                     for j in range(len(needle)):
#                         if haystack[k+j] == needle[j]:
#                             flag = True
#                         else: 
#                             flag = False
        
#         if flag: 
#             return k 
#         else: 
#             return -1
    



