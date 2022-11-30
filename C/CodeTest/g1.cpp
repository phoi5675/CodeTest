#include <iostream>
#include <queue>
using namespace std;
#define MAXN (1000)
int A, B, C, D;
bool visited[MAXN + 10][MAXN + 10];
struct node
{
    node(int a, int b, int elapsed) : a(a), b(b), elapsed(elapsed) {};
    int a, b, elapsed;
};
queue<node> Q;
void InputData()
{
    cin >> A >> B >> C >> D;
}
int bfs()
{
    int tmp_a, tmp_b;
    while (!Q.empty())
    {
        node n = Q.front();
        Q.pop();
        if (n.a == C && n.b == D)
        {
            return n.elapsed;
        }
        int a_left = A - n.a, b_left = B - n.b;
        // 왼쪽 버림
        if (!visited[0][n.b])
        {
            visited[0][n.b] = true;
            Q.push(node(0, n.b, n.elapsed + 1));
        }
        // 오른쪽 버림
        if (!visited[n.a][0])
        {
            visited[n.a][0] = true;
            Q.push(node(n.a, 0, n.elapsed + 1));
        }
        // 왼쪽 -> 오른쪽
        if (n.a <= b_left)
        {
            tmp_b = n.b + n.a;
            if (!visited[0][tmp_b])
            {
                visited[0][tmp_b] = true;
                Q.push(node(0, tmp_b, n.elapsed + 1));
            }
        }
        else
        {
            tmp_b = B;
            tmp_a = n.a - b_left;
            if (!visited[tmp_a][tmp_b])
            {
                visited[tmp_a][tmp_b] = true;
                Q.push(node(tmp_a, tmp_b, n.elapsed + 1));
            }
        }
        // 오른쪽 -> 왼쪽
        if (n.b <= a_left)
        {
            tmp_a = n.a + n.b;
            if (!visited[tmp_a][0])
            {
                visited[tmp_a][0] = true;
                Q.push(node(tmp_a, 0, n.elapsed + 1));
            }
        }
        else
        {
            tmp_a = A;
            tmp_b = n.b - a_left;
            if (!visited[tmp_a][tmp_b])
            {
                visited[tmp_a][tmp_b] = true;
                Q.push(node(tmp_a, tmp_b, n.elapsed + 1));
            }
        }
        // 왼쪽 채움
        if (!visited[A][n.b])
        {
            visited[A][n.b] = true;
            Q.push(node(A, n.b, n.elapsed + 1));
        }
        // 오른쪽 채움
        if (!visited[n.a][B])
        {
            visited[n.a][B] = true;
            Q.push(node(n.a, B, n.elapsed + 1));
        }
    }
    return -1;
}
int main()
{
    int ans = -2;
    InputData(); //입력받는 부분

    // 여기서부터 작성
    Q.push(node(0, 0, 0));
    visited[0][0] = true;
    ans = bfs();
    cout << ans << "\n"; // 출력하는 부분
    return 0;
}