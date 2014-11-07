#!/usr/bin/python
import sys
import numpy as np
import matplotlib.pyplot as plt
import re

def team_ana():
#    strt=str_list.split('\n')
#    print strt[0]
#    bk=0.0
#    bv=0.0
#    nk=0.0
#    nv=0.0
#    idx=0
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
        #print var[0],var[1],var[2],var[3],var[4],var[5],var[6],var[7],var[8],var[9]
        team_2=open("datafrom_"+var[2],'a')
        team_2.write(content[buf])
        team_1=open("datafrom_"+var[1],'a')
        team_1.write(content[buf])
        buf+=1
        print(str(buf)+"\n")


#readteam
team_ana()
