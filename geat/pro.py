import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def getDataWithFeature(data,feature):
    df = pd.DataFrame(data['DateTime'], columns=['DateTime'])
    df['Time'] = data['Time']
    scaler = MinMaxScaler()
    index=0
    for i in range(2,data.shape[1]-3):
        if(index>= len(feature)):
            break;
        if(feature[index]==list(data)[i]):
            result = scaler.fit_transform(np.array(data[list(data)[i]]).reshape(-1,1))
            df[list(data)[i]]=pd.to_numeric(result.reshape(-1))
            index+=1
    df['actual']=pd.to_numeric(data['溢流'])
    df['pred']=pd.to_numeric(data['pred'])
    return df;


def getTimeMean(df,feature,step):
    column = ['startDate', 'startTime', 'endDate', 'endTime', 'actual', 'pred']
    column[4:4] = feature
    result = pd.DataFrame(columns=column)
    index=0
    for i in range(step,df.shape[0],step):
        res=[]
        startDate=df['DateTime'][i-step]
        startTime = df['Time'][i - step]
        endDate = df['DateTime'][i-1]
        endTime = df['Time'][i-1]
        res.append(startDate)
        res.append(startTime)
        res.append(endDate)
        res.append(endTime)
        pred=1
        actual=1
        for j in range(i-step,i):
            if(df['actual'][j]==2):
                actual = 2
                break;


        #均值
        for j in range(len(feature)):
            res.append(np.mean(df[feature[j]][i-step:i]))
        res.append(actual)
        res.append(pred)
        result.loc[len(result.index)] = res
        if(i+step>df.shape[0]):
            res=[]
            startDate = df['DateTime'][i]
            startTime = df['Time'][i]
            endDate = df['DateTime'][df.shape[0]-1]
            endTime = df['Time'][df.shape[0] - 1]
            res.append(startDate)
            res.append(startTime)
            res.append(endDate)
            res.append(endTime)
            pred = 1
            actual = 1
            for j in range(i, df.shape[0]):
                if (df['actual'][j] == 2):
                    actual = 2
                    break;

            #均值
            for j in range(len(feature)):
                res.append(np.mean(df[feature[j]][i :df.shape[0]]))

            res.append(actual)
            res.append(pred)
            result.loc[len(result.index)] = res

    return result

