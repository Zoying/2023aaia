class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[nums[0]]]
        repeat = 0
        N = len(nums)
        for i in range(1, N):
            if nums[i] == nums[i - 1]:
                repeat = repeat + 1
                if len(ans) <= repeat:
                    ans.append([])
            else:
                repeat = 0
            ans[repeat].append(nums[i])
        return ans