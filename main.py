import geatpy as ea
import numpy as np
import pandas as pd
import success as suc
import trendline as td
import change as ch
import matplotlib.pyplot as plt


data=pd.read_csv('Rec1806252131.csv', encoding='utf-8')
step=500
feature='C1(%)'
feature1='C2(%)'
feature2='出口流量log(%)'
feature3='大钩位置(m)'
feature4='立压log(MPa)'
feature5='总烃(%)'
feature6='泵冲1(spm)'
df=td.form_slope(data,step,feature,feature1,feature2,feature3,feature4,feature5,feature6)
print(df)
ornum=ch.last(df)
print(ornum)
flag=[]
#构建问题

@ea.Problem.single
def evalVars(Vars):  # 定义目标函数（含约束）

    f1 = suc.sec3(flag,ornum, df, Vars, feature, feature1, feature2, feature3, feature4, feature5, feature6)  # 计算目标函数值
   # f2 = suc.sec2(flag,ornum, df, Vars, feature, feature1, feature2, feature3, feature4, feature5, feature6)
   # ObjV = np.hstack([f1, f2]),  # 计算目标函数值
    CV = 0  # 计算违反约束程度
    return f1, CV


problem = ea.Problem(name='soea quick start demo',
                        M=1,  # 目标维数
                        maxormins=[-1],  # 目标最小最大化标记列表，1：最小化该目标；-1：最大化该目标
                        Dim=7,  # 决策变量维数
                        varTypes=[0, 0, 0,0,0,0,0],  # 决策变量的类型列表，0：实数；1：整数
                        lb=[-1,-1,-1,-1,-1,-1,-1],  # 决策变量下界
                        ub=[1, 1,1,1,1,1,1],  # 决策变量上界
                        evalVars=evalVars)
# 构建算法
algorithm = ea.soea_SEGA_templet(problem,
                                    ea.Population(Encoding='RI', NIND=20),
                                    MAXGEN=500,  # 最大进化代数。
                                    logTras=1,  # 表示每隔多少代记录一次日志信息，0表示不记录。
                                    trappedValue=1e-6,  # 单目标优化陷入停滞的判断阈值。
                                    maxTrappedCount=100)  # 进化停滞计数器最大上限值。
# 求解
res = ea.optimize(algorithm, seed=1, verbose=True, drawing=1, outputMsg=True, drawLog=False, saveFlag=True, dirName='result')
print(res)

x1=flag
y1=[2]*len(flag)
y2=df['actual']
plt.plot(y2)
plt.scatter(x1,y1,color='r')
plt.xlabel('时间窗口') # 设置x轴标题
plt.ylabel('溢流标志')
plt.show()
f=open("C:/Users/User/Desktop/k1.txt","w")
f.write(str(flag))
f.close()