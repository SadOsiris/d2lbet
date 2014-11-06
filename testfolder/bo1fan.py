#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

bo2count=0
bo1win=0
def team_ana(str_list):
    strt=str_list.split('\n')
    print strt[0]
    bk=0.0
    bv=0.0
    nk=0.0
    nv=0.0

    idx=0
    buf=0
    with open("data-good-new") as f:
        content = f.readlines()
    while (buf<len(content)):
        global bo1win
        idx=1
        t=content[buf]
        #var=re.sub('s+','\t',t).split('\t')
        #t.strip() for t in data_string.splitlines():
        #var=t
        var=t.split('\t')
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        if(var[2]!=strt[0] and var[1]!=strt[0]):
            buf+=1
            #if(var[4]==strt[0] or var[3]==strt[0]):
            continue
        if(var[9]!="1\n"):
            buf+=1
            continue
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

        team_f=open("bo1_"+strt[0],'a')
        team_f.write(var[0]+" "+var[1]+" "+str(bk)+" "+str(bv)+" "+str(nk)+" "+str(nv)+'\n')
        buf+=1
        bo1win+=1

with open("complete_teamlist") as f:
    team_list = f.readlines()
team_idx=0
print team_list
while (team_idx<len(team_list)):
    global bo1win
    bo1win=0
    team_ana(team_list[team_idx])
    team_name=team_list[team_idx].split('\n')
    if bo1win>0:
        team_draw=np.genfromtxt('./bo1_'+team_name[0],delimiter=' ',names=['foo','bar','bk','bv','nk','nv'])

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
        plt.savefig('bo1_'+team_name[0]+'.png')

# Draw the plot to the screen
#    plt.show()
        plt.clf()

    team_idx+=1



