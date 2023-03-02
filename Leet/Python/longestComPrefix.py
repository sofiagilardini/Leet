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

        #compare letters to those in the shortest word

        #iterating over how many letters there are
        for j in range(len(shortestitem)):
            common = True

            #iterating over number of words
            for i in range(len(strs)):

                if strs[i][j] != shortestitem[j]:
                    common = False
                    break

            if common:
                letters.append(shortestitem[j])
            
            else:
                break


        commonstring = ''.join(letters)

        return commonstring



