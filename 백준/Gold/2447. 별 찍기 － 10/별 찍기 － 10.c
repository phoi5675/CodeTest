#include <stdio.h>
int stars[2188][2188];
int input;
void blank(int n){
    for (int i = 0; i < input; i++) {
        for (int j = 0; j < input; j++) {
            if ((n/3 <= i%n && i%n < (2*n)/3) && (n/3 <= j%n && j%n < (2*n)/3)) {
                stars[i][j] = 1;
            }
        }
    }
    
    if (n > 3) {
        blank(n / 3);
    }
}

int main(){
    scanf("%d", &input);
        
    blank(input);
    
    for (int i = 0; i < input; i++) {
        for (int j = 0; j < input; j++) {
            if (stars[i][j] == 1) {
                printf(" ");
            }
            else{
                printf("*");
            }
        }
        printf("\n");
    }
    return 0;
}
