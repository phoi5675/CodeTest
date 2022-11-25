#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define MAX (100)
#define EMPTY (0)
#define FILLED (1)
int M, N, K; //세로크기, 가로크기, 직사각형 개수
int sx[MAX + 10];
int sy[MAX + 10];
int ex[MAX + 10];
int ey[MAX + 10];
bool map[MAX + 10][MAX + 10];
int sol[MAX * MAX]; //각 영역 넓이 저장용
int dt[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
typedef struct _node
{
    _node(int y, int x) : y(y), x(x){};
    int y;
    int x;
} node;
queue<node> Q;
void InputData()
{
    cin >> N >> M >> K;
    for (int i = 0; i < K; i++)
    {
        cin >> sx[i] >> sy[i] >> ex[i] >> ey[i];
    }
}
void OutputData(int ans)
{
    cout << ans << endl;
    for (int i = 0; i < ans; i++)
    {
        cout << sol[i] << " ";
    }
    cout << endl;
}
int bfs(int y, int x)
{
    int area = 1;
    map[y][x] = FILLED;
    Q.push(node(y, x));

    while (!Q.empty())
    {   
        node front = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++)
        {
            int ny = front.y + dt[i][0], nx = front.x + dt[i][1];
            if ((0 <= ny && ny < N) && (0 <= nx && nx < M) && map[ny][nx] == EMPTY)
            {
                area++;
                map[ny][nx] = FILLED;
                Q.push(node(ny, nx));
            }
        }
    }

    return area;
}
int traverse()
{
    int regions = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (map[i][j] == EMPTY)
            {
                sol[regions++] = bfs(i, j);
            }
        }
    }
    return regions;
}
void fill_map()
{
    for (int i = 0; i < K; i++)
    {
        for (int y = sy[i]; y < ey[i]; y++)
        {
            for (int x = sx[i]; x < ex[i]; x++)
            {
                map[y][x] = FILLED;
            }
        }
    }
}
void print_map()
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << map[i][j] << ' ';
        }
        cout << endl;
    }
}
int main(void)
{
    int ans = -1;
    InputData(); //입력받는 부분

    //여기서부터 작성
    fill_map();
    ans = traverse();
    sort(sol, sol + ans);
    OutputData(ans); //출력하는 부분
    return 0;
}
