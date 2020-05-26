class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create list to store indices
        # var to store previous number
        
        print(nums)
        indices = []
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    indices.append(i)
                    indices.append(j)
        
        return indices





        