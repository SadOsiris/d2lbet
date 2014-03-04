#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def team_ana():
    bet=[60,63,67,68,69,70,79,80,81,82,83,84]
    underdog=[54,59,62,64,71,72,73,74,75]
    br=0.0
    bu=0.0
    bc=0.0
    nr=0.0
    nu=0.0
    nc=0.0
    buf=0
    team_f=open("ideal.txt",'a')
    team_f.write(str(0)+" "+str(0)+" "+str(br)+" "+str(bu)+" "+str(bc)+" "+str(nr)+" "+str(nu)+" "+str(nc)+'\n')
    with open("data-test") as f:
        content = f.readlines()
    while (buf<len(content)):
        t=content[buf]
        #var=re.sub('s+','\t',t).split('\t')
        #t.strip() for t in data_string.splitlines():
        #var=t
        var=t.split('\t')
        if((int(var[6]) not in bet) and (100-int(var[6]) not in underdog )):
            buf+=1
            continue
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        odds=var[8].split()
        if(len(odds)<7):
            lr=float(odds[0])
            lu=float(odds[1])
            lc=float(odds[2])
            rr=float(odds[5])
            ru=float(odds[4])
            rc=float(odds[3])
        else:
            lr=float(odds[1])
            lu=float(odds[2])
            lc=float(odds[3])
            rr=float(odds[6])
            ru=float(odds[5])
            rc=float(odds[4])
        if ((int(var[6])in bet) or ((100-int(var[6])) in bet)):
            if (int(var[6])>50 and var[5]=="1"):
                #br+=int(var[8+idx])
                #bu+=int(var[9+idx])
                #bc+=int(intvar[10+idx])
                br+=lr
                bu+=lu
                bc+=lc
                nr-=4
                nu-=4
                nc-=4
            elif (int(var[6])<50 and var[5]=="2"):
                #br+=int(var[13-idx])
                #bu+=int(var[12-idx])
                #bc+=int(var[11-idx])
                br+=rr
                bu+=ru
                bc+=rc
                nr-=4
                nu-=4
                nc-=4
            elif (int(var[6])>50 and var[5]=="2"):
                #br+=int(var[8+idx])
                #bu+=int(var[9+idx])
                #bc+=int(intvar[10+idx])
                br-=4
                bu-=4
                bc-=4
                nr+=rr
                nu+=ru
                nc+=rc
            elif (int(var[6])<50 and var[5]=="1"):
                #br+=int(var[8+idx])
                #bu+=int(var[9+idx])
                #bc+=int(intvar[10+idx])
                br-=4
                bu-=4
                bc-=4
                nr+=lr
                nu+=lu
                nc+=lc
        else:
            if (int(var[6])<50 and var[5]=="1"):
                nr-=4
                nu-=4
                nc-=4
                br+=lr
                bu+=lu
                bc+=lc
                #nr+=int(var[8+idx])
                #nu+=int(var[9+idx])
                #nc+=int(var[10+idx])

            elif (int(var[6])>50 and var[5]=="2"):
                nr-=4
                nu-=4
                nc-=4
                br+=rr
                bu+=ru
                bc+=rc
            elif (int(var[6])>50 and var[5]=="1"):
                nr+=lr
                nu+=lu
                nc+=lc
                br-=4
                bu-=4
                bc-=4
            elif (int(var[6])<50 and var[5]=="2"):
                br-=4
                bu-=4
                bc-=4
                nr+=rr
                nu+=ru
                nc+=rc
            #nr+=int(var[13-idx])
            #nu+=int(var[12-idx])
            #nc+=int(var[11-idx])
            #print var[0],br,bu,bc,nr,nu,nc
        buf+=1
        team_f=open("ideal.txt",'a')
        team_f.write(var[0]+" "+var[1]+" "+str(br)+" "+str(bu)+" "+str(bc)+" "+str(nr)+" "+str(nu)+" "+str(nc)+'\n')
    team_draw=np.genfromtxt("./ideal.txt",delimiter=' ',names=['foo','bar','br','bu','bc','nr','nu','nc'])
#    print(team_draw['bu'])
# Create the plot
    plt.plot(team_draw['br'],label='br',color='r')
    plt.plot(team_draw['bu'],label='bu',color='g')
    plt.plot(team_draw['bc'],label='bc',color='b')
    plt.plot(team_draw['nr'],label='nr',color='r',linestyle="dashed")
    plt.plot(team_draw['nu'],label='nu',color='g',linestyle="dashed")
    plt.plot(team_draw['nc'],label='nc',color='b',linestyle="dashed")
    plt.legend(
            loc='upper center', bbox_to_anchor=(0.5, -0.03),
                      fancybox=True, shadow=True, ncol=6
            )
# Save the figure in a separate file
    plt.savefig("ideal.png")
# Draw the plot to the screen
#    plt.show()
    plt.clf()

team_ana()
