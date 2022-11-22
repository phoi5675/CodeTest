#include <iostream>
#include <algorithm>

using namespace std;

#define MAXN ((int)1e5)
#define THOLD(x) ((x) * 0.9)

int N; //개수
int F[MAXN + 10];

void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> F[i];
    }
}

int solve(int left, int right, int cur_size)
{
    int res = 0;
    int mid;
    while (left <= right)
    {
        mid = (left + right) / 2;
        if (THOLD(F[mid]) <= cur_size)
        {
            left = mid + 1;
            res = mid;
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long ans = 0;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    // 오름차순 정렬
    sort(F, F + N);
    for (int i = 0; i < N - 1; i++)
    {
        int left = i + 1, right = N - 1;
        // 작은 파일 크기 < (본인 다음 큰 파일 크기) * 0.9인 경우 제외
        if (F[i] < THOLD(F[left]))
        {
            continue;
        }
        int max_idx = solve(left, right, F[i]);
        ans += (max_idx - i);
    }
    cout << ans << "\n"; // 출력하는 부분
    return 0;
}