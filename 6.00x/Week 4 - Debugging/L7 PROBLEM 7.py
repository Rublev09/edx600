def rem(x, a):
   """
   x: an integer argument
   a: an integer argument

   returns: integer, the remainder when x is divided by a.
   """
   print(x,a)
   if x == a:
      return 0
   elif x < a:
      return x
   else:
      return rem(x-a, a)
