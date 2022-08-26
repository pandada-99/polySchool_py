# 220627 AI기초프로그래밍(신교수님)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd
# pandas ==> get_dummies() ==> Dataframe ==> np.array
import numpy as np

df = pd.read_csv("data/data-04-zoo.csv")
print(df.shape)

x_train = df.iloc[:, :16]
y_train = df.iloc[:, -1]
print(y_train)

