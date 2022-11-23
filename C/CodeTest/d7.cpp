#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

#define EMPTY ('.')
#define FLOOD ('*')
#define ROCK ('X')
#define CAVE ('D')
#define ART ('S')

#define MAXN (50)
int vec[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
int R, C; //지도 세로, 가로 크기
char map[MAXN + 10][MAXN + 10];
bool visited[MAXN + 10][MAXN + 10];

typedef struct _node
{
    _node(int y, int x, int elapsed, char type)
        : y(y), x(x), elapsed(elapsed), type(type){};
    int y;
    int x;
    int elapsed;
    char type;
} node;

queue<node> Q;

void debug(node n)
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (n.type == ART && i == n.y && j == n.x)
            {
                cout << ART;
            }
            else
            {
                cout << map[i][j];
            }
        }
        cout << endl;
    }
    cout << endl;
}

void InputData()
{
    cin >> R >> C;
    for (int i = 0; i < R; i++)
    {
        cin >> map[i];
    }
}

void init()
{
    Q = queue<node>();
    memset(visited, 0, sizeof(visited));
}

void fill_init_queue(char type)
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (map[i][j] == type)
            {
                Q.push(node(i, j, 0, type));
            }
        }
    }
}

inline bool is_in_boundary(int y, int x)
{
    return (0 <= y && y < R) && (0 <= x && x < C);
}

int bfs()
{
    while (!Q.empty())
    {
        // debug(Q.front());
        node n = Q.front();
        Q.pop();

        if (map[n.y][n.x] == CAVE && n.type == ART)
        {
            return n.elapsed;
        }

        for (int i = 0; i < 4; i++)
        {
            int ny = vec[i][0] + n.y;
            int nx = vec[i][1] + n.x;

            if (is_in_boundary(ny, nx))
            {
                if ((n.type == FLOOD) && map[ny][nx] == EMPTY)
                {
                    map[ny][nx] = FLOOD;
                    Q.push(node(ny, nx, n.elapsed + 1, n.type));
                }
                else if ((n.type == ART) 
                    && (map[ny][nx] == EMPTY || map[ny][nx] == CAVE)
                    && !visited[ny][nx])
                {
                    visited[ny][nx] = true;
                    Q.push(node(ny, nx, n.elapsed + 1, n.type));
                }
            }
        }
    }
    return -1;
}
int main()
{
    int T, ans = -1;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++)
    {
        InputData(); //입력 받는 부분
        // 여기서부터 작성

        // 이전 테스트에서 사용한 전역 변수 초기화
        init();

        // 홍수, 사람 순서로 enqueue
        fill_init_queue(FLOOD);
        fill_init_queue(ART);

        ans = bfs();
        if (ans == -1)
            cout << "KAKTUS" << endl; //출력 하는 부분
        else
            cout << ans << endl;
    }
    return 0;
}
