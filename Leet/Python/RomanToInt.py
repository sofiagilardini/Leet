class Solution: 
    def romanToInt(self, s:str) -> int:

        counter = 0

        roman = {"I": 1, "V" : 5, "X": 10, "L": 50, "C" : 100, "D" : 500, "M": 1000}

        for i in range(len(s)):

            if i + 1 < len(s) and roman[s[i+1]] > roman[s[i]]:
                counter -= roman[s[i]]

            else: 
                counter += roman[s[i]]
                print("counter is", counter)
    
        return counter


# if __name__ == "__main__":
#     sol = Solution()
#     sol.RomanToInt("IIII")