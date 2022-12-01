#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
#define MAXN ((int)1e5)
int N;
int X[MAXN + 10];
int Y[MAXN + 10];
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
    int ans = (int)1e9;

    InputData(); //입력받는 부분

    //여기서부터 작성
    int default_dist = 0;
    // 모든 체크포인트 다 들린 경우 계산
    for (int i = 1; i < N; i++)
    {
        default_dist += (abs(X[i] - X[i - 1]) + abs(Y[i] - Y[i - 1]));
        // printf("%d\t%d\t%d\t%d\n", X[i], abs(X[i] - X[i - 1]), abs(Y[i] - Y[i - 1]), default_dist);
    }
    ans = default_dist;
    for (int i = 1; i < N - 1; i++)
    {
        ans = min(ans, 
            default_dist 
            - (abs(X[i - 1] - X[i]) + abs(Y[i - 1] - Y[i])
                + abs(X[i] - X[i + 1]) + abs(Y[i] - Y[i + 1]))
            + (abs(X[i - 1] - X[i + 1]) + abs(Y[i - 1] - Y[i + 1])));
    }
    cout << ans << endl; //출력하는 부분
    return 0;
}
