
def sec(ornum,df,Vars,feature,feature1,feature2,feature3,feature4,feature5,feature6):
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
def sec1(flag,ornum,df,Vars,feature,feature1,feature2,feature3,feature4,feature5,feature6):
    flag.clear()
    for i in range(499,len(df)-1):
      if(df[feature2+'c'][i]>Vars[2] or df[feature4+'c'][i]>Vars[4]):
        if(df[feature+'c'][i]>Vars[0] or df[feature1+'c'][i]>Vars[1] or df[feature5+'c'][i]>Vars[5]):
            flag.append(i)

        else :
            if(df[feature6+'c'][i]<=Vars[6]):
               if(df[feature3+'c'][i]>=Vars[3]):
                  flag.append(i)

    tot=0
    ptot=0
    for i in range(len(flag)):
           tot=abs(ornum[0]-flag[i])+tot
           ptot=ptot+1
    x=10000000
    if(ptot!=0):
      x=tot/ptot

    print(x,ptot)
    return x
def sec2(flag,ornum,df,Vars,feature,feature1,feature2,feature3,feature4,feature5,feature6):

    flag.clear()
    for i in range(499,len(df)-1):
      if(df[feature2+'c'][i]>Vars[2] or df[feature4+'c'][i]>Vars[4]):
        if(df[feature+'c'][i]>Vars[0] or df[feature1+'c'][i]>Vars[1] or df[feature5+'c'][i]>Vars[5]):
            flag.append(i)

        else :
            if(df[feature6+'c'][i]<=Vars[6]):
               if(df[feature3+'c'][i]>=Vars[3]):
                  flag.append(i)

    x=1000000
    for i in range(len(flag)):
           if(x<abs(ornum[0]-flag[i])):
               x=abs(ornum[0]-flag[i])

    print(x)
    return x
def sec3(flag,ornum,df,Vars,feature,feature1,feature2,feature3,feature4,feature5,feature6):
    flag.clear()
    for i in range(499,len(df)-1):
      if(df[feature2+'c'][i]>Vars[2] or df[feature4+'c'][i]>Vars[4]):
        if(df[feature+'c'][i]>Vars[0] or df[feature1+'c'][i]>Vars[1] or df[feature5+'c'][i]>Vars[5]):
            flag.append(i)

        else :
            if(df[feature6+'c'][i]<=Vars[6]):
               if(df[feature3+'c'][i]>=Vars[3]):
                  flag.append(i)

    x=0
    for i in range(len(flag)):
           if(abs(ornum[0]-flag[i])<=500):
               x=1000+x
               break
           for j in range(len(ornum)):
               if(flag[i]==ornum[j]):
                   x=100+x
                   break
           if(j==len(ornum)):
              x=x-100

    print(x,len(flag),len(df))
    return x