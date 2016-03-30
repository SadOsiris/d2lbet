#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def team_ana():
    bv=0.0
    nv=0.0
    buf=0
    with open("data-good-new") as f:
        content = f.readlines()
    while (buf<len(content)):
        t=content[buf]
        #var=re.sub('s+','\t',t).split('\t')
        #t.strip() for t in data_string.splitlines():
        #var=t
        var=t.split('\t')
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        odds=var[8].split()
        if (len(odds)==4):
            lv=float(odds[1])
            rv=float(odds[2])
        elif(len(odds)==2):
            lv=float(odds[0])
            rv=float(odds[1])
        else:
            buf+=1
            continue
        if (int(var[6])>50 and var[5]=="1"):
            bv+=lv
            nv-=1
        elif (int(var[6])<50 and var[5]=="2"):
            bv+=rv
            nv-=1
        elif (int(var[6])<50 and var[5]=="1"):
            bv-=1
            nv+=lv

        elif (int(var[6])>50 and var[5]=="2"):
            bv-=1
            nv+=rv
        buf+=1
        team_f=open("allfavor"+".txt",'a')
        team_f.write(var[0]+" "+var[1]+" "+str(bv)+" "+str(nv)+'\n')
    team_draw=np.genfromtxt("./allfavor"+".txt",delimiter=' ',names=['foo','bar','bv','nv'])
# Create the plot
#    plt.plot(team_draw['bk'],label='bk',color='r')
    plt.plot(team_draw['bv'],label='bv',color='r')
#    plt.plot(team_draw['nk'],label='nk',color='r',linestyle="dashed")
    plt.plot(team_draw['nv'],label='nv',color='y',linestyle="dashed")
    plt.legend(
            loc='upper center', bbox_to_anchor=(0.5, -0.03),
                      fancybox=True, shadow=True, ncol=4
            )
# Save the figure in a separate file
    plt.savefig("allavor"+".png")
# Draw the plot to the screen
#    plt.show()
    plt.clf()


team_ana()

