import math
def df(x,y):
    dx=-y+math.exp(x)
    return dx
def f(x):
    fx=math.exp(x)/2+math.exp(-x)
    return fx
h=0.1
y=[1.5]
x=[0]
n=1+int(1/h)
toch=[]
eps=[]
toch.append(f(x[0]))
eps.append(abs(toch[0]-y[0]))
print(eps[0])
for i in range(n):
    x.append(round(x[i]+h,10))
for i in range(1,n):
    yy=h*df(x[i-1],y[i-1])
    y.append(yy+y[i-1])
    toch.append(f(x[i]))
    eps.append(abs(toch[i]-y[i]))
print("Численное решение дифференциального уравнения:")
for i in range(n):
    print("y"+str(i)+":"+str(round(y[i],5))+" x"+str(i)+":"+str(x[i]))
print("Погрешность решения при каждом шаге:")
for i in range(n):
    print("eps"+str(i)+":"+str(eps[i]))