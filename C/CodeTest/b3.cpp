#include <iostream>
#include <queue>

using namespace std;

#define MAXN (100)

const int PAPER_LEN = 10;
int vec[][2] = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

typedef struct _node
{
    _node(int y, int x) : y(y), x(x) {};
    int y;
    int x;
} node;

int N;
int A[MAXN + 10];
int B[MAXN + 10];

bool visited[MAXN + 10][MAXN + 10];
bool paper_map[MAXN + 10][MAXN + 10];
queue<node> q;
void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> A[i] >> B[i];
    }
}

int bfs(int y, int x)
{
    int border_len = 0;
    q.push(node(y, x));
    visited[y][x] = true;

    while (!q.empty())
    {
        node n = q.front();
        q.pop();

        for (int i = 0; i < 4; i++)
        {
            int dy = vec[i][0], dx = vec[i][1];
            int ny = n.y + dy, nx = n.x + dx;

            // 색종이의 모서리 부분인 경우
            if ((0 < ny && ny < MAXN) && (0 < nx && nx < MAXN) && !visited[ny][nx])
            {
                // 색종이 부분만 탐색 종료를 위해 visited 변경
                if (paper_map[ny][nx])
                {
                    visited[ny][nx] = true;
                    q.push(node(ny, nx));
                }
                else
                {
                    border_len++;
                }
            }
            // 색종이의 모서리지만, 도화지의 경계선에 있는 경우
            // 색종이는 도화지 밖으로 나가지 않으므로, 도화지 경계선에 있는 경우 == 색종이 모서리
            else if (ny == 0 || ny == MAXN || nx == 0 || nx == MAXN)
            {
                border_len++;
            }
        }
    }

    return border_len;
}

int main()
{
    int ans = 0;
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    // 도화지 칠하기
    for (int i = 0; i < N; i++)
    {
        int x = A[i], y = B[i];
        for (int j = 0; j < 10; j++)
        {
            for (int k = 0; k < 10; k++)
            {
                paper_map[y + j][x + k] = true;
            }
        }
    }

    for(int i = 0; i <= MAXN; i++)
    {
        for (int j = 0; j <+ MAXN; j++)
        {
            if (paper_map[i][j] && !visited[i][j])
            {
                ans += bfs(i, j);
            }
        }
    }

    cout << ans << endl; // 출력하는 부분
    return 0;
}
