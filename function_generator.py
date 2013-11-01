#! /usr/bin/env python

import numpy
import scipy.stats as stats

import math
import sys
import random

def white_noise_shock(ma_x, ma_y, shock_scale):
  #choose a number of random white noise shocks to add to the series
  shock_count = random.choice(range(len(ma_x)/100))
  for i in range(shock_count):
    #for each shock, choose a starting point
	shock_start = random.choice(ma_x)
	#for that start, choose the shock duration (100 obs or less)
	shock_length = random.choice(range(100))
        shock_length = len(ma_y[shock_start:shock_start+shock_length])
	#generate the shock
	shock = stats.norm.rvs(shock_scale, size=shock_length, scale=shock_scale/2)
	ma_y[shock_start:shock_start+shock_length] += shock
  return ma_x, ma_y
 
def get_coeff(num_backward):
  coefficients = numpy.array(random.sample(range(num_backward*10), num_backward))+1
  return coefficients

def multivariate(x_size, low, high, observations):
  #builds a set with one pairwise interaction and one curvature
  coeff = get_coeff(x_size)
  #choose an interaction pair
  interaction_indeces = None
  interaction_coefficient = random.randrange(-10,10)
  mu = (high+low)/2.0 #naive middle of distribution
  sigma = (high-low)/4.0 #fakey sd
  
  if x_size > 1:
    int_index_one = random.choice(range(x_size))
    int_index_two = random.choice(range(x_size))
    while int_index_one == int_index_two:
      int_index_two = random.choice(range(x_size))
    interaction_indeces = (int_index_one, int_index_two)

  #choose curvature
  curvature_index = random.choice(range(x_size))
  curvature_coefficient = random.randrange(-10,10)
  X = []
  y = []
  for i in range(observations):
    x_i = numpy.array([random.normalvariate(mu,sigma) for i in range(x_size)])
    y_i = sum(x_i * coefficients)
	
    if interaction_indeces:
      y_i += interaction_coefficient * x_i[interaction_indeces[0]] * x_i[interaction_indeces[1]]
      y_i += curvature_coefficient*x_i[curvature_index]**2
      X.append(x_i)
      y.append(y_i)
  return X, y
    
	  
	  
  
def moving_average(steps, mean, num_backward, coefficients):
  x = range(steps)
  y_base = stats.norm.rvs(size=steps)
  y = range(steps)
  for i in range(len(x)):
    
    values = []
    if i < num_backward:
      # sample backward
      for j in range(num_backward):
        
        if (i-j) >= 0:
		  
		  values.append(y_base[i-j])
        else:
          values.append(0)
	  
    else:
      for j in range(num_backward):
        values.append(y_base[i-j])
    y_sample = numpy.array(values)      
    
    y[i] = mean + sum(y_sample * coefficients)
  return x, y

def fill_y(step):
  x = range(-100,100)
  y = range(200)
  for i in range(len(x)):
    y[i] = (0.001*i*step)**2 + 1

  y2 = map(lambda x: x + stats.norm.rvs(scale=0.3), y)
  y3 = map(lambda x: x + math.sin(x) + 1, y2)
  return range(200)*step,y3
  
  
if __name__ == "__main__":
# make a MA function with a sinusoidal seasonal component
  dataset_x = []
  dataset_y = []
  for i in range(5):
    x, y = fill_y(i)
    dataset_x += x
    dataset_y += y
  

  dataset = open("wave.dat", "w")
  for i in range(len(dataset_y)):
    print >> dataset, i, dataset_y[i]
  dataset.close()

  #make a moving average around a mean
  num_ma_steps = int(sys.argv[1])
  mean = float(sys.argv[2])
  num_back = int(sys.argv[3])
  shock_scale = float(sys.argv[4])
  coefficients = get_coeff(num_back)
  ma_x, ma_y = moving_average(num_ma_steps, mean, num_back,coefficients)
  dataset = open("moving_average.dat", "w")
  for i in range(len(ma_x)):
    print >> dataset, ma_x[i], ma_y[i]
  dataset.close()

  ma_x, ma_y = white_noise_shock(ma_x, ma_y, shock_scale)
  dataset = open("white_noise_shocks.dat", "w")
  for i in range(len(ma_x)):
    print >> dataset, ma_x[i], ma_y[i]
  dataset.close()
  
  X, y = multivariate(3,-25,25,500)
  dataset = open("multivariate.dat", "w")
  for i in range(len(X)):
    print >> dataset, y[i], " ".join(map(str,X[i]))
  dataset.close()

  
