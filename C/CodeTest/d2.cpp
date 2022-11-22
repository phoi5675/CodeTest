#include <iostream>
#include <algorithm>

using namespace std;

#define MAXNM ((int)1e5)

typedef struct _grass
{
    long long start;
    long long end;
} grass;

int N, M;                //소마리수, 잔디구간 개수
grass g_ary[MAXNM + 10];
void InputData()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> g_ary[i].start >> g_ary[i].end;
    }
}

bool compare(grass first, grass second)
{
    return first.start < second.start;
}

bool is_possible(long long gap)
{
    int grass_idx = 0;
    long long offset = g_ary[grass_idx].start;
    long long cur_cow_pos = offset;
    for (int cow_idx = 0; cow_idx < N - 1; cow_idx++)
    {
        long long next_cow_pos = cur_cow_pos + gap;
        // gap이 커서 다음 소 위치가 잔디 사이인 경우 
        // 다음 잔디로 넘어가야 하는 경우, 다음 잔디의 시작지점으로 설정
        // gap이 충분히 커서 다음 잔디가 아닌 n번째 뒤의 잔디에 위치할 수도 있음
        while (!(g_ary[grass_idx].start <= next_cow_pos &&
            next_cow_pos <= g_ary[grass_idx].end))
        {
            // 새로운 잔디 범위에 있는 경우
            if ((g_ary[grass_idx].start <= next_cow_pos
                && next_cow_pos <= g_ary[grass_idx].end))
            {
                offset = g_ary[grass_idx].start - cur_cow_pos;
                break;
            }
            else if (next_cow_pos <= g_ary[grass_idx].start)
            {
                next_cow_pos = g_ary[grass_idx].start;
                break;
            }
            if (++grass_idx >= M)
            {
                return false;
            }
        }
        // 소 위치 업데이트 
        cur_cow_pos = next_cow_pos;
    }
    return true;
}

long long solve(long long left, long long right)
{
    long long res = 1;
    long long mid;
    while (left <= right)
    {
        // overflow 발생하지는 않겠지만, 혹시나 해서 overflow 방지
        mid = left + (right - left) / 2;
        if (is_possible(mid))
        {
            res = max(res, mid);
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
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long ans = 0;
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    // 우선 시작지점으로 정렬
    sort(g_ary, g_ary + M, compare);
    // right의 경우, 최댓값은 빈 공간 고려하지 않고, 소들을 일정한 간격으로 둔 경우
    // 모두 동일한 간격일 때, ans 값이 최대가 되므로 right으로 설정
    long long left = 0;
    long long right = g_ary[M - 1].end;

    ans = solve(left, right);

    cout << ans << "\n"; // 출력하는 부분
    return 0;
}