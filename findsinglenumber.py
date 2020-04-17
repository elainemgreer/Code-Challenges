def single_number(nums):
        
    counts = {}

    for num in nums:
        if num not in counts:
          counts[num] = 1
        else:
          counts[num] += 1

    for key, value in counts.items():
        if value < 2:
            return key