#!/usr/bin/env python
# coding: utf-8

# In[1]:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

class LinearRegression:
    def __init__(self):
        self.a = None
        self.b = None

    def fit (self,x,y):
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        numerator = 0
        denominator = 0

        for i in range(len(x)):
            numerator += (x[i] - x_mean) * (y[i] - y_mean)
            denominator += (x[i] - x_mean)**2

        self.b = numerator / denominator
        self.a = y_mean - self.b*x_mean
        return self

    #making predictions from a and b obtained
    def predict(self,x):
        y_pred = self.a + self.b*x
        return y_pred


# In[ ]:
