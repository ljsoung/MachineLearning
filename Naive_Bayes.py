# 나이브 베이즈 알고리즘
# 조건부 확률 -> A가 일어나면 B가 일어날 확률(A가 일어나야 함)


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/spam.csv'
data = pd.read_csv(file_url)

print(data.head())