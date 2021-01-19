# given 2 arrays
# return true or false
# if there are common elements in the 2 arrays

def in_common(lst1, lst2):

  #method one- loop over both lists, nested loop, and if elements are equal, return True

  for i in lst1:
    for j in lst2:
      if i == j:
        return True
  return False

print(in_common(["bird", "dog", "bear"], ["bat", "lizard", "cat", "fox"]))

## this is bad runtime- technically it is O(a*b) because lists are different, but basically the same as On^2...quadratic run Time

# another approach might be hash

def in_common(lst1, lst2):

  #method 2- use a dictionary. Add elements from one list to dict, check if 

  # 2 ways to make dict from lst
  # word_dict = dict.fromkeys(lst1, True)

  word_dict = {word: True for word in lst1}

  for word in lst2:
    if word in word_dict.keys():
      return word_dict[word]

print(in_common([2], [2, 3, 4]))

## this solution is O(a + b) which is much better than previous one...in terms of time complexity, this is a better solution for large inputs
