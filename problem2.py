from rational_def import numerator, denominator, rational

def div_rational(x,y):
  """
  divide both rational numbers
  >>> div_rational(rational(1,2),rational(3,4))
  rational (2,3)
  >>> div_rational (rational(2,3),rational(3,9)
  rational(2,1)
  """
  num= numerator(x) * denominator(y)
  den= denominator(x) * numerator(y)
  return (num,den)
