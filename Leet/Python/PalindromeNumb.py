class Solution():
    
    def isPalindrome(self, x: int) -> bool:

        numstring = str(x)

        n = len(numstring)

        Palindrome = True

        for i in range(n):

            if (numstring[i] == numstring[n-1-i]):
                print("for now good")
            else: 
                Palindrome = False
        
        return Palindrome

        
    
if __name__ == "__main__":

    sol = Solution()
    sol.isPalindrome(121)