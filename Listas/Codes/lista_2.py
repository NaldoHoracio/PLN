# -*- coding: utf-8 -*-
"""
PLN: Lista 2

@author: edvonaldo
"""


import os
import csv
import math
import random
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

# PREPRANDO OS DADOS

path = 'C:/Users/edvon/Desktop/bbc-text.csv'

data_base = pd.read_csv(path)

#print(data_base.readlines())