'''https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python'''


def hamming(a,b):
  return sum(ch1 != ch2 for ch1, ch2 in zip(a, b))
