#include <iostream>
#include <queue>
using namespace std;

#define MAXN (100)
#define EMPTY ('0')
#define ZERGLING ('1')

typedef struct _node
{
    _node(int y, int x, int e) : y(y), x(x), elapsed(e) {};
    int y;
    int x;
    int elapsed;
} node;

int dt[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
int W, H;                       //지도의 가로 세로 크기
char map[MAXN + 10][MAXN + 10]; //지도 정보('1':저글링, '0':빈곳)
bool visited[MAXN + 10][MAXN + 10];
int sw, sh;                     //시작위치 가로 세로 좌표
queue<node> Q;

void InputData()
{
    cin >> W >> H;
    for (int i = 1; i <= H; i++)
    {
        cin >> &map[i][1];
    }
    cin >> sw >> sh;
}

int count_zerglings()
{
    int zerglings = 0;
    for (int i = 1; i <= H; i++)
    {
        for (int j = 1; j <= W; j++)
        {
            if (map[i][j] != EMPTY)
            {
                zerglings++;
            }
        }
    }
    return zerglings;
}

bool bfs(int &elapsed, int &zerglings)
{
    bool is_killed = false;

    while (!Q.empty() && zerglings > 0)
    {
        node front = Q.front();
        Q.pop();
        elapsed = front.elapsed;
        if (map[front.y][front.x] == ZERGLING)
        {
            is_killed = true;
            zerglings--;
        }

        for (int i = 0; i < 4; i++)
        {
            int dy = dt[i][0], dx = dt[i][1];
            int ny = front.y + dy, nx = front.x + dx;

            if ((1 <= ny && ny <= H) && (1 <= nx && nx <= W)
                && !visited[ny][nx] && map[ny][nx] == ZERGLING)
            {
                visited[ny][nx] = true;
                Q.push(node(ny, nx, front.elapsed + 1));
            }
        }
    }

    return is_killed;
}
int main()
{
    InputData(); //입력 받는 부분

    //여기서부터 작성
    int elapsed = 0;
    int zerglings = count_zerglings();

    Q.push(node(sh, sw, 0));
    visited[sh][sw] = true;
    int offset = bfs(elapsed, zerglings) == true ? 3 : 0;
    elapsed += offset;

    cout << elapsed << '\n';
    cout << zerglings << '\n';

    return 0;
}