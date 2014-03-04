#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def team_ana(str_list):
    strt=str_list.split('\n')
    print strt[0]
    br=0.0
    bu=0.0
    bc=0.0
    nr=0.0
    nu=0.0
    nc=0.0
    idx=0
    buf=0
    with open("data-good-new") as f:
        content = f.readlines()
    while (buf<len(content)):
        idx=1
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


        if (var[1]==strt[0] and var[5]=="1"):
            #br+=int(var[8+idx])
            #bu+=int(var[9+idx])
            #bc+=int(intvar[10+idx])
            br+=lr
            bu+=lu
            bc+=lc
            nr-=4
            nu-=4
            nc-=4
        elif(var[1]==strt[0] and var[5]=="2"):
            #br+=int(var[13-idx])
            #bu+=int(var[12-idx])
            #bc+=int(var[11-idx])
            br+=rr
            bu+=ru
            bc+=rc
            nr-=4
            nu-=4
            nc-=4
        elif(var[2]==strt[0] and var[5]=="1"):
            br-=4
            bu-=4
            bc-=4
            nr+=lr
            nu+=lu
            nc+=lc
            #nr+=int(var[8+idx])
            #nu+=int(var[9+idx])
            #nc+=int(var[10+idx])

        elif(var[2]==strt[0] and var[5]=="2"):
            br-=4
            bu-=4
            bc-=4
            nr+=rr
            nu+=ru
            nc+=rc
            #nr+=int(var[13-idx])
            #nu+=int(var[12-idx])
            #nc+=int(var[11-idx])
        elif(var[2]!=strt[0] and var[1]!=strt[0]):
            idx=2
        if (idx!=2):
            #print var[0],br,bu,bc,nr,nu,nc
            team_f=open(strt[0],'a')
            team_f.write(str(buf)+" "+var[0]+" "+str(br)+" "+str(bu)+" "+str(bc)+" "+str(nr)+" "+str(nu)+" "+str(nc)+'\n')
        buf+=1

with open("teamlist") as f:
    team_list = f.readlines()
team_idx=0
print team_list
while (team_idx<len(team_list)):
    team_ana(team_list[team_idx])
    team_name=team_list[team_idx].split('\n')
    team_draw=np.genfromtxt('./'+team_name[0],delimiter=' ',names=['foo','bar','br','bu','bc','nr','nu','nc'])
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
    plt.savefig(team_name[0]+'bo1.png')

# Draw the plot to the screen
#    plt.show()
    plt.clf()

    team_idx+=1



