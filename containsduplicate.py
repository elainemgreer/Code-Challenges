class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        if len(nums) > 1:
            num_set = set(nums)
            
            if sorted(nums) == sorted(list(num_set)):
                return False
            return True
        return False
        