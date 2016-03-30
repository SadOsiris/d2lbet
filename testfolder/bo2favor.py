#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def team_ana():
    bk=0.0
    bv=0.0
    nk=0.0
    nv=0.0
    buf=0
    with open("data-good-new") as f:
        content = f.readlines()
    while (buf<len(content)):
        t=content[buf]
        var=t.split('\t')
        if (var[9]=="1\n")or(var[9]=="3\n")or(var[9]=="5\n"):
            buf+=1
            continue
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        odds=var[8].split()
        if(len(odds)==4):
            lv=float(odds[1])
            rv=float(odds[2])
        elif(len(odds)==2):
            lv=float(odds[0])
            rv=float(odds[1])
        else:
            buf+=1
            continue
        if (int(var[6])>50 and var[5]=="1"):
           # bk+=4*lk
            bv+=lv
           # nk-=4
            nv-=1
        elif (int(var[6])<50 and var[5]=="2"):
            #bk+=4*rk
            bv+=rv
            #nk-=4
            nv-=1
        elif (int(var[6])<50 and var[5]=="1"):
            #bk-=4
            bv-=1
            #nk+=4*lk
            nv+=lv
            #nk+=int(var[8+idx])
            #nv+=int(var[9+idx])
            #nc+=int(var[10+idx])

        elif (int(var[6])>50 and var[5]=="2"):
            #bk-=4
            bv-=1
            #nk+=4*rk
            nv+=rv
            #nk+=int(var[13-idx])
            #nv+=int(var[12-idx])
            #nc+=int(var[11-idx])
            #print var[0],,bv,bc,nk,nv,nc
        buf+=1
        team_f=open("bo2favor"+".txt",'a')
        team_f.write(var[0]+" "+var[1]+" "+str(bv)+" "+str(nv)+'\n')
    team_draw=np.genfromtxt("./bo2favor"+".txt",delimiter=' ',names=['foo','bar','bv','nv'])
# Create the plot
#    plt.plot(team_draw['bk'],label='bk',color='r')
    plt.plot(team_draw['bv'],label='bv',color='r')
#    plt.plot(team_draw['nk'],label='nk',color='r',linestyle="dashed")
    plt.plot(team_draw['nv'],label='nv',color='g',linestyle="dashed")
    plt.legend(
            loc='upper center', bbox_to_anchor=(0.5, -0.03),
                      fancybox=True, shadow=True, ncol=4
            )
# Save the figure in a separate file
    plt.savefig("bo2favor"+".png")
# Draw the plot to the screen
    plt.clf()

team_ana()

