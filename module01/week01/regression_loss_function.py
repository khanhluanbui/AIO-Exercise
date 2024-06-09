# exercise 3:
import math
import random

def calc_mae(predict, target):
    return abs(predict - target)

def calc_mse(predict, target):
    return (predict - target) ** 2

def exercise3():
    num_samples = input('Input number of samples (integer number) which are generated: ')
    if not num_samples.isnumeric():
        print("number of samples must be an integer number")
        return

    loss_name = input('Input loss name: ')

    final_loss = 0
    num_samples = int(num_samples)
    for i in range(num_samples):
        predict = random.uniform(0,10)
        target = random.uniform(0,10)

        if loss_name == 'MAE':
            loss = calc_mae(predict, target)
        elif loss_name == 'MSE' or loss_name == 'RMSE':
            loss = calc_mse(predict, target)
        else:
            print(f'{loss_name} is not supported')
            return

        final_loss += loss
        print(f'loss_name: {loss_name}, sample: {i}: pred: {predict} target: {target} loss: {loss}')

    final_loss /= num_samples
    if loss_name == 'RMSE':
        final_loss = math.sqrt(final_loss)
    print(f'final {loss_name}: {final_loss}')

exercise3()
