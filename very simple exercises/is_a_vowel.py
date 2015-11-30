"""Write a function that takes a character (i.e. a string of length 1) 
and returns True if it is a vowel, False otherwise."""

def is_a_vowel(x):
  vowel = ['a','e','i','o','u']
  result = ''
  for i in vowel:
    if x == i:
      result = True
      break
    else:
      result = False
  if result == True:
    print "%s is a vowel" % x
  else:
    print "%s is not a vowel" % x
  

is_a_vowel("y")
