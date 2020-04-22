## not in place
def move_zeroes(nums):

  new_list = []
  zero_list = []

  for i, num in enumerate(nums):
    if num != 0:
      new_list.append(num)
    else:
      zero_list.append(num)
  
  new_list.extend(zero_list)




## in place
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    i = 0
    for j in range(len(nums)):

        if nums[j] != 0:
  
            nums[i], nums[j]= nums[j], nums[i]
            i += 1