class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # iterate over nums by i in range
        # if target found, return index
        # if not, find where number goes...
        # if target is greater than previous and less than next
        prev_num = 0
        
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
                
        else:
            for i in range(len(nums)):
                if target > max(nums):
                    num_index = len(nums)
                    return num_index
                if target < min(nums):
                    return 0
                if target > prev_num and target < nums[i]:
                        num_index = i
                        return num_index
                prev_num = nums[i]
                    