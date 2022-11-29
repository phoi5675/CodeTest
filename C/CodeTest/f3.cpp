#include <iostream>
#include <algorithm>
using namespace std;
#define MAXW (20)
int N; //도로의 개수
int W; //사건의 개수
struct POS
{
    int r, c; //세로, 가로
};
POS pos[MAXW + 10]; //사건 좌표

POS p1, p2;
int ans = (int)1e9;
void InputData()
{
    cin >> N;
    cin >> W;
    for (int i = 0; i < W; i++)
    {
        cin >> pos[i].r >> pos[i].c;
    }
}
int get_dist(POS police, POS case_pos)
{
    return abs(case_pos.r - police.r) + abs(case_pos.c - police.c);
}
void dfs(int case_num, int moved)
{
    if (moved > ans)
    {
        return;
    }
    if (case_num == W)
    {
        // cout << moved << '\t';
        ans = min(ans, moved);
        return;
    }
    int p1_dist = get_dist(p1, pos[case_num]);
    int p2_dist = get_dist(p2, pos[case_num]);

    POS prev = p1;
    p1 = pos[case_num];
    dfs(case_num + 1, moved + p1_dist);
    p1 = prev;

    prev = p2;
    p2 = pos[case_num];
    dfs(case_num + 1, moved + p2_dist);
    p2 = prev;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    InputData(); //입력받는 부분

    //여기서부터 작성
    p1.r = 1, p1.c = 1;
    p2.r = N, p2.c = N;

    dfs(0, 0);
    cout << ans << "\n"; //출력하는 부분
    return 0;
}