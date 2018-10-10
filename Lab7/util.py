def findMedian(lst):
  """Takes a list, returns the median element of that list"""
  cpy = lst[:]
  cpy.sort()
  #return -1
  if len(cpy) % 2 == 0: # Is Even number
    # [1,2,3,4]
    return (cpy[(len(cpy) // 2) -1] + cpy[(len(cpy) // 2)]) / 2
  else:
    return cpy[len(cpy) // 2]

print("util.py says: {}".format(__name__))

COLOR = 'red'

if __name__ == "__main__":
  i = 0
  while i < 100000:
    actual = findMedian([1,2,3,4,5])
    expected = 3
    assert(actual == expected)
    i += 1
    print("i is: {}".format(i))
