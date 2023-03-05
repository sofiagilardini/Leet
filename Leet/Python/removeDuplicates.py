class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        lpointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[lpointer] = nums[i]
                lpointer += 1
        
        return lpointer






