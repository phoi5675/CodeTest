#include <stdio.h>

typedef enum {false, true} bool;

int N, M;
int MAX = -2000000000;
int MIN = 2000000000;
int ary[12];
int opTree[11];
int convertedOpAry[11];
bool visited[11];
int opAry[4];

int calculateWithInt(int sel, int a, int b){
    switch (sel) {
        case 1:
            return a + b;
            break;
        case 2:
            return a - b;
            break;
        case 3:
            return a * b;
            break;
        case 4:
            return a / b;
            break;
        default:
            return a / (long)b;
            break;
    }
}
void convertToFullAry(){
    int index = 0;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < opAry[i]; j++) {
            convertedOpAry[index++] = i + 1;
        }
    }
}
void dfs(int count){
    // count = current level, M = max level, N = range of leaf
    if(count == M){
        int i = 0;
        int temp = ary[i];
        for (i = 0; i < M; i++){
            temp = calculateWithInt(opTree[i], temp, ary[i + 1]);
        }
        
        if(temp >= MAX){
            MAX = temp;
        }
        if(temp <= MIN){
            MIN = temp;
        }
    }

    for (int i = 1; i <= N; i++){
        if (!visited[i]){
            // i = value of current node
            visited[i] = true;
            opTree[count] = convertedOpAry[i - 1];
            dfs(count + 1);
            visited[i] = false;
        }
    }
}
int main(int argc, const char * argv[]) {
    // 부분중복순열을 이용하는 문제 -> dfs
    int input;
    
    scanf("%d", &input);
    
    for (int i = 0; i < input; i++) {
        scanf("%d", &ary[i]);
    }
    for (int i = 0; i < 4; i++) {
        scanf("%d", &opAry[i]);
    }
    
    convertToFullAry();
    
    M = input - 1;
    N = M;
    
    dfs(0);
    
    printf("%d\n%d\n", MAX, MIN);
    
    return 0;
}
