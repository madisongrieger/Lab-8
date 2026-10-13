from rational_def import numerator, denominator, rational

def print_rational(x):
  """
  rational number -> num and den
  takes in a rational number and prints the number in readable notation

  >>> print_rational(rational(3,4))
  3/4
  >>> print_rational(rational (5/10))
  5/10
  """
  num= numerator(x)
  den= denominator(x)
  print (str(num) + "/" + str(den))
  
