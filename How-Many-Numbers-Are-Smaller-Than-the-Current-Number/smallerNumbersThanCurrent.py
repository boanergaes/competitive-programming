class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        srtd = sorted(nums)
        idx = {}
        for i in range(len(srtd)):
            if srtd[i] not in idx:
                idx[srtd[i]] = i
                
        return [idx[num] for num in nums]