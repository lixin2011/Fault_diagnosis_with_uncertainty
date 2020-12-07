import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import seaborn as sns

os.chdir(r'D:\temp')
colors_green = [
    '#a1d99b',
    '#74c476',
    '#41ab5d',
    '#238b45',
    '#006d2c',
    '#00441b'
]
colors_red = [
    '#fee5d9',
    '#fcbba1',
    '#fc9272',
    '#fb6a4a',
    '#de2d26',
    '#a50f15'
]
colors_blue = [
    '#9ecae1',
    '#6baed6',
    '#4292c6',
    '#2171b5',
    '#08519c',
    '#08306b'
]
colors_purple = [
    '#bcbddc',
    '#9e9ac8',
    '#807dba',
    '#6a51a3',
    '#54278f',
    '#3f007d'
]
colors_yellow = [
    '#fdae6b',
    '#fd8d3c',
    '#f16913',
    '#d94801',
    '#a63603',
    '#7f2704'
]
def plot_samping_line_chart():
    '''
    绘制采样点的柱形图
    '''
    colors = ['#377eb8','#984ea3','#ff7f00']
    for uncertainty_level in list(range(6)):
        plt.figure(figsize=(9,5),dpi=300)
        for start_index,color_index in zip([0,5000,10000],[0,1,2]):
            x = df.index[start_index:start_index+5000]
            y = df.iloc[start_index:start_index+5000,uncertainty_level]
            print(y)
            plt.plot(x,y,linewidth=0.8,color=colors[color_index])
        plt.xticks(family='Times New Roman',fontsize=17)
        plt.yticks(family='Times New Roman',fontsize=17)
        plt.ylim(260,274)
        plt.grid(axis='y')
        plt.savefig(str(uncertainty_level)+'-line-chart.jpg')

def plot_samping_hist_chart():
    '''
    绘制采样点的直方图
    '''
    colors = ['#377eb8','#984ea3','#ff7f00']
    for uncertainty_level in list(range(6)):
        plt.figure(figsize=(9,5),dpi=300)
        for start_index,color_index in zip([0,5000,10000],[0,1,2]):
            y = df.iloc[start_index:start_index+5000,uncertainty_level]
            print(y)
            plt.hist(y,color=colors[color_index],density=True,edgecolor='grey',bins=45)
        plt.xticks(family='Times New Roman',fontsize=17)
        plt.yticks(family='Times New Roman',fontsize=17)
        plt.ylim(0,2)
        plt.grid(axis='x')
        plt.savefig(str(uncertainty_level)+'-hist-chart.jpg')

def plot_radial_column_chart():
    '''
    绘制故障的径向柱图
    '''
    plt.rc('patch',force_edgecolor=True)
    plt.rc('axes',axisbelow=True)
    fig = plt.figure(figsize=(8,8),dpi=300)
    n_row = df.shape[0]
    start_angle = 0
    for i in range(1,9):
        angle = np.arange(start_angle,start_angle + np.pi/4,np.pi/4/n_row)
        # 将横坐标（行名）转换为角度坐标
        radius = np.array(df.iloc[:,i])
        # 选择不同的列
        print(df.iloc[:,0])
        # 将纵坐标（DATaFrame中的第一列）转换为半径坐标    
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        plt.ylim(-0.03,0.2)
        # 将起始点设置为负值，就可以获得一个空心内圆
        plt.bar(angle,radius,color=colors_blue,alpha=0.9,width=0.13,align="edge", linewidth=0.2,edgecolor='k',zorder=1)
        # width需要微调保证比例，避免重叠
        start_angle += np.pi/4
    plt.grid(which='major',axis ="x", linestyle='-', linewidth='0.5', color='gray',alpha=0.5,zorder=1)
    plt.grid(which='major',axis ="y", linestyle='-', linewidth='0.5', color='gray',alpha=0.5,zorder=1)
    plt.xticks(alpha=0)
    plt.yticks(alpha=0)
    plt.savefig(r'1.jpg')

def plot_dumbball_chart(df,var,colors,w,h,start):
    '''
    绘制变量的哑铃图
    '''
    plt.rcParams["axes.grid"] = True
    plt.rcParams["grid.linestyle"] = (10,10)
    df = df.sort_values(axis=1,by=[1.0])
    print(df)
    fig = plt.figure(figsize=(w,h),dpi=300)
    y = df.columns
    for i in range(6): # 指定不确定度
        x = df.iloc[i,:]
        print(x)
        print(y)
        plt.scatter(x,y,color=colors[5-i],zorder=1)
    for i in range(5): # 指定不确定度，需要减1
        for j in range(var): # 指定变量
            plt.hlines(y=df.columns[j],xmin=df.iloc[i,j],xmax=df.iloc[i+1,j],zorder=0,colors=colors[5-i])
    plt.xticks([0.98,1.0],family='Times New Roman',fontsize=18)
    plt.yticks(family='Times New Roman',fontsize=18)
    # plt.grid(axis='x',alpha=0.5)
    plt.savefig(r'3.jpg')




if __name__ == "__main__":
    df = pd.read_excel(r'36.xlsx',index_col='std')
    # plot_samping_line_chart()
    # plot_samping_hist_chart()
    # plot_radial_column_chart()
    # plot_dumbball_chart(df,3,colors_green,5,6,0.5)
    # plot_dumbball_chart(df,8,colors_blue,7,9,0.85)
    # plot_dumbball_chart(df,22,colors_purple,9,16,0.9)
    plot_dumbball_chart(df,36,colors_yellow,9,22,0.9)
