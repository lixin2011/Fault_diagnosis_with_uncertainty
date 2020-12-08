import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import sklearn.metrics as sm





# 模型训练
os.chdir(r'E:\Data\combin_data')

list_3 = ['PRE','PRC','kW','fault']

list_8 = ['TWEI','TWEO','TWCI','TWCO','TR_dis','PRE','PRC','kW','fault']

list_22 =  ['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc'
            ,'Tsh_suc','TR_dis','Tsh_dis','PRE','PRC','PO_feed','kW','fault']

proc = list_22  #选择要计算的变量



df_result = pd.DataFrame()
row_count = 0
for var in proc[:-1]: # 选择变量
    df_train = pd.read_excel('train_data_0.xlsx')
    # 使用稳定数据训练
    df_train = df_train.loc[:,proc]  
    x_train = df_train.iloc[:,0:-1]
    print(x_train)
    y_train = df_train.loc[:,'fault']
    print(y_train)
    model = SVC(C=10000,gamma=0.0001)     #change
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
    cp_steady = sm.classification_report(y_test_steady, result)  
    print(cp_steady)
    for std in ['0.2','0.4','0.6','0.8','1.0']:
        # 使用随机数据测试
        file = var + '_0_' + std + '.csv'  #change
        df_test_random = pd.read_csv(file)       
        df_test_random = df_test_random.loc[:,proc]   #change
        x_test_random = df_test_random.iloc[:,0:-1]     #change
        print(x_test_random)
        y_test_random = df_test_random.loc[:,'fault']
        print(y_test_random)
        result = model.predict(x_test_random)
        # score = accuracy_score(y_test_random, result) 
        # cm_random = sm.confusion_matrix(y_test_random, result)
        cp_random = sm.classification_report(y_test_random, result, output_dict=True)
        df_result.loc[row_count,'std'] = std
        df_result.loc[row_count,'var'] = var
        df_result.loc[row_count,'cf'] = cp_random['cf']['precision']
        df_result.loc[row_count,'eo'] = cp_random['eo']['precision']
        df_result.loc[row_count,'fwc'] = cp_random['fwc']['precision']
        df_result.loc[row_count,'fwe'] = cp_random['fwe']['precision']
        df_result.loc[row_count,'rl'] = cp_random['rl']['precision']
        df_result.loc[row_count,'ro'] = cp_random['ro']['precision']
        print(df_result)
        df_result.to_excel(r'22-fault.xlsx')
        print(cp_random)
        row_count += 1