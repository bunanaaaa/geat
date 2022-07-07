import numpy as np
from sklearn import linear_model
import pandas as pd

# 计算斜率


def calculate_slope(data):
    reg = linear_model.LinearRegression()
    reg.fit(np.array(range(len(data))).reshape(-1, 1), np.array(data).reshape(-1, 1))
    slope = reg.coef_ # 斜率
    intercept = reg.intercept_ # 截距
    slope = slope[0][0]
    intercept = intercept[0]
    return slope

def form_slope(data,step,feature,feature1,feature2,feature3,feature4,feature5,feature6):
    df = pd.DataFrame(data['DateTime'], columns=['DateTime'])
    df['Time'] = data['Time']
    df[feature] = 0
    df[feature1] = 0
    df[feature4] = 0
    df[feature2] = 0
    df[feature3] = 0
    df[feature5] = 0
    df[feature6] = 0
    for i in range(0, len(data)-step+1,1):
        df[feature][i+step-1]=abs(calculate_slope(data[feature][i:i+step-1]))
    for i in range(0, len(data)-step+1, 1):
        df[feature1][i+step-1] = abs(calculate_slope(data[feature1][i:i+step-1]))
    for i in range(0, len(data)-step+1,1):
        df[feature2][i+step-1]=abs(calculate_slope(data[feature2][i:i+step-1]))
    for i in range(0, len(data)-step+1, 1):
        df[feature3][i+step-1] = abs(calculate_slope(data[feature3][i:i+step-1]))
    for i in range(0, len(data)-step+1,1):
        df[feature4][i+step-1]=abs(calculate_slope(data[feature4][i:i+step-1]))
    for i in range(0, len(data)-step+1, 1):
        df[feature5][i+step-1] = abs(calculate_slope(data[feature5][i:i+step-1]))
    for i in range(0, len(data)-step+1,1):
        df[feature6][i+step-1]=abs(calculate_slope(data[feature6][i:i+step-1]))
    df['actual']=data['溢流']
    return df


