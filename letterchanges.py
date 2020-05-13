def LetterChanges(str):

  alpha = list('abcdefghijklmnopqrstuvwxyz')
  new_string = ""

  for char in str:
    if char.isalpha():
      for i, letter in enumerate(alpha):
        if letter == char:
          new_string += alpha[i + 1]

    else:
      new_string += char

  cap_string = ""

  for letter in new_string:
    if letter in "aeiouAEIOU":
      letter = letter.upper()
      cap_string += letter
    else:
      cap_string += letter

  return cap_string