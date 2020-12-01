import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import sklearn.metrics as sm

# 导入文件并进行数据拆分
os.chdir(r'D:\Data\ua')
df_steady = pd.read_excel('test_data_0.xlsx')  #只使用了一种稳态数据集
for var in  ['TWCO']:
        # 遍历所有变量，为每一个不确定性变量创建一个数据量为1358*5000行的文件
    df_combin_all = pd.DataFrame(columns=['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc','Tsh_suc','TR_dis','Tsh_dis','PRE','PRC','PO_feed','FWC','FWE','FWW','FWH','FWB','VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net','kW','fault'])
    for row in range(1357):
        # 处理随机数据
        df_random = pd.read_excel('0_'+str(row)+'_1.0.xlsx')   #更改文件
        data_random = df_random.loc[:,var]
        # 处理稳定数据
        data_steady = df_steady.loc[row,'TWEI':"fault"]
        data_steady = np.array(data_steady)
        data_steady_all = np.repeat(data_steady,5000,0)
        data_steady_all = data_steady_all.reshape(37,5000)
        data_steady_all = data_steady_all.T
        df_combin = pd.DataFrame(data_steady_all,columns=['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc','Tsh_suc','TR_dis','Tsh_dis','PRE','PRC','PO_feed','FWC','FWE','FWW','FWH','FWB','VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net','kW','fault'])
        # 数据组合
        df_combin.loc[:,var] = data_random
        df_combin_all = pd.concat([df_combin_all,df_combin],axis=0)
        print('\n随机变量为'+var+',增加第'+str(row)+'行的数据：\n')
        print(df_combin_all)
    df_combin_all.to_csv(var+'_0_1.0.csv')   #更改文件
    del df_combin_all
    print('\n\nsample finished')


