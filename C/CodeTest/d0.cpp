#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

#define MAXN ((int)1e6)
int N;              //마을 수
// int A[MAXN + 10]; //마을 위치
// int B[MAXN + 10]; //잡힌 물고기 양
int tmp[MAXN + 10];
typedef struct _node
{
    int pos;
    int fish;
} node;
node towns[MAXN + 10];
void InputData()
{
    scanf("%d", &N);
    for (int i = 0; i < N; i++)
    {
        scanf("%d %d", &towns[i].pos, &towns[i].fish);
    }
}

bool is_possible(int children)
{
    long long need = 0;
    for (int i = 0; i < N - 1; i++)
    {
        // 현재 마을에서 남은 물고기 계산 -> 음수인 경우 불가능한 조합
        need = need + towns[i].fish - children;
        if (need < 0)
        {
            need -= (towns[i + 1].pos - towns[i].pos);
        }
        else
        {
            need -= (towns[i + 1].pos - towns[i].pos);
            if (need < 0)
            {
                need = 0;
            }
        }
    }
    return (need + towns[N - 1].fish - children) >= 0;
}
int solve(int left, int right)
{
    int res = 1;
    while (left <= right)
    {
        int mid = (left + right) / 2;
        if (is_possible(mid))
        {
            res = mid;
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
        
    }
    return res;
}
int main()
{
    int ans = -1;
    InputData(); //입력받는 부분

    //여기서부터 작성
    int left = 0, right = 0;
    for (int i = 0; i < N; i++)
    {
        right = max(right, towns[i].fish);
    }

    ans = solve(left, right);
    cout << ans << endl; //출력하는 부분
    return 0;
}