#include <stdio.h>

int main(){
	double rate1 = 0.008;
	int a,b;
	a = (rate1<0.01)&&(rate1>0.005);
	b = 0.005<rate1<0.01;
	printf("%d\n",a);
	printf("%d",b);
}
