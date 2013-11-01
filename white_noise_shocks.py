#! /usr/bin/env python

from function_generator import *

if __name__ == "__main__":
  num_ma_steps = int(sys.argv[1])
  mean = float(sys.argv[2])
  num_back = int(sys.argv[3])
  shock_scale = float(sys.argv[4])
  coefficients = get_coeff(num_back)
  step_counter = 0
  while (True):
    ma_x, ma_y = moving_average(num_ma_steps, mean, num_back,coefficients)
    ma_x, ma_y = white_noise_shock(ma_x, ma_y, shock_scale)
    ma_x = numpy.array(ma_x)
    ma_x += step_counter*num_ma_steps
    for i in range(len(ma_x)):
      print ma_x[i], ma_y[i]
    step_counter += 1
