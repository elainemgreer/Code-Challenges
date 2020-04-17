def max_subarray(nums):

    sum_list = []
    current_max = nums[0]
    
    sum_list.append(current_max)
    
    if len(nums) == 1:
        for num in nums:
            return num

    for i in range(len(nums)):
        try:
            if current_max + nums[i+1] > nums[i+1]:
                current_max = current_max + nums[i+1]
            else:
                current_max = nums[i+1]
            sum_list.append(current_max)
        except:
            break
    
    return max(sum_list)
