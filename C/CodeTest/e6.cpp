#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstdio>

using namespace std;

#define MAXN (50)
int N, M, K; //철도역수, 철도수, 추가로 연결시킬수있는 철도수
int ans;

bool graph[MAXN + 10][MAXN + 10];
bool visited[MAXN + 10];
bool conn_visited[MAXN + 10];
bool has_vertex[MAXN + 10];
vector<int> connected;
queue<int> Q;
void InputData()
{
    cin >> N >> M >> K;
    for (int i = 0; i < M; i++)
    {
        int edge1, edge2;
        cin >> edge1 >> edge2;
        graph[edge1][edge2] = true;
        graph[edge2][edge1] = true;

        has_vertex[edge1] = true;
        has_vertex[edge2] = true;
    }
}

bool compare(int first, int second)
{
    return first > second;
}

int bfs(int edge)
{
    int connected_edges = 1;
    Q.push(edge);
    visited[edge] = true;

    while (!Q.empty())
    {
        int cur_edge = Q.front();
        Q.pop();

        for (int i = 1; i <= MAXN; i++)
        {
            if (i == cur_edge || visited[i])
            {
                continue;
            }
            if (graph[cur_edge][i])
            {
                visited[i] = true;
                Q.push(i);
                connected_edges++;
            }
        }
    }
    return connected_edges;
}

int main()
{
    InputData(); //입력받는 부분

    // 여기서부터 작성
    // 도시 클러스터링
    for (int i = 1; i <= MAXN; i++)
    {
        if (visited[i] || !has_vertex[i])
        {
            continue;
        }
        connected.push_back(bfs(i));
    }

    // 추가 철도 연결 -> 그리디하게 큰 도시들부터 연결
    sort(connected.begin(), connected.end(), compare);

    int rail_added = 0;
    for (int i = 0; i < connected.size(); i++)
    {
        // 연결된 도시 개수 == 놓인 철도 개수 + 1이므로 1 offset
        if (rail_added == K + 1)
        {
            break;
        }
        ans += connected[i];
        rail_added++;
    }

    cout << ans << "\n"; // 출력하는 부분
    return 0;
}
