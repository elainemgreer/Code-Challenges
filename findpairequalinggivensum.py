def find_pair(lst, sum_nums):

  high = len(lst) -1
  # since we are indexing, we want to subtract one to account for starting at 0
  
  low = 0 # start at bottom of lisdt

  # this means there are still nums to check in list...if low becomes the same as high that means we have crossed
  while low < high:
    print(low, high)
    calc = lst[low] + lst[high]
    if calc == sum_nums:
      print(calc, sum_nums)
      return True
    if calc < sum_nums:
      low += 1
    if calc > sum_nums:
      high -= 1

  return False

print(find_pair([1, 2, 4, 4], 8))