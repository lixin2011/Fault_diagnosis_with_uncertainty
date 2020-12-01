from matplotlib import colors
import matplotlib.pyplot as plt
import os
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import seaborn as sns
os.chdir(r'D:\temp')
df = pd.read_excel(r'22-t.xlsx')

def plot_bar():
    x = df.columns[1:]
    acc_0_0 = df.iloc[0,1:].values
    acc_0_2 = df.iloc[1,1:].values
    acc_0_4 = df.iloc[2,1:].values
    acc_0_6 = df.iloc[3,1:].values
    acc_0_8 = df.iloc[4,1:].values
    acc_1_0 = df.iloc[5,1:].values
    print(acc_0_2)
    plt.figure(figsize=(8,8))
    color = ['#d0d1e6','#a6bddb','#67a9cf','#3690c0','#02818a','#016450']
    plt.bar(x,acc_0_0,color=color[0],width=0.5,zorder=1,align='center',edgecolor='k')
    plt.bar(x,acc_0_2,color=color[1],width=0.5,zorder=1,align='center',edgecolor='k')
    plt.bar(x,acc_0_4,color=color[2],width=0.5,zorder=2,align='center',edgecolor='k')
    plt.bar(x,acc_0_6,color=color[3],width=0.5,zorder=2,align='center',edgecolor='k')
    plt.bar(x,acc_0_8,color=color[4],width=0.5,zorder=2,align='center',edgecolor='k')
    plt.bar(x,acc_1_0,color=color[5],width=0.5,zorder=2,align='center',edgecolor='k')
    plt.ylim(0.85,1)
    plt.yticks(family='Times New Roman',fontsize=13)
    plt.xticks(family='Times New Roman',fontsize=13)
    plt.grid(True,color='grey',linewidth='1',axis='y',alpha=0.2)
    plt.savefig('info.jpg',dpi=300)


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

plot_3()
