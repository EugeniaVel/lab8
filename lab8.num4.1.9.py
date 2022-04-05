def df(x,y):
    dy=(y**2+x**2*y)/x**3
    return dy
def f(x):
    fx=x**2/(1+x)
    return fx
def adam(y,ff,i,h):
    ad=(y[i-1])+((h/24)*(55*ff[i-1]-59*ff[i-2]+37*ff[i-3]-9*ff[i-4]))
    return ad
def cor(y,ff,i,h):
    cr=y[i-1]+(h/24)*(9*ff[i]+19*ff[i-1]-5*ff[i-2]+ff[i-3])
    return cr
h=0.1
n=int(1/h)+1
x=[1]
y=[0.5]
eps=[]
toch=[]
fp=[0]
k=[0,0,0,0]
toch.append(f(x[0]))
fp.append(df(x[0],y[0]))
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
    fp.append(df(x[i],y[i]))
    toch.append(f(x[i]))
    eps.append(abs(toch[i]-y[i]))
for i in range(4,n):
    yy=adam(y,fp,i,h)
    y.append(yy)
    fp.append(df(x[i],y[i]))
    y[i]=cor(y,fp,i,h)
    toch.append(f(x[i]))
    eps.append(abs(toch[i]-y[i]))
for i in range(n):
    print("y"+str(i)+":"+str(round(y[i],9))+" x"+str(i)+":"+str(x[i]))
print("Погрешность решения при каждом шаге:")
for i in range(n):
    print("eps"+str(i)+":"+str(eps[i]))