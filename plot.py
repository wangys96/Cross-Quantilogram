import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from .calculate import CQBS,CQBS_alphas,CQBS_years

def bar_example(data1,data2,picname="",show=True):
    alist=[0.1,0.5,0.9]
    dataset=[CQBS(data1,alist[i],data2,alist[i],20,verbose=True) for i in range(3)]

    fig1,ax1=plt.subplots(2,3,figsize=(12,4))
    plt.subplots_adjust(wspace=0.3,hspace=0.8) 
    xaxis=[str(x) for x in dataset[0].index]    
    ax1[0][0].set_ylabel("Cross-Quantilogram",fontsize="x-large",labelpad=0.1)

    for i in range(3):
        ax1[0][i].set_title("α={}".format(alist[i]),fontsize="xx-large")       
        ax1[0][i].tick_params(labelsize="large")
        ax1[0][i].axhline(color="black",linewidth=1)
        ax1[0][i].bar(xaxis,dataset[i]["cq"],width=0.2,color="black")
        ax1[0][i].plot(xaxis,dataset[i]["cq_upper"],color='red',linestyle="dashed")
        ax1[0][i].plot(xaxis,dataset[i]["cq_lower"],color='red',linestyle="dashed")
        ax1[0][i].xaxis.set_major_locator(ticker.MultipleLocator(2))
        m = (abs(dataset[i]["cq"]).max()//0.05)*0.05+0.1
        ax1[0][i].set_ylim(-m,m)
        
    ax1[1][0].set_ylabel("Portmanteau",fontsize="x-large")
    for i in range(3):
        ax1[1][i].set_title("α={}".format(alist[i]),fontsize="xx-large")
        ax1[1][i].set_xlabel("lag",fontsize="xx-large")        
        ax1[1][i].tick_params(labelsize="large")
        ax1[1][i].plot(xaxis,dataset[i]["q"],color='black')
        ax1[1][i].plot(xaxis,dataset[i]["qc"],color='red',linestyle="dotted")
        ax1[1][i].xaxis.set_major_locator(ticker.MultipleLocator(2))
    fig1.align_labels()
    if picname:
        fig1.savefig(picname+".png",dpi=200,quality=95,bbox_inches="tight")   
    if show:
        print(str(picname)+":")
        plt.show()

def heatmap_example(data1,data2,picname="",show=True):
    alist=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
    dataset = CQBS_alphas(data1,alist,data2,alist,1,verbose=True)
    data_mat=np.array([[d["cq"] for d in row] for row in dataset])
    data_txt=[["*" if ((d["cq"]>d["cq_upper"] or d["cq"]<d["cq_lower"])and d["q"]>d["qc"])\
                else "" for d in row] for row in dataset]
                
    fig, ax = plt.subplots(figsize=(4,5))
    im = ax.imshow(data_mat, cmap="Greys")
    ax.set_ylabel("US lag=1",fontsize="xx-large",verticalalignment="center",labelpad=5)
    ax.set_xlabel("CN",fontsize="xx-large",labelpad=35)
    cbar = ax.figure.colorbar(im,ax=ax,fraction=0.046,pad=0.02,orientation="horizontal",)
    cbar.ax.tick_params(labelsize="large")
    cbar.ax.set_ylabel("", rotation=-90, va="bottom")
    ax.set_xticks(np.arange(data_mat.shape[1]))
    ax.set_yticks(np.arange(data_mat.shape[0]))
    ax.set_yticklabels(alist,horizontalalignment="right",fontsize="large")
    ax.set_xticklabels(alist,fontsize="large")    
    ax.tick_params(top=True, bottom=False,labeltop=True, labelbottom=False)                   
    plt.setp(ax.get_xticklabels(), rotation=-60, ha="right",rotation_mode="anchor")        
    ax.set_xticks(np.arange(data_mat.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data_mat.shape[0]+1)-.5, minor=True)
    ax.tick_params(which="minor", bottom=False, left=False)
    
    data = im.get_array()
    valfmt="{x}"
    threshold = im.norm(data.max())/2.0
    textcolors=["black", "white"]
    kw = dict(horizontalalignment="center",verticalalignment="center")              
    valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[im.norm(data[i, j]) > threshold])
            text = im.axes.text(j, i, valfmt(data_txt[i][j], None),fontsize="large",**kw)

    fig.tight_layout()
    if picname:
        fig.savefig(picname+".png",dpi=200,quality=95,bbox_inches="tight")
    if show:
        print(picname+":")
        plt.show()

def rolling_example(data1,data2,picname="",show=True):
    alist=[0.1,0.5,0.9]
    dataset = [CQBS_years(data1,alist[i],data2,alist[i],verbose=True) for i in range(3)]
    fig1,ax1=plt.subplots(2,3,figsize=(12,6))
    plt.subplots_adjust(wspace=0.3,hspace=0.5) 
    xaxis=[x for x in dataset[0].index]
    
    ax1[0][0].set_ylabel("Rolling\nCross-Quantilogram",fontsize="x-large",labelpad=0.1)
    for i in range(3):
        ax1[0][i].set_title("α={}".format(alist[i]),fontsize="xx-large")     
        ax1[0][i].tick_params(labelsize="large")
        ax1[0][i].axhline(color="black",linewidth=1)        
        ax1[0][i].plot(xaxis,dataset[i]["cq_upper"],"rd--",markersize=5,markerfacecolor="w")
        ax1[0][i].plot(xaxis,dataset[i]["cq_lower"],"rd--",markersize=5,markerfacecolor="w")
        ax1[0][i].plot(xaxis,dataset[i]["cq"],"ko-",markersize=4)
        ax1[0][i].xaxis.set_major_locator(ticker.MultipleLocator(2))
        m = (max(abs(dataset[i]["cq"]).max(),abs(dataset[i]["cq_upper"]).max(),abs(dataset[i]["cq_lower"]).max())//0.05)*0.05+0.1
        ax1[0][i].set_ylim(-m,m)
        
    ax1[1][0].set_ylabel("Portmanteau",fontsize="x-large")
    for i in range(3):
        ax1[1][i].set_title("α={}".format(alist[i]),fontsize="xx-large")
        ax1[1][i].set_xlabel("year",fontsize="xx-large")        
        ax1[1][i].tick_params(labelsize="large")
        ax1[1][i].plot(xaxis,dataset[i]["q"],color='black')
        ax1[1][i].plot(xaxis,dataset[i]["qc"],color='red',linestyle="dotted")
        ax1[1][i].xaxis.set_major_locator(ticker.MultipleLocator(2))
    fig1.align_labels()

    if picname:
        fig1.savefig(picname+".png",dpi=200,quality=95,bbox_inches="tight")   
    if show:
        print(picname+":")
        plt.show()