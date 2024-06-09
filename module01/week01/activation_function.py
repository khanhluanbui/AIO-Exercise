# Exercise 2:
import math


def is_number(x):
    try:
        float(x)

    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x) # hàm max(), Hàm này trả về giá trị lớn hơn giữa 0 và x, x>= 0 trả về x, x<0 trả về 0

def elu(x, alpha=0.01):
    if x <= 0 :
        return alpha * (math.exp(x) - 1)
    else:
        return x


def exercise2 ():
  x = input('Input x: ')
  activation_function = input('Input activation Function ( sigmoid | relu |elu ): ')

  # Check if x is a number
  if not is_number(x):
      print('x must be a number')
  else:
      # Check if activation function is valid
      if activation_function not in ['sigmoid', 'relu', 'elu']:
          print(f"{activation_function} is not supported")
      else:
          # Convert x to float
          x = float(x)

          # Calculate the result based on the activation function
          if activation_function == 'sigmoid':
              result = sigmoid(x)
          elif activation_function == 'relu':
              result = relu(x)
          elif activation_function == 'elu':
              result = elu(x, alpha=0.01)

  # Print the result
  print(f"{activation_function}: f({x})={result}")

exercise2()