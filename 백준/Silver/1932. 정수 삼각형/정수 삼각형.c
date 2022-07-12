#include <stdio.h>
typedef enum {false, true} bool;

int ary[510][510];
int memoMax[510][510];
int depth;
int MAX;

int max(int a, int b){
    return (a > b) ? a : b;
}
void dp(int level, int aryIndex){
    int prevLevel = level - 1;
    
    if (level == 1) {
        return;
    }
    
    if (aryIndex == 0) {
        if (memoMax[prevLevel][aryIndex] == 0) {
            dp(prevLevel, aryIndex);
        }
        memoMax[level][aryIndex] = ary[level][aryIndex] + memoMax[prevLevel][aryIndex];
    }
    else if (aryIndex == level) {
        if (memoMax[prevLevel][aryIndex - 1] == 0) {
            dp(prevLevel, aryIndex - 1);
        }
        memoMax[level][aryIndex] = ary[level][aryIndex] + memoMax[prevLevel][aryIndex - 1];
    }
    else {
        if (memoMax[prevLevel][aryIndex - 1] == 0) {
            dp(prevLevel, aryIndex - 1);
        }
        else if (memoMax[prevLevel][aryIndex] == 0) {
            dp(prevLevel, aryIndex);
        }
        memoMax[level][aryIndex] =
            ary[level][aryIndex] + max(memoMax[prevLevel][aryIndex], memoMax[prevLevel][aryIndex - 1]);
    }
}

int main(int argc, const char * argv[]) {

    scanf("%d", &depth);
    
    for (int i = 0; i <= depth; i++) {
        for (int j = 0; j < i; j++) {
            scanf("%d", &ary[i][j]);
        }
    }
    
    memoMax[1][0] = ary[1][0];
    for (int i = 0; i < depth; i++) {
        dp(depth, i);
        
        if (memoMax[depth][i] > MAX) {
            MAX = memoMax[depth][i];
        }
    }
    
    printf("%d\n", MAX);
    
    return 0;
}
