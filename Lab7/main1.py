import util

scores = [100, 50, 75, 80]
extra_credit = [0, 50, 25, 20]

def main(scores, *args, **kwargs):
  augmented_scores = scores[:]
  print(args)
      
  for i,extra_credit in enumerate(args):
    augmented_scores[i] += extra_credit
  median = util.findMedian(augmented_scores)
  for key in kwargs:
    if key == "sum" and kwargs[key] is not None:
      print("The sum is: {}".format(sum(augmented_scores)))
    elif key == "count" and kwargs[key] is not None:
      print("The count is: {}".format(len(augmented_scores)))
  print('The median score is: {}'.format(median))

# Case 1, you're calling this file directily
# Then __name__ == "__main__"
# Case 2, you're not calling this file directly
# Then __name__ == the name of the module

print("main.py says: {}".format(__name__))

if __name__ == "__main__":
  main(scores, count=True, sum=None)