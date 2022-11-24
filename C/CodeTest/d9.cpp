#include <iostream>
#include <queue>

using namespace std;

#define MAXN (102)
#define INF ((int)1e9)

int vec[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
int N;      //산크기
int eh, ew; //목적지 위치 세로, 가로
int map[MAXN + 10][MAXN + 10];
int visited[MAXN + 10][MAXN + 10];
int ans;

typedef struct _node
{
    _node(int y, int x) : y(y), x(x){};
    int y;
    int x;
} node;
queue<node> Q;
void InputData()
{
    cin >> N;
    cin >> eh >> ew;
    for (int h = 1; h <= N; h++)
    {
        for (int w = 1; w <= N; w++)
        {
            cin >> map[h][w];
            visited[h][w] = INF;
        }
    }
}
inline int energy(int from, int to)
{
    if (from == to)
    {
        return 0;
    }
    else if (from < to)
    {
        return (to - from) * (to - from);
    }
    else
    {
        return from - to;
    }
}
inline bool is_in_mountain(int y, int x)
{
    return (1 <= y && y <= N) && (1 <= x && x <= N);
}
void init_enqueue()
{
    for (int i = 0; i <= N + 1; i++)
    {
        for (int j = 0; j <= N + 1; j++)
        {
            if (i == 0 || i == N + 1 || j == 0 || j == N + 1)
            {
                Q.push(node(i, j));
            }
        }
    }
}
int bfs()
{
    while (!Q.empty())
    {
        node n = Q.front();
        Q.pop();
        for (int i = 0; i < 4; i++)
        {
            int ny = n.y + vec[i][0], nx = n.x + vec[i][1];
            if (is_in_mountain(ny, nx))
            {
                int energy_used = visited[n.y][n.x] + energy(map[n.y][n.x], map[ny][nx]);
                if (energy_used < visited[ny][nx])
                {
                    Q.push(node(ny, nx));
                    visited[ny][nx] = energy_used;
                }
            }
        }
    }
    return visited[eh][ew];
}
int main()
{
    InputData(); //입력 받는 부분

    //여기서부터 작성
    init_enqueue();

    ans = bfs();
    cout << ans << endl; //출력하는 부분
    return 0;
}