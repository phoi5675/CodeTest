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
    _node(int y, int x, int moves) : y(y), x(x), moves(moves) {};
    int y;
    int x;
    int moves;
} node;

queue<node> floodQ;
queue<node> next_floodQ;
queue<node> artistQ;
queue<node> next_artistQ;

void debug(node artist)
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (i == artist.y && j == artist.x)
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
    while (!floodQ.empty())
    {
        floodQ.pop();
    }
    while (!next_floodQ.empty())
    {
        next_floodQ.pop();
    }
    while (!artistQ.empty())
    {
        artistQ.pop();
    }
    while (!next_artistQ.empty())
    {
        next_artistQ.pop();
    }
    memset(visited, 0, sizeof(visited));
}

void fill_init_queue()
{
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++)
        {
            if (map[i][j] == ART)
            {
                artistQ.push(node(i, j, 0));
                map[i][j] = EMPTY;
                visited[i][j] = true;
            }
            else if (map[i][j] == FLOOD)
            {
                next_floodQ.push(node(i, j, 0));
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
    while (!artistQ.empty())
    {
        // debug(artistQ.front());

        // 홍수 먼저 발생
        while (!floodQ.empty())
        {
            node flood = floodQ.front();
            floodQ.pop();

            for (int i = 0; i < 4; i++)
            {
                int ny = vec[i][0] + flood.y;
                int nx = vec[i][1] + flood.x;

                if (is_in_boundary(ny, nx) && map[ny][nx] == EMPTY)
                {
                    map[ny][nx] = FLOOD;
                    next_floodQ.push(node(ny, nx, 0));
                }
            }
        }

        // 홍수가 먼저 visited 처리를 하므로 동시에 화가와 홍수가 도착하는지 검사 필요 없음
        while (!artistQ.empty())
        {
            node artist = artistQ.front();
            artistQ.pop();

            if (map[artist.y][artist.x] == CAVE)
            {
                return artist.moves;
            }
            for (int i = 0; i < 4; i++)
            {
                int ny = vec[i][0] + artist.y;
                int nx = vec[i][1] + artist.x;

                if (is_in_boundary(ny, nx) && !visited[ny][nx] 
                    && (map[ny][nx] == CAVE || map[ny][nx] == EMPTY))
                {
                    visited[ny][nx] = true;
                    next_artistQ.push(node(ny, nx, artist.moves + 1));
                }
            }
        }

        floodQ = next_floodQ;
        next_floodQ = queue<node>();
        artistQ = next_artistQ;
        next_artistQ = queue<node>();
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
        fill_init_queue();

        ans = bfs();
        if (ans == -1)
            cout << "KAKTUS" << endl; //출력 하는 부분
        else
            cout << ans << endl;
    }
    return 0;
}
