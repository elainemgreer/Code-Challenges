"""Does a string have balanced parentheses?

For example::

   >>> has_balanced_parens("()")
   True

   >>> has_balanced_parens("(Oh Noes!)(")
   False

   >>> has_balanced_parens("((There's a bonus open paren here.)")
   False

   >>> has_balanced_parens(")")
   False

   >>> has_balanced_parens("(")
   False

   >>> has_balanced_parens("(This has (too many closes.) ) )")
   False

If you receive a string with no parentheses, consider it balanced::

   >>> has_balanced_parens("Hey...there are no parens here!")
   True
"""


def has_balanced_parens(string):
    """Does a string have balanced parentheses?"""

    open_count = 0
    close_count = 0
    words = string.split(" ")
    letters = []
    

    for word in words:
      for char in word:
        letters.append(char)
   
    for char in letters:
      if char == "(":
       
        open_count += 1
     

      if char == ")":
        
        close_count += 1
    

    if open_count == close_count:
      return True
    else:
      return False


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")
