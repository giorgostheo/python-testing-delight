from random import randint
s=0
b=[]

checker =  False


for i in range (10):
    for j in range (20):
       b.append([i,j])


while (checker ==False):
    d=randint(0,8)
    for k in range (19,0,1):
        if (k==1):
            checker ==True
            break
        if (b[d],[k]==0 and [d+1],[k]==0):
            b[d][k]=b[d][k] +1
            b[d][k+1]=b[d][k+1] +1
            b[d][k+2]=b[d][k+2] +1
            b[d+1][k]=b[d+1][k] +1
            s=s+1
            break


print s
#for i in range (10):
    #for j in range (20):
        #print b[i],[j]
