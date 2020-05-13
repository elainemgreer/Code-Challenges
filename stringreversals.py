def FirstReverse(str):

    #reverse string

  reverse_string = str[::-1]

  return reverse_string





def reverse_another_way(str):

  index = 0
  list_str = list(str) 
  new = ""

  while list_str:
    current = list_str.pop()
    new += current
    index += 1
  
  return new




def reverse_words(message):

  # must reverse in place so no new list
  # must separate out words
  # iterate through list and append letters to end until you reach space

  length = len(message)

  for i in range(length):
    letter = message.pop()
    message.append(letter)
    print(message)

