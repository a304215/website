#include <stdio.h>
int main()
{
	int n;
	float c,r,f,value = 0,discount;
	scanf("%f",&f);
	scanf("%d",&n);
	scanf("%f",&c);
	scanf("%f",&r);
	int i,j;
	for(i = 1;i<=n;i++){
		discount = 1;
		for(j = 1;j<=i;j++){
			discount = discount/(1+r);
		}
	}
	value = value + discount*f*c;
	if(i==n){
		value = value+discount*f;
	}
	printf("%8.4f",value);
	return 0;
}
