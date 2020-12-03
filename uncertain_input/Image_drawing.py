import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import cm,colors

os.chdir(r'D:\temp')
df = pd.read_excel(r'8.xlsx')
colors_green = [
    '#edf8e9',
    '#c7e9c0',
    '#a1d99b',
    '#74c476',
    '#31a354',
    '#006d2c'
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
    '#eff3ff',
    '#c6dbef',
    '#9ecae1',
    '#6baed6',
    '#3182bd',
    '#08519c'
]
colors_purple = [
    '#f2f0f7',
    '#dadaeb',
    '#bcbddc',
    '#9e9ac8',
    '#756bb1',
    '#54278f'
]
colors_yellow = [
    '#feedde'
    '#fdd0a2',
    '#fdae6b',
    '#fd8d3c',
    '#e6550d',
    '#a63603'
]
def plot_samping_line_chart():
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


def plot_waterfall_3D():
    fig = plt.figure(figsize=(8,8),dpi=200)
    ax = fig.gca(projection='3d')
    ax.view_init(azim=-70,elev=20)
    ax.grid(False)
    xs = ['0','0.2','0.4','0.6','0.8','1.0']
    zs = ['PRE','PRC','kW']
    verts = []
    for z in zs:
        ys = df[z].values
        verts.append(list(zip(xs,ys)))
    print(verts)
    pal_husl = sns.husl_palette(len(zs),h=15/360,l=0.65,s=1).as_hex
    # 在HUSL调色空间获得均匀间隔的颜色
    poly = PolyCollection(verts,facecolors=pal_husl,edgecolor='k')
    # ax.add_collection3d(poly,zs=zs,zdir='y')
    # plt.show()

def plot_3():
    plt.figure(figsize=(23,6),dpi=300)
    x = df.columns[1:]
    color = ['#d0d1e6','#c6dbef','#9ecae1','#6baed6','#3182bd','#08519c']
    for var,mc in zip(list(range(0,5)),[1,2,3,4,5]):
        y = df.iloc[var,1:].values
        print(y)
        plt.bar(x=x,height=y,edgecolor='k',color=color[mc],zorder=10-var,width=0.8)
        print(x)

    plt.xticks(family='Times New Roman',fontsize=15)
    plt.yticks(family='Times New Roman',fontsize=15)
    plt.ylim(0,30)
    # plt.fill_between(x,df['kW'],0,color=color[5],alpha=0.3,zorder=1)
    # plt.fill_between(x,df['PRC'],0,color=color[4],alpha=0.3,zorder=2)
    # plt.fill_between(x,df['PRE'],0,color=color[3],alpha=0.3,zorder=3)
    plt.savefig(r'3.jpg')

def plot_8():
    plt.figure(figsize=(8,4),dpi=300)
    # x = ['0','0.2','0.4','0.6','0.8','1.0']
    color = [  '#66c2a5',
               '#fc8d62',
               '#8da0cb',
               '#e78ac3',
               '#a6d854', ]

    for var,mc in zip([0,5000,10000],list(range(3))):
        y = df.iloc[var:var+5000,5]
        print(y)
        plt.hist(y,zorder=5-mc,label=var,color=color[mc],bins=50,edgecolor='grey',density=True)
    plt.xlim(260,275)
    plt.ylim(0,2)
    plt.xticks(family='Times New Roman',fontsize=15)
    plt.yticks(family='Times New Roman',fontsize=15)
    # plt.fill_between(x,df['kW'],0,color=color[5],alpha=0.3,zorder=1)
    # plt.fill_between(x,df['PRC'],0,color=color[4],alpha=0.3,zorder=2)
    # plt.fill_between(x,df['PRE'],0,color=color[3],alpha=0.3,zorder=3)
    plt.savefig(r'8.jpg')

def scatter():
    plt.figure(figsize=(8,4),dpi=300)
    x = df.index
    y = df.iloc[:,5]
    plt.plot(x,y,linewidth=1,color='#08306b')
    plt.xticks(family='Times New Roman',fontsize=15)
    plt.yticks(family='Times New Roman',fontsize=15)
    plt.ylim(260,275)
    plt.grid(axis='y')
    plt.savefig(r'3.jpg')

# plot_samping_line_chart()
# plot_samping_hist_chart()
plot_radial_column_chart()