#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;
#define MAXH (5)
#define MAXW (9)
#define INF ((int)1e9)

const char EMPTY = '.', SOL = 'o', WALL = '#';
char map[MAXH + 2][MAXW + 2];
int solremain, solmove = INF;
int init_remain;
const int dt[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
void InputData()
{
    for (int h = 0; h < MAXH; h++)
    {
        cin >> &map[h][0];
    }
}
void debug()
{
    for (int i = 0; i < MAXH; i++)
    {
        printf("%s\n", map[i]);
    }
    cout << endl;
}
int count_sols()
{
    int sols = 0;
    for (int i = 0; i < MAXH; i++)
    {
        for (int j = 0; j < MAXW; j++)
        {
            if (map[i][j] == SOL)
            {
                sols++;
            }
        }
    }
    return sols;
}
inline bool is_in_map(int y, int x)
{
    return (0 <= y && y < MAXH) && (0 <= x && x < MAXW);
}

void dfs(int remain, int move)
{
    // printf("%d\n", remain);
    if (remain <= solremain)
    {
        // printf("remain : %3d, moved : %3d\n", remain, move);
        solmove = move;
        solremain = min(solremain, remain);
    }
    if (remain == 1)
    {
        return;
    }
    for (int i = 0; i < MAXH; i++)
    {
        for (int j = 0; j < MAXW; j++)
        {
            if (map[i][j] == SOL)
            {
                for (int d = 0; d < 4; d++)
                {
                    int ny = i + dt[d][0], nx = j + dt[d][1];
                    int nny = i +  2 * dt[d][0], nnx = j + 2 * dt[d][1];
                    if (is_in_map(ny, nx) && is_in_map(nny, nnx)
                        && map[ny][nx] == SOL && map[nny][nnx] == EMPTY)
                    {
                        map[i][j] = EMPTY;
                        map[nny][nnx] = SOL;
                        map[ny][nx] = EMPTY;
                        // printf("moved\n");
                        // debug();
                        dfs(remain - 1, move + 1);
                        map[i][j] = SOL;
                        map[nny][nnx] = EMPTY;
                        map[ny][nx] = SOL;
                        // printf("rollback\n");
                        // debug();

                    }
                }
            }
        }
    }
}
int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++)
    {
        InputData(); //입력받는 부분

        //여기서부터 작성
        solremain = count_sols();
        dfs(solremain, 0);
        cout << solremain << " " << solmove << endl; //출력하는 부분
    }
    return 0;
}