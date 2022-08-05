#include <stdio.h>

#define MAP_SIZE 500 + 1
#define VEC_LEN 4

typedef enum
{
    false,
    true
} bool;

int VEC[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

int board[MAP_SIZE][MAP_SIZE];
int dp[MAP_SIZE][MAP_SIZE];
int n, m;

int dfs(int y, int x)
{
    if (y == n - 1 && x == m - 1)
    {
        return 1;
    }
    if (dp[y][x] != -1){
        return dp[y][x];
    }
    
    dp[y][x] = 0;
    
    for (int i = 0; i < VEC_LEN; i++)
    {
        int ny, nx;
        ny = y + VEC[i][0];
        nx = x + VEC[i][1];

        if (0 <= ny && ny < n && 0 <= nx && nx < m && board[y][x] > board[ny][nx])
        {
            dp[y][x] += dfs(ny, nx);
        }
    }
    return dp[y][x];
}

int main()
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf(" %d", &board[i][j]);
            dp[i][j] = -1;
        }
    }
    printf("%d\n", dfs(0, 0));
    return 0;
}
