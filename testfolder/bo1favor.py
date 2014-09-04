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
        #var=re.sub('s+','\t',t).split('\t')
        #t.strip() for t in data_string.splitlines():
        #var=t
        var=t.split('\t')
        if var[9]!="1\n":
            buf+=1
            continue
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        odds=var[8].split()
        if(len(odds)<7):
            lk=float(odds[0])
            lv=float(odds[1])
            rk=float(odds[3])
            rv=float(odds[2])
        if (int(var[6])>50 and var[5]=="1"):
            bk+=4*lk
            bv+=4*lv
            nk-=4
            nv-=4
        elif (int(var[6])<50 and var[5]=="2"):
            bk+=4*rk
            bv+=4*rv
            nk-=4
            nv-=4
        elif (int(var[6])<50 and var[5]=="1"):
            bk-=4
            bv-=4
            nk+=4*lk
            nv+=4*lv
            #nk+=int(var[8+idx])
            #nv+=int(var[9+idx])
            #nc+=int(var[10+idx])

        elif (int(var[6])>50 and var[5]=="2"):
            bk-=4
            bv-=4
            nk+=4*rk
            nv+=4*rv
            #nk+=int(var[13-idx])
            #nv+=int(var[12-idx])
            #nc+=int(var[11-idx])
            #print var[0],,bv,bc,nk,nv,nc
        buf+=1
        team_f=open("bo1favor"+".txt",'a')
        team_f.write(var[0]+" "+var[1]+" "+str(bk)+" "+str(bv)+" "+str(nk)+" "+str(nv)+'\n')
    team_draw=np.genfromtxt("./bo1favor"+".txt",delimiter=' ',names=['foo','bar','bk','bv','nk','nv'])
#    print(team_draw['bbku'])
# Create the plot
    plt.plot(team_draw['bk'],label='bk',color='r')
    plt.plot(team_draw['bv'],label='bv',color='g')
    plt.plot(team_draw['nk'],label='nk',color='r',linestyle="dashed")
    plt.plot(team_draw['nv'],label='nv',color='g',linestyle="dashed")
    plt.legend(
            loc='upper center', bbox_to_anchor=(0.5, -0.03),
                      fancybox=True, shadow=True, ncol=6
            )
# Save the figure in a separate file
    plt.savefig("bo1favor"+".png")
# Draw the plot to the screen
#    plt.show()
    plt.clf()


team_ana()

