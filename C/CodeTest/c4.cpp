#include <iostream>
#include <string>
#include <queue>
using namespace std;

#define MAXN ((int)1e4)
#define INF ((int)1e9)
#define L (0)
#define R (1)
const string LEFT = "left";
typedef struct _customer
{
    _customer(int idx, int arrived) : idx(idx), arrived(arrived) {};
    int idx;
    int arrived;
} customer;

int M, T, N; //배에태울수있는수, 배이동시간, 손님수
int arrived[MAXN + 10];

queue<customer> q[2];
queue<customer> boat_q;

int getIdx(char *str)
{
    return LEFT.compare((string)str) == 0 ? L : R;
}
int change_pos(int pos)
{
    return pos == L ? R : L;
}

void InputData()
{
    int arrived;
    cin >> M >> T >> N;
    for (int i = 0; i < N; i++)
    {
        char side[10];
        cin >> arrived >> side;
        q[getIdx(side)].push(customer(i, arrived));
    }
}
void OutputData()
{
    for (int i = 0; i < N; i++)
    {
        cout << arrived[i] << "\n";
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    InputData(); //입력받는 부분

    //여기서부터 작성
    int pos = L;
    int elapsed = 0;
    const int CAPA = M;
    const int TRANSIT_TIME = T;

    while (q[L].size() || q[R].size())
    {
        // 4. 기다리던 손님이 없는 경우
        if (q[pos].empty() || (!q[pos].empty() && q[pos].front().arrived > elapsed))
        {
            int other_side = change_pos(pos);
            int cur_side_arrived = q[pos].empty() ? INF : q[pos].front().arrived;
            int other_side_arrived = q[other_side].empty() ? INF : q[other_side].front().arrived;
            // 현재 정박중인 정박장에 올 손님과, 반대편 정박장에 올 손님 중 누가 먼저 오는지 계산
            if (cur_side_arrived <= other_side_arrived)
            {
                elapsed = cur_side_arrived;
            }
            else
            {
                // 반대편에 손님이 먼저 도착해서 반대편으로 가는 경우에는 이동시간도 추가해야 함
                if (elapsed >= other_side_arrived)
                {
                    elapsed += TRANSIT_TIME;
                }
                else
                {
                    elapsed = other_side_arrived + TRANSIT_TIME;
                }
                pos = other_side;
            }
        }
        // 1. 현재 정박한 정박장에서 손님 싣기
        while (!q[pos].empty() && boat_q.size() < CAPA)
        {
            customer c = q[pos].front();
            if (elapsed >= c.arrived)
            {
                q[pos].pop();
                boat_q.push(c);
                // string s = pos == L ? "left " : "right ";
                // cout << c.idx << " at " << s << elapsed << " boat capa : " << boat_q.size() << '\n';
            }
            else
            {
                break;
            }
        }
        // 2. 정박장 변경
        if (!boat_q.empty())
        {
            pos = change_pos(pos);
            elapsed += TRANSIT_TIME;
        }
        // 3. 도착 후 손님 내리기
        while (!boat_q.empty())
        {
            customer c = boat_q.front();
            boat_q.pop();
            arrived[c.idx] = elapsed;
        }
    }
    OutputData(); //출력하는 부분
    return 0;
}
