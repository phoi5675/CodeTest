#include <iostream>

using namespace std;

#define MAX_N (100000)

int N, M;
int need[MAX_N];

bool isPossible(int m)
{
    int sum = m;
    int cnt = 1;
    for (int i = 0; i < N;)
    {
        if (sum < need[i])
        {
            if (++cnt > M)
                return false;
            sum = m;
        }
        else
        {
            sum -= need[i];
            i++;
        }
    }
    return true;
}
int Solve()
{
    int s = 0, e = 0, sol = 0;
    for (int i = 0; i < N; i++)
    {
        if (s < need[i])
            s = need[i];
        e += need[i];
    }
    while (s <= e)
    {
        int m = (s + e) / 2;
        if (isPossible(m))
        {
            sol = m;
            e = m - 1;
        }
        else
        {
            s = m + 1;
        }
    }
    return sol;
}

void Input_Data()
{
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        cin >> need[i];
    }
}

int main()
{
    ios_base::sync_with_stdio();
    cin.tie(nullptr);
    cout.tie(nullptr);
    int sol = -1;

    // 입력 받는 부분
    Input_Data();

    sol = Solve(); // 여기서부터 작성

    // 출력하는 부분
    cout << sol << '\n';

    return 0;
}