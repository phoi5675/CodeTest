#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;

#define MAXN (100)
#define INF ((int)1e9)
int L;                //정비를 받지 않고 갈수있는 최대거리
int N;                //정비소 개수
int dist[MAXN + 10];  //정비소사이거리
int times[MAXN + 10]; //정비시간

typedef struct _vnode
{
    _vnode()
    {
        repaired_time_sum = INF;
        visited_shops = queue<int>();
    }
    int repaired_time_sum;
    queue<int> visited_shops;
} vnode;

vnode visited[MAXN + 10];
queue<int> Q;
void InputData()
{
    cin >> L;
    cin >> N;
    for (int i = 1; i <= N + 1; i++)
    {
        cin >> dist[i];
    }
    for (int i = 1; i <= N; i++)
    {
        cin >> times[i];
    }
}

void init_enqueue()
{
    int dist_sum = 0;
    visited[0].repaired_time_sum = 0;
    for (int i = 1; i <= N; i++)
    {
        dist_sum += dist[i];
        if (dist_sum <= L)
        {
            Q.push(i);
            visited[i].repaired_time_sum = times[i];
            visited[i].visited_shops.push(i);
        }
        else
        {
            return;
        }
    }
}
void bfs()
{
    while (!Q.empty())
    {
        int cur = Q.front();
        Q.pop();

        int dist_sum = 0;
        for (int i = cur + 1; i <= N + 1; i++)
        {
            dist_sum += dist[i];
            if (dist_sum > L)
            {
                break;
            }
            if (visited[cur].repaired_time_sum + times[i] < visited[i].repaired_time_sum)
            {
                visited[i].repaired_time_sum = visited[cur].repaired_time_sum + times[i];

                visited[i].visited_shops = queue<int>(visited[cur].visited_shops);
                visited[i].visited_shops.push(i);
                Q.push(i);
            }
        }
    }
}
int main()
{
    InputData(); //입력 받는 부분

    //여기서부터 작성
    // 한 번에 도착할 수 있는 경우 계산
    // 정비소는 N번째에 위치했기 때문에, N도 루프에 포함
    int dist_sum = 0;
    for (int i = 1; i <= N + 1; i++)
    {
        dist_sum += dist[i];
    }
    if (dist_sum <= L)
    {
        cout << 0 << endl;
        return 0;
    }

    init_enqueue();
    bfs();

    cout << visited[N + 1].repaired_time_sum << '\n';
    cout << visited[N + 1].visited_shops.size() - 1 << '\n';
    queue<int> printQ = visited[N + 1].visited_shops;

    while (!printQ.empty())
    {
        int front = printQ.front();
        if (front != N + 1)
        {
            cout << front << ' ';
        }
        printQ.pop();
    }
    cout << '\n';

    return 0;
}