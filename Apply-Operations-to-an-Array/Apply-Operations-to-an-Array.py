class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        h = 0
        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            while h < i and nums[h]:
                h += 1
            if nums[i]:
                nums[i], nums[h] = nums[h], nums[i]
        return nums