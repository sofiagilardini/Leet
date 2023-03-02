# class Solution: 

#     def longestCommonPrefix(self, strs: List[str]) -> str: 

#         for i in List:

myList = ["ABCDEF", "ABCDEFG", "ABCDEFGH"]

shortestitem = myList[0]
minlen = len(myList[0])

#finding which word has the shortest length to iterate over

for i in range(len(myList)):
    length_i = len(myList[i])

    if (length_i < minlen):
        minlen = length_i
        shortestitem = myList[i]


letters = []

# taking the i th letter of each word and comparing to see if they are equal. If equal, add to array of common letters

for j in range(len(shortestitem)):
    
    for i in range(len(myList)):

        firstletter = myList[i][j]
        letter = myList[0][j]

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




