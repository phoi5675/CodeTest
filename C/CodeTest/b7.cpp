#include <iostream>
#include <algorithm>
using namespace std;
#define MAXN ((int)1e5)
int N; //영화수
struct DATA
{
    int s, e;
};
DATA A[MAXN + 10];
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i].s >> A[i].e;
    }
}
bool compare(DATA first, DATA second)
{
    if (first.e < second.e)
    {
        return true;
    }
    else if (first.e == second.e)
    {
        return (first.e - first.s) < (second.e - second.s);
    }
    else
    {
        return false;
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int ans = 0;
    InputData(); //입력받는 부분

    //여기서부터 작성
    sort(A, A + N, compare);

    DATA prev_movie;

    prev_movie = A[0];
    int first_watched = 0;
    // 2시간 이상인 첫 번째 영화 찾기
    while (first_watched < N && A[first_watched].e - A[first_watched].s < 2)
    {
        first_watched++;
    }
    // 본 영화가 한 개도 없는 경우(2시간 미만 영화만 존재)
    if (first_watched >= N)
    {
        cout << 0 << '\n';
        return 0;
    }
    prev_movie = A[first_watched];
    ans++;
    for (int i = first_watched + 1; i < N; i++)
    {
        // 2시간 미만 영화 제외
        if (A[i].e - A[i].s < 2 || A[i].s < prev_movie.e)
        {
            continue;
        }
        if (prev_movie.e <= A[i].s)
        {
            prev_movie = A[i];
            ans++;
        }
    }

    cout << ans << "\n"; //출력하는 부분
    return 0;
}
