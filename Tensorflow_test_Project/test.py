from __future__ import absolute_import, division, print_function

import pathlib

import pandas as pd
import seaborn as sns
import numpy as np

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)



df = pd.DataFrame({'age': [5, 6, np.NaN],
                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
                             pd.Timestamp('1940-04-25')],
                    'name': ['Alfred', 'Batman', ''],
                    'toy': [None, 'Batmobile', 'Joker']})

print(50*'*')
print(df)

print(50*'*')
dfisna = df.isna()
print(dfisna)

print(50*'*')
dfisnasum = df.isna().sum()
print(dfisnasum)
