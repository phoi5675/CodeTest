#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAXN (100)
int A;
int N;
int W[MAXN + 10];
int ans;
void InputData()
{
    cin >> A >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> W[i];
    }
}
void dfs(int level, int skills_used, int points)
{
    // cout << points << ' ';
    if (level >= N)
    {
        ans = min(ans, skills_used);
        return;
    }
    if (skills_used >= ans)
    {
        return;
    }

    // 물방울 합칠 수 있는 경우
    if (points > W[level])
    {
        dfs(level + 1, skills_used, points + W[level]);
    }
    else 
    {
        // 물방울 한 개 새로 생성하면 합칠 수 있는 경우
        // 새로 생성하는 경우에는 생성한 물방울을 합쳐야 하므로 level을 이동하지 않음
        if(points > 1)
        {
            dfs(level, skills_used + 1, points + (points - 1));
        }
        // 물방울 제거해야 하는 경우
        dfs(level + 1, skills_used + 1, points);
    }
}
int main()
{
    int t, T;
    cin >> T;
    for (t = 1; t <= T; t++)
    {
        InputData(); //입력받는 부분

        //여기서부터 작성
        ans = N;
        // 오름차순 정렬
        sort(W, W + N);
        dfs(0, 0, A);
        cout << "Case #" << t << ": " << ans << endl; //출력하는 부분
    }
    return 0;
}