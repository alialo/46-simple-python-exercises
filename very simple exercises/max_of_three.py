"""Define a function max_of_three() that takes three numbers as arguments
   and returns the largest of them."""

def max_of_three(one,two,three):
  result = "%d is greater than %d and %d."
  if (one == two) and (one == three) and (two == three):
    print "All of your numbers are the same, please change them."
  elif (one == two) or (one == three) or (two == three):
    print "Two of your numbers are the same, please change them."
  elif (one > two) & (one > three):
    print result % (one,two,three)
    return one
  elif (two > one) & (two > three):
    print result % (two,one,three)
    return two
  elif (three > one) & (three > two):
    print result % (three,one,two)
    return three

max_of_three(1,8,50)
