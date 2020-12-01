import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import sklearn.metrics as sm





# 模型训练
os.chdir(r'D:\Data\ua\combin_data')
'''df_train = pd.read_excel('train_data_0.xlsx')

df_train = df_train.drop(columns=drop_list_22)    #change

x_train = df_train.iloc[:,1:-1]
print(x_train)
y_train = df_train.loc[:,'fault']
print(y_train)
model = SVC(C=10000,gamma=0.0001)     #change
model.fit(x_train,y_train)
# 使用稳定数据测试
df_test_steady = pd.read_excel('test_data_0.xlsx')

df_test_steady = df_test_steady.drop(columns=drop_list_22)    #change

x_test_steady = df_test_steady.iloc[:,1:-1]
print(x_test_steady)
y_test_steady = df_test_steady.loc[:,'fault']
print(y_test_steady)
result = model.predict(x_test_steady)
score = accuracy_score(y_test_steady, result)  
print(score)
cm_ateady = sm.confusion_matrix(y_test_steady, result)
cp_steady = sm.classification_report(y_test_steady, result)
print(cm_ateady)
print(cp_steady)'''
# 使用随机数据测试
# 进入循环

list_3 = ['PRE','PRC','kW','fault']

list_8 = ['TWEI','TWEO','TWCI','TWCO','TR_dis','PRE','PRC','kW','fault']

list_22 =  ['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc'
            ,'Tsh_suc','TR_dis','Tsh_dis','PRE','PRC','PO_feed','kW','fault']

proc = list_8



df_result = pd.DataFrame()
for var in proc[:-1]:
    df_train = pd.read_excel('train_data_0.xlsx')
    df_train = df_train.loc[:,proc]
    print(df_train)    
    x_train = df_train.iloc[:,0:-1]
    print(x_train)
    y_train = df_train.loc[:,'fault']
    print(y_train)
    model = SVC(C=100,gamma=0.1)     #change
    model.fit(x_train,y_train)
    # 使用稳定数据测试
    df_test_steady = pd.read_excel('test_data_0.xlsx')
    df_test_steady = df_test_steady.loc[:,proc]   
    x_test_steady = df_test_steady.iloc[:,0:-1]
    print(x_test_steady)
    y_test_steady = df_test_steady.loc[:,'fault']
    print(y_test_steady)
    result = model.predict(x_test_steady)
    score = accuracy_score(y_test_steady, result)  
    print(score)
    for std in ['0.2','0.4','0.6','0.8','1.0']:
        # 使用稳定数据训练

        # cm_ateady = sm.confusion_matrix(y_test_steady, result)
        # cp_steady = sm.classification_report(y_test_steady, result)
        # 使用随机数据测试
        file = var + '_0_' + std + '.csv'  #change
        df_test_random = pd.read_csv(file)       
        df_test_random = df_test_random.loc[:,proc]   #change
        x_test_random = df_test_random.iloc[:,0:-1]     #change
        print(x_test_random)
        y_test_random = df_test_random.loc[:,'fault']
        print(y_test_random)
        result = model.predict(x_test_random)
        score = accuracy_score(y_test_random, result) 
        df_result.loc[std,var] = score 
        # cm_random = sm.confusion_matrix(y_test_random, result)
        # cp_random = sm.classification_report(y_test_random, result)
        print(df_result)
df_result.to_excel(r'8.xlsx')
