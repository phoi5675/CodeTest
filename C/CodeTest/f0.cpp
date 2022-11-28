#include <iostream>
#include <algorithm>

using namespace std;

int N;
int W[20];
int ans = 0;
long long debug_ary[20];

void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> W[i];
    }
}
bool is_rounded(long long a, long long b)
{
    long long divider = 10;
    while (a && b)
    {
        long long left_1 = a % divider, left_2 = b % divider;
        if (left_1 + left_2 >= divider)
        {
            return true;
        }
        a /= divider;
        b /= divider;
    }
    return false;
}

void dfs(int level, int cows, long long weight_sum)
{
    if (cows > ans)
    {
        ans = cows;
    }
    if (level == N)
    {
        return;
    }

    for (int i = level; i < N; i++)
    {
        if (!is_rounded(weight_sum, W[i]))
        {
            debug_ary[level] = W[i];
            dfs(i + 1, cows + 1, weight_sum + W[i]);
        }
    }
}
int main()
{

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    dfs(0, 0, 0);
    cout << ans << endl; //출력하는 부분
    return 0;
}