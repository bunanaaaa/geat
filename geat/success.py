
def sec(df,Vars,feature,feature1,feature2,feature3,feature4,feature5,feature6):
    tot=0 #存储的是预测正确的个数
    whtot=0 #存储的是真实情况下溢流的个数
    wrtot=0 #存储的是预测错误的个数
    for i in range(499,len(df)):
       if((df[feature][i]>=Vars[0] and df[feature1][i]>=Vars[1] and df[feature2][i]>=Vars[0] and df[feature3][i]>=Vars[1] and df[feature4][i]>=Vars[0] and df[feature5][i]>=Vars[1] and df[feature6][i]>=Vars[0]  )and df['actual'][i]==2):
         tot=tot+1
       if(df['actual'][i]==2):
         whtot=whtot+1
       if((df[feature][i]>=Vars[0] and df[feature1][i]>=Vars[1]and df[feature2][i]>=Vars[0] and df[feature3][i]>=Vars[1] and df[feature4][i]>=Vars[0] and df[feature5][i]>=Vars[1] and df[feature6][i]>=Vars[0] )and df['actual'][i]==1):
           wrtot=wrtot+1

    res=tot/(whtot+wrtot)
    return res