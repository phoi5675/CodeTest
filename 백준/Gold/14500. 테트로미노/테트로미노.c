#include <stdio.h>

#define ARY_SIZE 501
#define TET_LEN 4
#define TETS_T_LEN 4
#define VEC_LEN 3
#define max(a, b) (a) > (b) ? (a) : (b)

typedef enum
{
    false,
    true
} bool;

int TETS[][2] = {{1, 0}, {0, 1}, {0, -1}};
int TETS_T[][3][2] = {
    {{-1, -1}, {-1, 0}, {-1, 1}},
    {{-1, -1}, {0, -1}, {1, -1}},
    {{1, -1}, {1, 0}, {1, 1}},
    {{-1, 1}, {0, 1}, {1, 1}}};
int res = 0;
int n, m;
bool visited[ARY_SIZE][ARY_SIZE] = {false};
int field[ARY_SIZE][ARY_SIZE] = {0};

void dfs(int y, int x, int level, int covered)
{
    if (level == TET_LEN)
    {
        res = max(res, covered);
        return;
    }

    for (int i = 0; i < VEC_LEN; i++)
    {
        int dy, dx, ny, nx;
        dy = TETS[i][0];
        dx = TETS[i][1];
        ny = y + dy;
        nx = x + dx;
        if ((0 <= ny && ny < n) && (0 <= nx && nx < m) && !visited[ny][nx])
        {
            visited[ny][nx] = true;
            dfs(ny, nx, level + 1, covered + field[ny][nx]);
            visited[ny][nx] = false;
        }
    }
}
int main(int argc, const char *argv[])
{
    scanf("%d %d", &n, &m);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf(" %d", &field[i][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            visited[i][j] = true;
            dfs(i, j, 1, field[i][j]);
            visited[i][j] = false;

            for (int test = 0; test < TETS_T_LEN; test++)
            {
                bool is_intact = true;
                int t_sum = field[i][j];

                for (int v = 0; v < VEC_LEN; v++)
                {
                    int ni, nj;
                    ni = i + TETS_T[test][v][0];
                    nj = j + TETS_T[test][v][1];
                    if ((0 <= ni && ni < n) && (0 <= nj && nj < m))
                    {
                        t_sum += field[ni][nj];
                    }
                    else
                    {
                        is_intact = false;
                        break;
                    }
                }
                if (is_intact)
                {
                    res = max(res, t_sum);
                }
            }
        }
    }
    printf("%d\n", res);
    return 0;
}
