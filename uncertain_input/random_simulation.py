import numpy as np
import pandas as pd
import os
os.chdir(r'D:\Data\ua')
random_value = 0  #不同的稳态测试集，用于验证结果是否统一，暂时只做0
df = pd.read_excel('test_data_'+str(random_value)+'.xlsx')
for row in range(1357):
    data = pd.DataFrame()
    for var in range(1,37):
        #组合所有行的不确定性数据
        #i为数据的行（为不同时刻的数据）
        #j为数据的列（为不同变量对应的数据，第一列为索引，数据从第二列开始（即为从1开始））
        ave = df.iloc[row,var]
        std = 0.4  #手动设置
        random_list = np.random.normal(loc=ave,scale=std,size=5000)
        temp_data = pd.DataFrame(random_list,columns=[str(var)])
        data = pd.concat([data,temp_data],axis=1)
    
    data.columns = ['TWEI','TWEO','TBI','TBO','TWCI','TWCO','TSI','TSO','THI','THO','TWI','TWO','TO_sump','TO_feed','T_suc','Tsh_suc','TR_dis','Tsh_dis','PRE','PRC','PO_feed','FWC','FWE','FWW','FWH','FWB','VSS','VSL','VH','VM','VC','VE','VW','P_lift','PO_net','kW']
    print(data)
    data.to_excel(str(random_value)+'_'+str(row)+'_'+str(std)+'.xlsx',index=False)


