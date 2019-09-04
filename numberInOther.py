# Write a function that takes two non-negative long integers, A & B, and returns the 0-based 
# position of where A “appears” in B.  Examples:
# • A: 53    B: 1953786     Answer: 2
# • A: 87    B: 49268794   Answer: 4
# • A: 26    B: 12345678   Answer: “26 does not appear in 12345678”
# Please do not use the simple approach of using the built-in string search function.
from math import log10, ceil

def numberInOther(a, b):
  sizeA = ceil(log10(a))
  sizeB = ceil(log10(b))
  
  print(sizeA, sizeB)

  if sizeB < sizeA:
    return "", a, "does not appear in", b
    
  M = pow(10, sizeA)

  testNumber = b % M
  
  print("TN: ", testNumber)
  
  if (testNumber - a) == 0:
    print("true")
    
  print("False")
  
tests = [
  {
    'a': 1953786,
    'b': 53
  },
  {
    'a': 53,
    'b': 1953786
  }
]

for t in tests:
  a = t['a']
  b = t['b']
  numberInOther(a, b)
  
  