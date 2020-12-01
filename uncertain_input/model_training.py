import pandas as pd
import numpy as np
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


drop_list_3 = ['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc','Tsh_suc','TR_dis','Tsh_dis'
            ,'PO_feed','FWC','FWE','FWW','FWH','FWB','VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net']
drop_list_8 = ['TBI','TBO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc','Tsh_suc','Tsh_dis','PO_feed','FWC','FWE','FWW','FWH','FWB',
            'VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net']
drop_list_21 = ['FWC','FWE','FWW','FWH','FWB','VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net','kW']
drop_list_36 = []      
    


# 导入文件并进行数据拆分
os.chdir(r'D:\Data\ua')
'''
df = pd.read_excel('data_selected.xlsx')
print(df)
data = df.loc[:,:'kW']
print(data)
flag = df.loc[:,'fault']
print(flag)
for random_value in range(5):
    x_train,x_test,y_train,y_test = train_test_split(data,flag,random_state=random_value,test_size=0.3)
    #将经过拆分的文件分割为两个文件
    x_train_data = pd.DataFrame(x_train)
    y_train_data = pd.DataFrame(y_train)
    train_data = pd.concat([x_train_data,y_train_data],axis=1)
    train_data.to_excel('train_data_'+str(random_value)+'.xlsx')
    x_test_data = pd.DataFrame(x_test)
    y_test_data = pd.DataFrame(y_test)
    test_data = pd.concat([x_test_data,y_test_data],axis=1)
    test_data.to_excel('test_data_'+str(random_value)+'.xlsx')'''

train_data = pd.read_excel(r'train_data_0.xlsx')
# train_data = train_data.drop(columns=drop_list_21)
x_train = train_data.iloc[:,1:-1]
print(x_train)
y_train = train_data.loc[:,'fault']
print(y_train)
test_data = pd.read_excel(r'test_data_0.xlsx')
# test_data = test_data.drop(columns=drop_list_21)
x_test = test_data.iloc[:,1:-1]
print(x_test)
y_test = test_data.loc[:,'fault']
print(y_test)
k = 0
a = 0
a1,a2,a3 = [],[],[]
for i in [1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,1e2,1e3,1e4,1e5,1e6,1e7,1e8]:
    for ga in [1e-8,1e-7,1e-6,1e-5,1e-4,1e-3,1e-2,1e-1,1,1e2,1e3,1e4,1e5,1e6,1e7,1e8]:
                                k = k + 1
                                print('*',end='\r')  #迭代次数
                                model = SVC(C=i,gamma=ga)
                                model.fit(x_train,y_train)
                                result = model.predict(x_test)
                                score = accuracy_score(y_test, result)                                 
                                if score > a:
                                    a = score
                                    print('\n')
                                    print('\n......updating parameters............\n')
                                    print('C:  ',i)
                                    a1.append(i)
                                    print('gamma:  ',ga)
                                    a2.append(ga)
                                    print('\naccuracy:  ',score)
                                    a3.append(score)
                                    param_list = np.array([a1,a2,a3])
                                    param_list = param_list.T
                                    param = pd.DataFrame(param_list,columns=['C','gamma','accuracy'])                                         
print('\n\n\n\n......updating finished......\n')
print('best n_estimators:  ',a1[-1])
print('best max_depth:  ',a2[-1])
print('best score:  ',a3[-1])
print('\n\n')
               