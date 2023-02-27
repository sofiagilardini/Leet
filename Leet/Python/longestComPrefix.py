# class Solution: 

#     def longestCommonPrefix(self, strs: List[str]) -> str: 

#         for i in List:



myList = ["Sofia", "Sof"]
print("length of myList is", len(myList))


#for k in range(len(myList)):

letters = []
common = True
commons = []

while common == True: 
    for j in range(4):
        for i in range(len(myList)):
            letters.append(myList[i][j])
            print("letters is", letters)


        for k in range(len(myList)-1):
            if (letters[k] == letters[k+1]):
                print("they're common and letters looks like", letters)
                #commons.append(letters[k])

            else: 
                common = False



# firstletter1 = myList[0][0]
# firstletter2 = myList[1][0]

# secondletter1 = myList[0][2]
# secondletter2 = myList[1][2]

# letters.append(firstletter1)
# letters.append(firstletter2)

# if (letters[0] == letters[1]):
#     print("the common letters are", letters)


    # print(myList[j])
    # print("length of", j, "is", len(myList[j]))

    #make a new list with all the letter

    # for j in range(len(myList[k])):
    #     letter = myList[k][j]
    #     letters.append(letter)
    #     print("letter is", letter)
    #     print("letters list is", letters)



