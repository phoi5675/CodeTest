#include <stdio.h>
typedef enum {false, true} bool;


int main(int argc, const char * argv[]) {
    int n, k;
    int coin[12];
    
    int usedCoin = 0;
    
    scanf("%d%d", &n, &k);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &coin[i]);
    }
    
    for (int i = n - 1; i >= 0; i--) {
        usedCoin += (k / coin[i]);
        k %= coin[i];
    }
    
    printf("%d", usedCoin);
    return 0;
}
