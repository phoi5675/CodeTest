#include <iostream>
#include <queue>
#include <cstring>

using namespace std;
#define MAXH (12)
#define MAXW (6)

const char R='R', G='G', B='B', P='P', Y='Y';
const char EMPTY='.', BOOM='*';

const int MIN_SELECTED = 4;

int vec[][4] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

char map[MAXH + 2][MAXW + 2];
char new_map[MAXH + 2][MAXW + 2];
bool visited[MAXH + 2][MAXW + 2];
typedef struct _node
{
    _node(int y, int x) : y(y), x(x){};
    int y;
    int x;
} node;
queue<node> Q;
void InputData()
{
    for (int i = 0; i < MAXH; i++)
    {
        cin >> map[i];
    }
}
void init()
{
    memset(new_map, EMPTY, sizeof(new_map));
    memset(visited, false, sizeof(visited));
}

inline void copy_map()
{
    memcpy(map, new_map, sizeof(new_map));
}
void remove_boomed()
{
    for (int x = 0; x < MAXW; x++)
    {
        int boom_in_line = 0;
        int y = MAXH - 1;
        while (y - boom_in_line >= 0)
        {
            while (y - boom_in_line >= 0
                && map[y - boom_in_line][x] == BOOM)
            {
                boom_in_line++;
            }
            new_map[y][x] = map[y - boom_in_line][x];
            y--;
        }
    }
}
bool bfs(int y, int x)
{
    bool is_boomed = false;
    char color = map[y][x];
    int selected = 1;
    Q.push(node(y, x));
    queue<node>boomQ = queue<node>(Q);
    visited[y][x] = true;

    while (!Q.empty())
    {
        node front = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++)
        {
            int ny = front.y + vec[i][0], nx = front.x + vec[i][1];

            if ((0 <= ny && ny < MAXH) && (0 <= nx && nx < MAXW)
                && !visited[ny][nx] && map[ny][nx] == color)
            {
                visited[ny][nx] = true;
                node n = node(ny, nx);
                Q.push(n);
                boomQ.push(n);
            }
        }
    }
    if (boomQ.size() >= MIN_SELECTED)
    {
        is_boomed = true;
        while (!boomQ.empty())
        {
            node n = boomQ.front();
            boomQ.pop();
            map[n.y][n.x] = BOOM;
        }
    }

    return is_boomed;
}
int traverse()
{
    int boomed = 0;
    bool is_boomed = true;
    while (is_boomed)
    {
        is_boomed = false;
        for (int i = MAXH - 1; i >= 0; i--)
        {
            for (int j = MAXW - 1; j >= 0; j--)
            {
                if (map[i][j] != EMPTY && map[i][j] != BOOM && !visited[i][j])
                {
                    if (bfs(i, j))
                    {
                        is_boomed = true;
                    }
                }
            }
        }
        if (is_boomed)
        {
            boomed++;
        }
        // 다음 라운드 위한 맵 세팅
        remove_boomed();    // 터진 부분 빼고 나머지 위에 있던 블록을 아래로 내림
        copy_map();
        memset(new_map, EMPTY, sizeof(new_map));
        memset(visited, false, sizeof(visited));
    }
    return boomed;
}
int main()
{
    int T, t, ans = -1;
    cin >> T;
    for (t = 1; t <= T; t++)
    {
        InputData(); //입력받는 부분

        //여기서부터 작성
        init();
        ans = traverse();
        cout << ans << endl; //출력하는 부분
    }
    return 0;
}
