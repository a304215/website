#include <stdio.h>
int main(){
	int a = 0 ;
	int b = 0 ;
	int c = 0;
	int count = 0;
	scanf("%d",&a);
	scanf("%d",&b);
	scanf("%d",&c);
	if(a>0.01){
		count +=1;
	}
	if(b>0.01){
		count+=1;
	}
	if(c > 0.01){
		count+=1;
	}
	float sum = 0 ;
	if(count>=2){
		sum = (float)count/2*100.5;
		printf("%f",sum);
	}
	
	return 0;
}
