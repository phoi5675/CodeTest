#include <stdio.h>
#include <string.h>
#include <math.h>
typedef enum {false, true} bool;

void charToNum(char * input, int output[], char op[]){
    int numIndex = 0;
    int tempIndex = 0;
    char temp[10];
    
    for (int i = 0; i < strlen(input); i++) {
        if (input[i] != '+' && input[i] != '-') {
            temp[tempIndex++] = input[i];
        }
        
        // 연산자 집어넣기 / 숫자 변환
        if (input[i] == '+' || input[i] == '-' || i == strlen(input) - 1) {
            for (int j = 0; j < tempIndex; j++) {
                output[numIndex] += (temp[j] - '0') * (int)pow(10, tempIndex - j - 1);
                temp[j] = '0';
            }
            numIndex++;
            tempIndex = 0;
            
            op[numIndex] = (input[i] == '+') ? '+' : (input[i] == '-') ? '-' : '\0';
        }
    }
}
int calculate(int num[], char op[]){
    int res = 0;
    int temp = 0;
    bool braketOpen = false;
    
    for (int i = 0; i < strlen(op); i++) {
        if (op[i] == '-') {
            // braketOpen = braketOpen ? false : true; // 열려 있으면 닫고, 닫혀 있으면 괄호 열기
            braketOpen = true;
        }

        if (braketOpen) {
            temp += num[i];
        }
        else {
            res += num[i];
        }
    }
    return res - temp;
}
int main(int argc, const char * argv[]) {
    char input[100];
    char op[100] = {'0'};
    int num[100] = {0};
    
    scanf("%s", input);
    
    charToNum(input, num, op);
    
    printf("%d", calculate(num, op));
    
    return 0;
}
