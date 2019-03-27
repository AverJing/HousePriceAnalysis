# -*- coding: utf-8 -*-
import numpy as np
import math


def level_check(data):
    # 原始数据级比校验
    n = len(data)
    grade_ratio = []
    for i in range(len(data)):
        if (i < n - 1):
            # grade_ratio[i] = history_data[i] / history_data[i+1]
            # 报错 list assignment index out of range 因为空数组不能指定下标
            grade_ratio.append(data[i] / data[i + 1])
            #print(grade_ratio[i])
    # 可容覆盖区间(low,high), 在此区间内方可进行灰色预测
    low = math.exp(-2 / (n + 1))
    high = math.exp(2 / (n + 1))
    for level in grade_ratio:
        if level>low and level<high:
            continue
        else:
            return False
    return True

# 数据平移变换处理
def data_handle(data,c):
    #print('平移处理',c)
    for i in range(len(data)):
        data[i] = data[i]+c
    if level_check(data):
        return #函数出口
    else:
        data_handle(data,c)

# 预测
def forecast(data,c):
    n = len(data)
    X0 = np.array(data) #创建一维数组，原始数据
    #累加生成
    data_agg = [sum(data[0:i+1]) for i in range(n)] #一次累加 1-AGO
    # range(3)->[0,1,2]; range(1,3)->[1,2]; range(0,15,5)->[0,5,10];range(0,-3,-1)-"[0,-1,-2]
    X1 = np.array(data_agg) # 一次累加生成的数列,一维

    #计算数据矩阵B和数据向量Y，
    B = np.zeros([n-1,2]) #array[[0,0],[0,0]....[0,0]] n-1个[0,0]
    Y = np.zeros([n-1,1]) #array[[0],[0],....[0]] n-1个[0]
    for i in range(0,n-1):
        B[i][0] = -0.5*(X1[i] + X1[i+1])
        B[i][1] = 1
        Y[i][0] = X0[i+1]

    #计算GM(1,1)微分方程的参数a和u
    #numpy.linalg.inv()求矩阵的逆 B.T是矩阵B的转置 a.dot(b)等同numpy.dot(a,b)求矩阵积，不可逆
    A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
    a = A[0][0]
    u = A[1][0]

    #建立灰色预测模型，计算出预测值列
    XX0 = np.zeros(n)
    #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    XX0[0] = X0[0] # X0[0]:724.57
    for i in range(1,n): #1,2,...n-1
        # round(a,2) a保留小数点后两位
        XX0[i] = round((X0[0] - u/a)*(1-math.exp(a))*math.exp(-a*(i)),2)
    #print(XX0) # 根据预测模型预测的值
    #print(X0) #原始数据
    #模型精度的后验差检验
    e = 0      #求残差平均值
    for i in range(0,n):
        e += (X0[i] - XX0[i])
    e /= n

    #求历史数据平均值
    aver = 0
    for i in range(0,n):
        aver += X0[i]
    aver /= n

    #求历史数据方差
    s12 = 0
    for i in range(0,n):
        s12 += (X0[i]-aver)**2
    s12 /= n

    #求残差方差
    s22 = 0
    for i in range(0,n):
        s22 += ((X0[i] - XX0[i]) - e)**2
    s22 /= n

    #求后验差比值:残差方差/原始数据方差
    C = s22 / s12
    """
    指标C是后验差检验的两个重要指标，指标越小越好，C越小
    表示s12大而s22小，s12大表示原始数据方差大，即原始数据离散程度大
    s22小表示残差方差小，即残差离散程度小。
    C小表明尽管原始数据很离散，但模型所得计算值与实际值之差并不太离散
    C<=0.35 1级（好）；0.35<C<=0.5 2级（合格）；0.5<C<=0.65 3级（勉强）；
    C>0.65 4级（不合格）
    """
    #求小误差概率
    cout = 0
    for i in range(0,n):
        if abs((X0[i] - XX0[i]) - e) < 0.6754*math.sqrt(s12):
            cout = cout+1
        else:
            cout = cout
    P = cout / n
    """
       指标P越大越好，P越大，残差与残差平均值之差小于给定值0.6754的点较多，即拟合值（预测值）分布比较均匀
    """
    #print(C,P)
    if (C <= 0.35 and P >= 0.95):
        #预测精度为一级
        print('预测精度为一级(好)：')
    elif (C <=0.5 and P >= 0.8 ):
        print('预测精度为二级(合格)：')
    elif (C <= 0.65 and P >= 0.7):
        print('预测精度为三级(勉强)：')
    else:
        print('预测精度为四级(不合格)：')

    m = 3  # 预测的个数
    print('往后3个月的预测值为：')
    res = np.zeros(m)
    for i in range(0, m):
        res[i] = round((X0[0] - u / a) * (1 - math.exp(a)) * math.exp(-a * (i + n))-c,0) # 返回数据，不保留小数
        print(res[i])
    return res




