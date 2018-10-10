 def coollist(*args, **kwargs):
...   empty = {}
...   for index, value in enumerate(args):
...     empty[index] = value
...   for key, value in kwargs.items():
...     empty[key] = value
...   return empty