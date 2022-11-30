#include <iostream>
#include <cstring>
#include <deque>
#include <cstdio>

using namespace std;
#define MAXN (100)
struct node
{
    node(int y, int x, int vec) : y(y), x(x), vec(vec) {};
    int y, x, vec;
};
int dt[][2] = {{-1, 0}, {0, -1}, {1, 0}, {0, 1}};   // U, L, D, R
const char LEFT = 'L', RIGHT = 'D';
const char FRUIT = '*', SNAKE = 'o', EMPTY = '.';
int N;
int K;
int L;
int X[MAXN + 10];
char CMD[MAXN + 10];
char map[MAXN + 10][MAXN + 10];
deque<node> Q;
void InputData()
{
    cin >> N;
    cin >> K;
    for (int i = 0; i < K; i++)
    {
        int R, C;
        cin >> R >> C;
        map[R][C] = FRUIT;
    }
    cin >> L;
    for (int i = 0; i < L; i++)
    {
        cin >> X[i] >> CMD[i];
    }
}
int change_vec(int cur_vec, char turn_to)
{
    if (turn_to == LEFT)
    {
        return (cur_vec + 1) % 4;
    }
    else
    {
        return (cur_vec + 3) % 4;
    }
}
inline bool is_in_map(int y, int x)
{
    return (1 <= y && y <= N) && (1 <= x && x <= N);
}
void debug()
{
    cout << endl;
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N; j++)
        {
            printf("%c", map[i][j]);
        }
        cout << endl;
    }
}
int bfs()
{
    int elapsed = 0;
    bool is_game_over = false;
    int cmd_idx = 0;

    while (!is_game_over)
    {
        // debug();
        node head = Q.back();
        int ny = head.y + dt[head.vec][0], nx = head.x + dt[head.vec][1];
        elapsed++;
        if (!is_in_map(ny, nx) || (is_in_map(ny, nx) && map[ny][nx] == SNAKE))
        {
            is_game_over = true;
            return elapsed;
        }

        // 다음 방향 전환 계산
        if (cmd_idx < L && elapsed == X[cmd_idx])
        {
            head.vec = change_vec(head.vec, CMD[cmd_idx++]);
        }
        // 이동 후 사과 먹기
        Q.push_back(node(ny, nx, head.vec));
        // 사과 아닌 경우에는 꼬리 삭제
        if (map[ny][nx] != FRUIT)
        {
            node tail = Q.front();
            Q.pop_front();
            map[tail.y][tail.x] = EMPTY;
        }
        map[ny][nx] = SNAKE;
    }
    return elapsed;
}
int main()
{
    int ans = -1;
    memset(map, EMPTY, sizeof(map));
    InputData(); //입력받는 부분

    //여기서부터 작성
    Q.push_back(node(1, 1, 3));
    ans = bfs();
    cout << ans << endl; //출력하는 부분
    return 0;
}