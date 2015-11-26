"""Define a function max() that takes two numbers as arguments and returns
 the largest of them. Use the if-then-else construct available in Python. 
 (It is true that Python has the max() function built in, but writing it
  yourself is nevertheless a good exercise.)"""

def max(one,two):
  if one > two:
    print "%d is greater than %d." % (one,two)
    return one
  elif one < two:
    print "%d is greater than %d." % (two,one)
    return two
  else:
    print "Your numbers are the same."

max(100,99)
