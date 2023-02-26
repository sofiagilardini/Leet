class Solution:

    nums = [2, 7, 11, 15]
    target = 9

    def twoSum(self, nums, target): 

        ComplementMap = dict()

        for i in range(len(nums)):
            num = nums[i] # i = 1, num = 7
            complement = target - num # complement = 2

            if num in ComplementMap:
                return [i, ComplementMap[num]]
            else:
                ComplementMap[complement] = i # {7, 0}






