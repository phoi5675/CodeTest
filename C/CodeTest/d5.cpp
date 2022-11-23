#include <iostream>
#include <queue>

using namespace std;

#define BLUE        ('B')
#define RED         ('R')
#define WALL        ('#')
#define GOAL        ('H')
#define EMPTY       ('.')
#define MAXN        (15)

int R, C;                     //게임판 행(세로), 열(가로) 크기
char map[MAXN + 5][MAXN + 5]; //게임판('#':벽, '.':빈공간, 'R':빨간구슬, 'B':파란구슬, 'H':목표구멍)

typedef struct _ball
{
    _ball(int y, int x) : y(y), x(x){};
    int y;
    int x;
} ball;
typedef struct _node
{
    _node(int ry, int rx, int by, int bx, int count)
          : bball(ball(by, bx)), rball(ball(ry, rx)), count(count) {};
    ball bball;
    ball rball;
    int count;
} node;

int dt[][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};

queue<node> Q;

void InputData()
{
    cin >> R >> C;
    for (int i = 0; i < R; i++)
    {
        cin >> map[i];
    }
}
void check_wall(int &ny, int &nx, ball b)
{
    if (map[ny][nx] == WALL)
    {
        ny = b.y;
        nx = b.x;
    }
}

int bfs()
{
    bool visited[MAXN + 5][MAXN + 5][MAXN + 5][MAXN + 5] = {false};
    // visited는 빨간 공 기준으로 방문처리
    while (!Q.empty())
    {
        node n = Q.front();
        Q.pop();
        if (map[n.rball.y][n.rball.x] == GOAL)
        {
            return n.count;
        }
        if (n.count > 10)
        {
            continue;
        }

        for (int i = 0; i < 4; i++)
        {
            int dy = dt[i][1], dx = dt[i][0];
            // 0, R - 1, C - 1 부분은 벽이므로 y, x 는 ((0, R), (0, C)) 범위 안에 항상 있음
            int by = n.bball.y + dy, bx = n.bball.x + dx;
            int ry = n.rball.y + dy, rx = n.rball.x + dx;

            // 벽에 부딪혔는지 각자 테스트
            check_wall(by, bx, n.bball);
            check_wall(ry, rx, n.rball);


            // 방문 / 공 부딪힌 경우 / 파란 공 들어간 경우는 패스
            if ((visited[ry][rx][by][bx])
                || (ry == by && rx == bx)
                || (map[by][bx] == GOAL))
            {
                continue;
            }
            visited[ry][rx][by][bx] = true;
            
            Q.push(node(ry, rx, by, bx, n.count + 1));
        }
    }
    return -1;
}
void initialize()
{
    while (!Q.empty())
    {
       Q.pop(); 
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T, ans = -1;
    cin >> T;
    for (int i = 0; i < T; i++)
    {
        ans = -1;
        InputData(); //입력

        //여기서부터 작성
        // 이전 케이스 사용된 값 초기화
        initialize();
        // 공 위치 찾기
        int by, bx, ry ,rx;
        for (int y = 1; y < R; y++)
        {
            for (int x = 1; x < C; x++)
            {
                if (map[y][x] == BLUE)
                {
                    by = y;
                    bx = x;
                    map[y][x] = EMPTY;
                }
                else if (map[y][x] == RED)
                {
                    ry = y;
                    rx = x;
                    map[y][x] = EMPTY;
                }
            }
        }
        Q.push(node(ry, rx, by, bx, 0));

        ans = bfs();
        cout << ans << "\n"; //출력
    }
    return 0;
}