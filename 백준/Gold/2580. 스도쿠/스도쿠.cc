#include <iostream>
#include <vector>
#include <cstdio>

using namespace std;

#define MAXN (9)

int sudoku[MAXN][MAXN];
bool col[MAXN + 5][MAXN + 5];
bool row[MAXN + 5][MAXN + 5];
bool square[MAXN + 5][MAXN + 5];
struct POS
{
    POS(int y, int x) : y(y), x(x){};
    int y;
    int x;
};
vector<POS> empty_blocks;
void InputData()
{
    for (int r = 0; r < MAXN; r++)
    {
        for (int c = 0; c < MAXN; c++)
        {
            cin >> sudoku[r][c];
        }
    }
}
void OutputData()
{
    for (int r = 0; r < MAXN; r++)
    {
        for (int c = 0; c < MAXN; c++)
        {
            cout << sudoku[r][c] << " ";
        }
        cout << endl;
    }
}
int get_sq_idx(int y, int x)
{
    return 3 * (y / 3) + (x / 3);
}
bool dfs(int idx)
{
    if (idx == empty_blocks.size())
    {
        return true;
    }

    int y = empty_blocks[idx].y, x = empty_blocks[idx].x;

    int sq_idx = get_sq_idx(y, x);
    for (int k = 1; k <= 9; k++)
    {
        if (!square[sq_idx][k] && !row[y][k] && !col[x][k])
        {
            square[sq_idx][k] = true;
            row[y][k] = true;
            col[x][k] = true;
            sudoku[y][x] = k;
            if (dfs(idx + 1))
            {
                return true;
            }
            sudoku[y][x] = 0;
            square[sq_idx][k] = false;
            row[y][k] = false;
            col[x][k] = false;
        }
    }

    return false;
}

void init()
{
    for (int i = 0; i < MAXN; i++)
    {
        for (int j = 0; j < MAXN; j++)
        {
            int sq_idx = get_sq_idx(i, j);
            int block = sudoku[i][j];
            if (block)
            {
                // square
                square[sq_idx][block] = true;
                // row / col
                row[i][block] = true;
                col[j][block] = true;
            }
        }
    }

    // count empty cells
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (sudoku[i][j] == 0)
            {
                empty_blocks.push_back(POS(i, j));
            }
        }
    }
}
int main()
{
    InputData(); //입력받는 부분

    //여기서부터 작성
    init();

    dfs(0);
    OutputData(); //출력하는 부분
    return 0;
}