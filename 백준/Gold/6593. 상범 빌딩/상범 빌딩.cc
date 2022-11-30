#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

#define MAX_SIZE (30)

const char START = 'S', EXIT = 'E', WALL = '#', EMPTY = '.';
const int dt[][3] = 
{
    {0, 0, 1}, {0, 0, -1}, {0, 1, 0}, {0, -1, 0}, {1, 0, 0}, {-1, 0, 0}
};
struct node
{
    node(int l, int r, int c, int moved) : l(l), r(r), c(c), moved(moved) {};
    int l, r, c, moved;
};
int L, R, C;
char map[MAX_SIZE + 10][MAX_SIZE + 10][MAX_SIZE + 10];
bool visited[MAX_SIZE + 10][MAX_SIZE + 10][MAX_SIZE + 10];
queue<node> Q;

bool is_in_range(int l, int r, int c)
{
    return (0 <= l && l < L) && (0 <= r && r < R) && (0 <= c && c < C);
}
bool InputData()
{
    cin >> L >> R >> C;
    if ((L == 0) && (R == 0) && (C == 0))
        return false;
    for (int l = 0; l < L; l++)
    {
        for (int r = 0; r < R; r++)
        {
            cin >> map[l][r];
        }
    }
    return true;
}
void init(int &ans)
{
    ans = -1;
    Q = queue<node>();
    memset(visited, false, sizeof(visited));
}
int bfs(node start_node)
{
    Q.push(start_node);

    while (!Q.empty())
    {
        node front = Q.front();
        Q.pop();

        for (int i = 0; i < 6; i++)
        {
            int dl = dt[i][0], dr = dt[i][1], dc = dt[i][2];
            int nl = front.l + dl, nr = front.r + dr, nc = front.c + dc;
            if (is_in_range(nl, nr, nc) && map[nl][nr][nc] != WALL
                && !visited[nl][nr][nc])
            {
                visited[nl][nr][nc] = true;
                Q.push(node(nl, nr, nc, front.moved + 1));
                if (map[nl][nr][nc] == EXIT)
                {
                    return front.moved + 1;
                }
            }
        }
    }
    return -1;
}
node find_start_point()
{
    for (int l = 0; l < L; l++)
    {
        for (int r = 0; r < R; r++)
        {
            for (int c = 0; c < C; c++)
            {
                if (map[l][r][c] == START)
                {
                    visited[l][r][c] = true;
                    return node(l, r, c, 0);
                }
            }
        }
    }
    return node(-1, -1, -1, -1);
}
int main()
{
    int ans = -1;
    while (InputData())
    {

        //여기서부터 작성
        init(ans);
        ans = bfs(find_start_point());
        if (ans == -1)
            cout << "Trapped!" << endl;
        else
            cout << "Escaped in " << ans << " minute(s)." << endl;
    }
    return 0;
}