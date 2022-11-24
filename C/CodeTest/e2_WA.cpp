#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

#define MAXN (100)
#define INF ((int)1e9)

typedef struct _node
{
    _node(int moved, int from, int m_from, int m_to) 
        : moved(moved), from(from)
    {
        mlen_pos = make_pair(m_from, m_to);
    };
    int moved;
    int from;
    int to;
    pair<int, int> mlen_pos;
} node;
int N, M;
int graph[MAXN + 10][MAXN + 10];
int visited[MAXN + 10][MAXN + 10];
int prev_ary[MAXN + 10][MAXN + 10];

queue<node> Q;
void InputData()
{
    cin >> N >> M;
    int from, to, dist;
    for (int i = 0; i < M; i++)
    {
        cin >> from >> to >> dist;
        if (dist < graph[from][to])
        {
            graph[from][to] = dist;
            graph[to][from] = dist;
        }
    }
}
void init(int ary[][MAXN + 10])
{
    for (int i = 0; i <= MAXN; i++)
    {
        for (int j = 0; j <= MAXN; j++)
        {
            ary[i][j] = INF;
        }
    }
}
void enqueue()
{
    for (int i = 2; i <= MAXN; i++)
    {
        if (graph[1][i] != INF)
        {
            Q.push(node(graph[1][i], i, 1, i));
        }
    }
}
node bfs()
{
    node ret = node(INF, 0, 0, 0);

    while (!Q.empty())
    {
        node front = Q.front();
        Q.pop();

        int from = front.from;
        for (int i = 0; i <= MAXN; i++)
        {
            if (graph[from][i] != INF && front.moved + graph[from][i] < visited[from][i])
            {
                prev_ary[from][i] = from;
                visited[from][i] = graph[from][i] + front.moved;
                int m_from = from, m_to = i;
                if (graph[m_from][m_to] < graph[front.mlen_pos.first][front.mlen_pos.second])
                {
                    m_from = front.mlen_pos.first;
                    m_to = front.mlen_pos.second;
                }
                node next = node(front.moved + graph[from][i], i, m_from, m_to);
                Q.push(next);
                if (i == N && next.moved <= ret.moved)
                {
                    ret = next;
                }
            }
        }
    }
    return ret;
}
int main()
{
    int ans = -1;
    init(graph);
    init(visited);
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    enqueue();
    node hay_pos = bfs();
    int h_from = hay_pos.mlen_pos.first, h_to = hay_pos.mlen_pos.second;
    graph[h_from][h_to] *= 2;
    // cout << h_from << ' ' << h_to << endl;
    init(visited);
    enqueue();
    node ret = bfs();
    ans = ret.moved - hay_pos.moved;

    // cout << ret.moved << '\t' << hay_pos.moved << endl;

    cout << ans << endl; // 출력하는 부분
    return 0;
}