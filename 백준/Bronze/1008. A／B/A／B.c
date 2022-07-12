#include <stdio.h>
int main(){
    int a, b;
    scanf("%d%d", &a, &b);
    
    printf("%.9lf", (double)a / (double)b);
    return 0;
}
