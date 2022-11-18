#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define MAXN (100)
#define EMPTY (0)

int N; //색종이 수
int X[MAXN + 10];
int Y[MAXN + 10];
int paper[MAXN + 10][MAXN + 10];
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> X[i] >> Y[i];
    }
}

int main()
{
    int ans = 0;
    InputData(); //입력받는 부분

    //여기서부터 작성
    // 맵 초기화
    for (int i = 0; i < N; i++)
    {
        for (int y = Y[i]; y < Y[i] + 10; y++)
        {
            for (int x = X[i]; x < X[i] + 10; x++)
            {
                paper[y][x]++;
            }
        }
    }

    for (int uy = 0; uy < MAXN; uy++)
    {
        for (int ux = 0; ux < MAXN; ux++)
        {
            if (paper[uy][ux] == EMPTY)
            {
                continue;
            }
            for (int dy = 0; dy < MAXN; dy++)
            {
                for (int dx = 0; dx < MAXN; dx++)
                {
                    if (dx < ux || dy < uy || paper[dy][dx] == EMPTY)
                    {
                        continue;
                    }
                    int local_max = 0;
                    bool isEmpty = false;
                    for (int sq_y = uy; (sq_y <= dy && !isEmpty); sq_y++)
                    {
                        for (int sq_x = ux; (sq_x <= dx && !isEmpty); sq_x++)
                        {
                            if (paper[sq_y][sq_x] == EMPTY)
                            {
                                isEmpty = true;
                                break;
                            }
                            local_max++;
                        }
                    }
                    if (!isEmpty)
                    {
                        ans = max(ans, local_max);
                    }
                }
            }
        }
    }

    cout << ans << endl; //출력하는 부분
    return 0;
}