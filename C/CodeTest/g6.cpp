#include <iostream>
#include <algorithm>
#include <queue>
#include <cstdio>
using namespace std;

int N, M;
int s[100 + 10];
int e[100 + 10];
int in[10 + 10];
int num[10 + 10];
bool graph[10 + 10][10 + 10];

queue<int> Q[10 + 10];
void InputData()
{
    cin >> N >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> s[i] >> e[i];
    }
    for (int i = 0; i < N; i++)
    {
        cin >> in[i];
    }
}
void OutputData()
{
    for (int i = 1; i <= N; i++)
    {
        cout << num[i] << " ";
    }
    cout << endl;
}

void make_graph()
{
    for (int i = 0; i < M; i++)
    {
        graph[s[i]][e[i]] = true;
    }
}
void dfs(int rank, int depth)
{
    for (int i = 1; i <= N; i++)
    {
        if (graph[rank][i])
        {
            dfs(i, depth + 1);
        }
    }
    Q[depth].push(rank);
}
void bfs()
{
    for (int i = 10; i >= 0; i--)
    {
        while (!Q[i].empty())
        {
            int rank = Q[i].front();
            // cout << i << '\t' << rank << endl;
            Q[i].pop();
            // 이미 낮은 랭크에서 방문한 경우 pass
            if (num[rank])
            {
                continue;
            }
            int lower_rank_money = 0;
            for (int lower_rank = 1; lower_rank <= N; lower_rank++)
            {
                // 연결된 부하 직원 중 제일 돈을 많이 받은 직원의 금액 구함
                if (graph[rank][lower_rank])
                {
                    lower_rank_money = max(lower_rank_money, num[lower_rank]);
                }
            }

            for (int m_idx = 0; m_idx < N; m_idx++)
            {
                // 위에서 구한 부하 직원 금액보다 큰 금액 할당
                if (lower_rank_money < in[m_idx])
                {
                    num[rank] = in[m_idx];
                    in[m_idx] = 0;
                    break;
                }
            }
        }
    }
}
void solve()
{
    dfs(1, 0);
    bfs();
}
int main()
{
    InputData(); //입력받는 부분

    // 여기서부터 작성
    sort(in, in + N);  // 오름차순 정렬

    make_graph();
    solve();
    OutputData(); // 출력하는 부분
    return 0;
}