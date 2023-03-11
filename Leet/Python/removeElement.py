from typing import List

class Solution: 
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0 # counter for elements to keep (elements != val)

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        for i in range(len(nums)-1, k, -1):
            nums[i] = "_"
    
        return k


testlist = [0, 0, 4, 5, 6, 0, 7, 8]
val1 = 0

sol = Solution()
sol.removeElement(testlist, val1)
print("updated list is ", testlist)