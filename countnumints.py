# count number of integers where int is x and x+1 is also present in array



def count_nums(nums):

  count = 0

  for num in nums:
    if num + 1 in nums:
      print(num)
      count += 1
  
  return


