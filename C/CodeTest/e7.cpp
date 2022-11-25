#include <iostream>
#include <algorithm>
#include <queue>

#include <cstdlib>
#include <cstring>
using namespace std;

#define MAXN (500)
#define POW_MAX ((int)1e6)
int N;
int grids[MAXN + 10][MAXN + 10];
bool visited[MAXN + 10][MAXN + 10];
const int dt[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
typedef struct _node
{
    _node(int y, int x) : y(y), x(x) {};
    int y;
    int x;
} node;
queue<node> Q;
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> grids[i][j];
        }
    }
}
int bfs(int y, int x, int tractor)
{
    int covered = 1;
    visited[y][x] = true;
    Q.push(node(y, x));

    while (!Q.empty())
    {
        node front = Q.front();
        Q.pop();

        for (int i = 0; i < 4; i++)
        {
            int ny = front.y + dt[i][0], nx = front.x + dt[i][1];
            if ((0 <= ny && ny < N) && (0 <= nx && nx < N) && !visited[ny][nx]
                && abs(grids[front.y][front.x] - grids[ny][nx]) <= tractor)
            {
                visited[ny][nx] = true;
                covered++;
                Q.push(node(ny, nx));
            }
        }
    }
    return covered;
}
int traverse(int tractor)
{
    int covered = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (!visited[i][j])
            {
                covered = max(covered, bfs(i, j, tractor));
            }
        }
    }
    return covered;
}
int search(int minimum_area)
{
    int covered_area;
    int left = 0, right = POW_MAX;
    int mid;
    int ret = 0;
    while (left <= right)
    {
        mid = (left + right) / 2;
        covered_area = traverse(mid);
        // printf("area : %d\t power : %d\n", covered_area, mid);
        if (covered_area >= minimum_area)
        {
            ret = mid;
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
        memset(visited, false, sizeof(visited));
    }
    return ret;
}
int main()
{
    int ans = -1;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    int minimum_area = ((N * N) / 2) + ((N * N) % 2);
    ans = search(minimum_area);
    cout << ans << endl; // 출력하는 부분
    return 0;
}