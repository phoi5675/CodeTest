#include <iostream>
#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXN (10)
#define INF ((int)1e9)
#define NOT_VISITED (-1)
int N;
int cost[MAXN + 10][MAXN + 10];
int solpath[MAXN + 10]; //답 경로
int optimized_sum = INF;
int traversed[MAXN + 10];
bool visited[MAXN + 10];
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> cost[i][j];
        }
    }
}
void OutputData(int sol)
{
    cout << sol << endl;
    for (int i = 0; i < N; i++)
    {
        cout << solpath[i] << " ";
    }
    cout << endl;
}
bool dfs(int level, int sum)
{
    if (level == N)
    {
        // for (int i = 0; i < N; i++)
        // {
        //     cout << traversed[i] << '\t';
        // }
        // cout << sum << endl;
        if (sum < optimized_sum)
        {
            optimized_sum = sum;
            memcpy(solpath, traversed, sizeof(traversed));
            return true;
        }
        return false;
    }
    else if (sum >= optimized_sum)
    {
        return false;
    }

    for (int i = 0; i < N; i++)
    {
        if (traversed[level] == NOT_VISITED && !visited[i])
        {
            visited[i] = true;
            traversed[level] = i + 1;
            int next_sum = sum + cost[level][i];
            // cout << level << '\t' << cost[i][level] << " / ";
            dfs(level + 1, next_sum);
            traversed[level] = NOT_VISITED;
            visited[i] = false;
        }
    }
    return false;
}
int main()
{
    int ans = -1;

    InputData(); //입력받는 부분

    //여기서부터 작성
    for (int i = 0; i < N; i++)
    {
        traversed[i] = NOT_VISITED;
    }

    dfs(0, 0);
    ans = optimized_sum;
    OutputData(ans); //출력하는 부분
    return 0;
}
