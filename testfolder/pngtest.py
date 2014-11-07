import random
import numpy as np

trial_counts=10000
n=0.0
bk=0.0
bv=0.0
nk=0.0
nv=0.0

def trial(teamname):
    buf=0;
    bk=0.0
    bv=0.0
    nk=0.0
    nv=0.0
    with open("datafrom_"+teamname) as f:
        content= f.readlines()
    while (buf<len(content)):
        t=content[buf]
        var=t.split('\t')
        odds=var[8].split()
        png=random.randint(0,1)
        if(len(odds)<5):
            lk=float(odds[0])
            lv=float(odds[1])
            rk=float(odds[2])
            rv=float(odds[3])
        else:
            print "errrr"
            print var
            print strt[0]
        #bet on team
        if (png==1):
            if(var[1]==teamname):
                if(var[5]=="1"):
                    bk+=4*lk
                    bv+=4*lv
                #print ("bet on VG, VG won")
                else:
                    bk+=4*rk
                    bv+=4*rv
            if(var[2]=="VG"):
                #print ("bet on VG, VG lost")
                bk-=4
                bv-=4

        #dont bet on team

        if(png==0):
            if(var[2]==teamname):
                if(var[5]=="1"):
                    bk+=4*lk
                    bv+=4*lv
                else:
                    bk+=4*rk
                    bv+=4*rv
                #print ("not bet on VG, VG lost")
            if(var[1]==teamname):
                #print ("not bet on VG, VG won")
                bk-=4
                bv-=4
        buf+=1
    global n
    global list_bk
    global list_bv
    list_bv.append(bv)
    list_bk.append(bk)
    n+=1


def team_ana(str_list):
    strt=str_list.split('\n')
    global bk
    global bv
    global nk
    global nv
    idx=0
    buf=0
    with open("datafrom_"+strt[0]) as f:
        content = f.readlines()
    while (buf<len(content)):
        idx=1
        t=content[buf]
        var=t.split('\t')
        if(var[2]!=strt[0] and var[1]!=strt[0]):
            buf+=1
            continue
        odds=var[8].split()
        if(len(odds)<5):

            lk=float(odds[0])
            lv=float(odds[1])
            rk=float(odds[3])
            rv=float(odds[2])
        else:
            print "errrr"
            print var
            print strt[0]


        if (var[1]==strt[0] and var[5]=="1"):
            #br+=int(var[8+idx])
            #bu+=int(var[9+idx])
            #bc+=int(intvar[10+idx])
            bk+=4*lk
            bv+=4*lv
            nk-=4
            nv-=4
        elif(var[1]==strt[0] and var[5]=="2"):
            #br+=int(var[13-idx])
            #bu+=int(var[12-idx])
            #bc+=int(var[11-idx])
            bk+=4*rk
            bv+=4*rv
            nk-=4
            nv-=4
        elif(var[2]==strt[0] and var[5]=="1"):
            bk-=4
            bv-=4
            nk+=lk
            nv+=lv
            #nr+=int(var[8+idx])
            #nu+=int(var[9+idx])
            #nc+=int(var[10+idx])

        elif(var[2]==strt[0] and var[5]=="2"):
            bk-=4
            bv-=4
            nk+=4*rk
            nv+=4*rv
            #nr+=int(var[13-idx])
            #nu+=int(var[12-idx])
            #nc+=int(var[11-idx])
            #print var[0],br,bu,bc,nr,nu,nc
        buf+=1

with open("complete_teamlist") as f:
    team_list = f.readlines()
team_idx=0
fileOUT=open("team_test",'w')
while (team_idx<len(team_list)):
    list_bv=[]
    list_bk=[]
    team_ana(team_list[team_idx])

    team_name=team_list[team_idx].split('\n')

    while (n<trial_counts):
        trial(team_name[0])
    bv_avg=np.average(list_bv)
    bk_avg=np.average(list_bk)
    bv_std=np.std(list_bv)
    bk_std=np.std(list_bk)
    print team_name[0],(bk-bk_avg)/bk_std,(bv-bv_avg)/bv_std,(nk-bk_avg)/bk_std,(nv-bv_avg)/bv_std,bk_avg/bk_std,bv_avg/bv_std
    fileOUT.write( team_name[0]+' '+str((bk-bk_avg)/bk_std)+' '+str((bv-bv_avg)/bv_std)+' '
            +str((nk-bk_avg)/bk_std)+' '+str((nv-bv_avg)/bv_std)+' '+str(bk_avg/bk_std)+' '+str(bv_avg/bv_std)+'\n')

    bv=0
    bk=0
    nk=0
    nv=0
    n=0
    team_idx+=1


