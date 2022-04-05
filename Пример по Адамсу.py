import math
def df(x,y):
    dy=(y+x)**2
    return dy
def f(x):
    fx=math.tan(x)-x
    return fx
def adam(y,i):
    ad=(y[i-1])+((h/24)*(55*y[i-1]-59*y[i-2]+37*y[i-3]-9*y[i-4]))
    return ad
def cor(y,ff,i):
    cr=y[i-1]+(h/24)*(9*ff[i]+19*ff[i-1]-5*ff[i-2]+ff[i-3])
    return cr
h=0.1
n=int(1/h)+1
x=[0]
y=[0]
eps=[]
toch=[]
fp=[0]
k=[0,0,0,0]
toch.append(f(x[0]))
eps.append(abs(toch[0]-y[0]))
for i in range(n):
    x.append(round(x[i]+h,1))
for i in range(1,4):
    k[0]=h*df(x[i-1],y[i-1]);
    k[1]=h*df(x[i-1]+0.5*h,y[i-1]+0.5*k[0])
    k[2]=h*df(x[i-1]+0.5*h,y[i-1]+0.5*k[1])
    k[3]=h*df(x[i-1]+h,y[i-1]+k[2])
    dy=(k[0]+2*k[1]+2*k[2]+k[3])/6;
    y.append(y[i-1]+dy)
    fp.append(y[i])
    toch.append(f(x[i]))
    print(y[i],toch[i])
for i in range(4,n):
    yy=adam(y,i)
    y.append(yy)
    fp.append(df(x[i],y[i]))
    y[i]=cor(y,fp,i)
    toch.append(f(x[i]))
    print(y[i],toch[i])