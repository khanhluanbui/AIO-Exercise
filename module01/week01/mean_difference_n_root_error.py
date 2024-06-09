# exercise 5:
def md_nre_single_sample (y, y_hat, n, p):
  return ((y**(1/n))-(y_hat**(1/n)))**p

print(md_nre_single_sample(100, 99.5, 2, 1))