#include<stdio.h>
#include<math.h>
int main(){
    double zerorate[5];
    double yield[5];
    double c,discount;
    printf("輸入每期之戶付債息\n");
    scanf("%1f",&c);
    for(int i = 0 ; i < 5;i++){
        printf("輸入yield rate %d:\n",i+1);
        scanf("%lf",&yield[i]);
    }
    zerorate[0] = yield[0];
    for(int i = 1; i<=4;i++){
        double bondvalue = 0;
        for(int j = 0;j<=i;j++){
            discount = 1/pow(1+yield[i],j+1);
            bondvalue = bondvalue+discount*c;
            if(j==i){
                bondvalue = bondvalue+discount*100;
            }
        }
        for (int j = 0 ; j <i;j++){
            double pv = c;
            pv = pv/pow(1+zerorate[j],j+1);
            bondvalue = bondvalue-pv;
        }
    zerorate[i] = pow((c+100)/bondvalue,1.0/(i+1))-1;
    }
    for(int i = 0;i<=4;i++){
        printf("第%d期zero rate=%f\n",i+1,zerorate[i]);
    }
}