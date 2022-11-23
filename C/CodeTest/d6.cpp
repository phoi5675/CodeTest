#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define VISITED (0)

typedef struct _node
{
    _node(int idx, int pos, int moves) :
        idx(idx), pos(pos), moves(moves) {};
    int idx;
    int pos;
    int moves;
} node;
vector<int> minors;
queue<node> Q;
int S, E; //출발 정류장 번호, 도착 정류장 번호

void InputData()
{
    cin >> S >> E;
}
bool is_minor(int num)
{
    if ((num % 2) == 0)
    {
        return false;
    }
    else
    {
        int div = num / 2;
        for (int i = 3; i < div; i++)
        {
            if (num % i == 0)
            {
                return false;
            }
        }
    }
    return true;
}
void get_minors()
{
    for (int i = 1000; i < 10000; i++)
    {
        if (is_minor(i))
        {
            minors.push_back(i);
        }
    }
}

int find_idx(int num)
{
    for (int i = 0; i < minors.size(); i++)
    {
        if (minors[i] == num)
        {
            return i;
        }
    }
    return -1;
}
bool is_nearby(int p1, int p2)
{
    int dist = 0;
    
    for (int div = 1000; div > 0; div /= 10)
    {
        int q1 = p1 / div, q2 = p2 / div;
        p1 -= (q1 * div);
        p2 -= (q2 * div);
        if (q1 != q2)
        {
            dist++;
        }
        if (dist > 1)
        {
            return false;
        }
    }
    return dist == 1;
}

int bfs(int start, int end)
{
   while (!Q.empty())
    {
        node n = Q.front();
        Q.pop();

        // cout << n.idx << '\t' << n.pos << '\t' << n.moves << endl;
        if (n.pos == end)
        {
            return n.moves;
        }
        for (int i = 0; i < minors.size(); i++)
        {
            if (minors[i] == VISITED)
            {
                continue;
            }
            if (is_nearby(n.pos, minors[i]))
            {
                // cout << n.idx << '\t' << n.pos << '\t' << minors[i] << '\t' << n.moves << endl;
                Q.push(node(i, minors[i], n.moves + 1));
                minors[i] = VISITED;
            }
        }
    }
    return -1;
}
int main()
{
    int ans = -1;
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    int start = S, end = E;
    // 소수 구하기
    get_minors();
    // cout << minors.size() << '\t' << start << '\t' << end << endl;
    int start_idx = find_idx(start);
    minors[start_idx] = VISITED;
    Q.push(node(start_idx, start, 0));

    ans = bfs(start, end);
    cout << ans << endl; // 출력하는 부분
    return 0;
}