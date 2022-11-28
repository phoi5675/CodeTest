#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

#define MAXN (20)
#define INF ((int)1e9)
int N, B;
int H[MAXN + 10];
int presum[MAXN + 10];
int ans;
void InputData()
{
    cin >> N >> B;
    for (int i = 1; i <= N; i++)
    {
        cin >> H[i];
    }
}

bool dfs(int level, int sum)
{
    // cout << level << '\t' << sum << endl;
    if (B > sum + presum[N] - presum[level - 1])
    {
        return false;
    }
    if (sum - B >= 0)
    {
        if (ans > sum - B)
        {
            ans = sum - B;
            // cout << sum << '\t';
            if (ans == 0){
                return true;
            }
        }
        return false;
    }
    for (int i = level; i <= N; i++)
    {
        if (dfs(i + 1, sum + H[i]))
        {
            return true;
        }
    }
    return false;
}
void init()
{
    ans = INF;
    for (int i = 1; i <= N; i++)
    {
        presum[i] = presum[i - 1] + H[i];
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
        init();
        dfs(1, 0);
        cout << ans << endl;
    }
    return 0;
}
