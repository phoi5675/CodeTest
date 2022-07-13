#include <stdio.h>
#include <math.h>

void moveh(int from, int to) {
    printf("%d %d\n", from, to);
}

void hanoi(int n, int from, int by, int to) {
    if (n == 1) moveh(from, to);
    else {
        hanoi(n-1, from, to, by);
        moveh(from, to);
        hanoi(n-1, by, from, to);
    }
}

int main(void) {
    int i = 0;
    scanf("%d", &i);
    
    printf("%d\n", (int)pow(2, i) - 1);
    hanoi(i, 1, 2, 3);
}
