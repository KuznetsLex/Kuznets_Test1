f = open('mat_dv.txt')
parallel={}
winnersa={}
winnersg={}
max=0
maxa=0
maxg=0

for i in f:
    l=i.split()
    maximum=int(l[3])+int(l[4])



    if maximum>=max:
        max=maximum
        name=l[0]+' '+l[1]
        parallel[int(l[2])]=name+' '+str(max)





    if int(l[3])>=maxa:
        maxa=int(l[3])
        name=l[0]+' '+l[1]
        winnersa[int(l[2])]=name+' '+str(maxa)




    if int(l[4])>=maxg:
        maxg=int(l[4])
        name=l[0]+' '+l[1]
        winnersg[int(l[2])]=name+' '+str(maxg)


print('Победители в 8 -',parallel.get(8),';            Победители в 9 -',parallel.get(9),';            Победители в 10 -',parallel.get(10),';              Победители в 11 -',parallel.get(11))
print('Победители алгебры в 8 -',winnersa.get(8),';     Победители алгебры в 9 -',winnersa.get(9),';     Победители алгебры в 10 -',winnersa.get(10),';     Победители алгебры в 11 -',winnersa.get(11))
print('Победители геометрии в 8 -',winnersg.get(8),';   Победители геометрии в 9 -',winnersg.get(9),';       Победители геометрии в 10 -',winnersg.get(10),';     Победители геометрии в 11 -',winnersg.get(11))
