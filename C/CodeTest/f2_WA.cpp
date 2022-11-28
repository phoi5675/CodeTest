#include <iostream>
#include <cstring>
using namespace std;
#define MAXM (7)
int N; //임의의수
int WV[2][MAXM + 1];
int A; //하나당 추가 가치
int traversed[MAXM + 1];

int sol;              //가장 가치가 높은 수식의 수식 가치
int solcnt[MAXM + 1]; //사용횟수
void InputData()
{
    cin >> N;
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < MAXM; j++)
        {
            cin >> WV[i][j];
        }
    }
    cin >> A;
}
void OutputData()
{
    cout << sol << "\n";
    for (int i = 0; i < MAXM; i++)
    {
        cout << solcnt[i] << " ";
    }
    cout << "\n";
}
int calc()
{
    int numbers_used = 0;
    int sum = 0;
    for (int i = 0; i < MAXM; i++)
    {
        int score_idx = traversed[i] <= 4 ? 0 : 1;
        sum += traversed[i] * WV[score_idx][i];
        numbers_used += traversed[i];
        // cout << traversed[i] << ' ' << WV[score_idx][i] << " / ";
    }
    // cout << numbers_used;
    // cout << endl;
    sum += (A * numbers_used);
    return sum;
}
void dfs()
{
    // for (int i = 0; i < MAXM; i++)
    // {
    //     cout << traversed[i] << ' ';
    // }
    // cout << '\t';
    int score_sum = calc();
    // cout << score_sum;
    // cout << endl;
    if (score_sum > sol)
    {
        memcpy(solcnt, traversed, sizeof(traversed));
        sol = score_sum;
        // return;
    }

    for (int i = MAXM - 1; i > 0; i--)
    {
        if (traversed[i] == 0)
        {
            continue;
        }
        traversed[i - 1] += 2;
        traversed[i]--;
        dfs();
        traversed[i]++;
        traversed[i - 1] -= 2;
    }
}
void init_traversed()
{
    int leftover = N;
    for (int i = MAXM - 1; i >= 0; i--)
    {
        traversed[i] += (leftover / (1 << i));
        leftover = leftover % (1 << i);
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData(); //입력

    //여기서부터 작성
    init_traversed();
    dfs();

    OutputData(); //출력
    return 0;
}
