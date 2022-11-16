#include <iostream>
#include <algorithm>

using namespace std;

enum PF
{
    E = 1,
    W,
    S,
    N
};

int K;
int A[6 + 10];
int B[6 + 10];
void InputData()
{
    cin >> K;
    for (int i = 0; i < 6; i++)
    {
        cin >> A[i] >> B[i];
    }
}

int rotate_right(int num)
{
    return (num + 1) % 6;
}
int rotate_left(int num)
{
    if (num == 0)
    {
        return 5;
    }
    else
    {
        return (num - 1) % 6;
    }
}

int main()
{
    int ans = -1;
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    int w_idx = 0, h_idx = 0;
    int w_max = 0, h_max = 0;
    for (int i = 0; i < 6; i++)
    {
        if (A[i] == E || A[i] == W)
        {
            w_max = max(w_max, B[i]);
            if (w_max == B[i])
            {
                w_idx = i;
            }
        }
        else
        {
            h_max = max(h_max, B[i]);
            if (h_max == B[i])
            {
                h_idx = i;
            }
        }
    }

    int main_area = w_max * h_max;
    int small_area = 0;

    // 작은 영역 구하기
    int h1, h2, w1, w2;
    // 가장 큰 둘레의 바로 옆에 붙어 있지 않은 둘레가 빈 공간
    h1 = B[rotate_left(w_idx)];
    h2 = B[rotate_right(w_idx)];

    w1 = B[rotate_left(h_idx)];
    w2 = B[rotate_right(h_idx)];

    int empty_width = 0, empty_height = 0;

    for (int i = 0; i < 6; i++)
    {
        if ((A[i] == E || A[i] == W) && (B[i] != w1 && B[i] != w2))
        {
           empty_width = B[i]; 
        }
        else if ((A[i] == N || A[i] == S) && (B[i] != h1 && B[i] != h2))
        {
            empty_height = B[i];
        }
    }

    small_area = empty_width * empty_height;
    ans = K * (main_area - small_area);

    cout << ans << '\n'; // 출력하는 부분
    return 0;
}