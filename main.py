import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree

df = pd.read_csv('Train_v2.csv')

data = pd.get_dummies(df.drop('bank_account', axis=1))
print(data)