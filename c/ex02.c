#include <stdio.h>
int main(){
	int x = 6;
	int y = 5;
	int output = (x>=5)&&y<10;
	printf("%d\n",output);
	output = !(x>10)+(!y);
	printf("%d\n",output);
	output = (!x)>10+!y;
	printf("%d\n",output);
}
