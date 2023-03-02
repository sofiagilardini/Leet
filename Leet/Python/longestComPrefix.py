class Solution: 

    def longestCommonPrefix(self, strs: List[str]) -> str: 

        shortestitem = strs[0]
        minlen = len(strs[0])

        #finding which word has the shortest length to iterate over

        for i in range(len(strs)):
            length_i = len(strs[i])

            if (length_i < minlen):
                minlen = length_i
                shortestitem = strs[i]


        letters = []

        # taking the i th letter of each word and comparing to see if they are equal. If equal, add to array of common letters

        for j in range(len(shortestitem)):
            
            for i in range(len(strs)):

                firstletter = strs[i][j]
                letter = strs[0][j]

                if (firstletter == letter):
                    common = True
                
                else: 
                    common = False

            if (common == True):
                letters.append(letter)

        print(f"Common prefix is is {letters}")

        commonstring = ""

        for i in range(len(letters)):
            commonstring += letters[i]

        print(f"Common prefix is is {commonstring}")

        return commonstring


