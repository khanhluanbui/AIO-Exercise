# Excercise 1:
import math

def exercise1 ( tp, fp, fn):

  #Kiểm tra dữ liệu có phai int không:
  if not isinstance(tp, int):
    print('tp must be int')
    return
  if not isinstance(fp, int):
    print('fp must be int')
    return
  if not isinstance(fn, int):
    print('fn must be int')
    return

  #Kiểm tra tất cả giá trị có lớn hơn 0
  if tp <= 0 or fp <= 0 or fn <= 0:
    print('tp and fp and fn must be greater than zero')
    return

  precision = tp / (tp + fp)
  recall = tp / (tp + fn)
  f1_score = 2 * (precision * recall) / (precision + recall)

  print (f'precision is {precision}')
  print (f'recall is {recall}')
  print (f'f1_score is {f1_score}')

exercise1(2, 3, 4)