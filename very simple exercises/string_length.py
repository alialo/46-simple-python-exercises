"""Define a function that computes the length of a given list or string. 
(It is true that Python has the len() function built in, but writing it 
  yourself is nevertheless a good exercise.)"""

def string_length(x):
  count = 0
  for i in x:
    count += 1
  return count

result = string_length("this-length-isn't-19")
print result
