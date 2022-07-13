#include <stdio.h>
typedef enum {false, true} bool;

int ary[130][130];
int input;
int numOfBlue;
int numOfWhite;

void square(int width, int x, int y){
    bool isBlue = ary[y][x] == 1 ? true : false;
    bool fragmented = false;
    int corner = ary[y][x];
    int sqaure = width * width / 2;
    int halfWidth = width / 2;
    
    for (int i = 0; i < sqaure; i++) {
        int yAxis = i / width;
        int xAxis = i % width;
        
        if ((corner == ary[y + yAxis][x + xAxis]) && (corner == ary[y + halfWidth + yAxis][x + xAxis])) {
            continue;
        }
        else if (width > 1) {
            square(halfWidth, x, y);
            square(halfWidth, x + halfWidth, y);
            square(halfWidth, x, y + halfWidth);
            square(halfWidth, x + halfWidth, y + halfWidth);
            fragmented = true;
            break;
        }
    }
    
    if (!fragmented) {
        if (isBlue) {
            numOfBlue++;
        }
        else{
            numOfWhite++;
        }
    }
}

int main(int argc, const char * argv[]) {

    scanf("%d", &input);
    
    for (int i = 0; i < input; i++) {
        for (int j = 0; j < input; j++) {
            scanf("%d", &ary[i][j]);
        }
    }
    
    square(input, 0, 0);
    
    printf("%d\n%d", numOfWhite, numOfBlue);
    return 0;
}
