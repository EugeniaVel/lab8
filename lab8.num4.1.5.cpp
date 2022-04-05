#include <iostream>
#include <cmath>
using namespace std;
double df(double x,double y)
{
	double f;
	f=(-3*x*y+8*y-pow(x,2))/(pow(x,2)-5*x+6);
	return f;
}
double fx(double x)
{
	double f;
	f=(-0.25*pow(x,4)+(2/3)*pow(x,3)+12)/(pow(x-2,2)*(x-3));
	return f;
}
int main()
{
	setlocale(LC_ALL,"Russian");
	int i,n;
	double *y,*yr,*x,*k,h,xx,dy,eps;
	xx=1;
	h=0.1;
	n=xx/h+2;
	y=new double[n];
	yr=new double[n];
	x=new double[n];
	k=new double[4];
	y[0]=-1;
	x[0]=0;
	yr[0]=fx(x[0]);
	eps=abs(y[0]-yr[0]);
	cout<<"x0:"<<x[0]<<" y0:"<<y[0]<<" Погрешность:"<<eps<<"\n";
	for(i=1;i<n;i++)
	{
		x[i]=x[i-1]+h;
		k[0]=h*df(x[i-1],y[i-1]);
		k[1]=h*df(x[i-1]+0.5*h,y[i-1]+0.5*k[0]);
		k[2]=h*df(x[i-1]+0.5*h,y[i-1]+0.5*k[1]);
		k[3]=h*df(x[i-1]+h,y[i-1]+k[2]);
		dy=(k[0]+2*k[1]+2*k[2]+k[3])/6;
		y[i]=y[i-1]+dy;
		yr[i]=fx(x[i]);
		eps=abs(y[i]-yr[i]);
		cout<<"x"<<i<<":"<<x[i]<<" y"<<i<<":"<<y[i]<<" Погрешность:"<<eps<<"\n";
	}
}