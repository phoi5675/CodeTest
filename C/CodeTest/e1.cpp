#include <iostream>
#include <queue>
#include <unordered_map>
#include <cstdlib>

using namespace std;
#define MAXN (10000)
#define INF ((int)1e9)
#define DST ('Z')
#define IS_UPPER(n) ('A' <= (n) && (n) <= 'Z' ? 1 : 0)

int P;
char N1[MAXN + 10];
char N2[MAXN + 10];
int L[MAXN + 10];
char farm;
int sol;

typedef struct _node
{
    _node(char farm, char cur_pos, int moved) :
        farm(farm), cur_pos(cur_pos), moved(moved) {};
    char farm;
    char cur_pos;
    int moved;
} node;
unordered_map<char, unordered_map<char, int> > graph;
unordered_map<char, unordered_map<char, int> > visited;
queue<node> Q;
void InputData()
{
    cin >> P;
    char from, to;
    int dist;
    for (int i = 0; i < P; i++)
    {
        cin >> from >> to >> dist;
        if (graph.find(from) != graph.end() 
            && graph[from].find(to) != graph[from].end())
        {
            if (dist < graph[from][to])
            {
                graph[from][to] = dist;
                graph[to][from] = dist;
            }
        }
        else
        {
            if (graph.find(from) == graph.end())
            {
                graph.insert(make_pair(from, unordered_map<char, int>()));
            }
            if (graph.find(to) == graph.end())
            {
                graph.insert(make_pair(to, unordered_map<char, int>()));
            }
            graph[from][to] = dist;
            graph[to][from] = dist;
        }
    }
}
void init()
{
    // visited 초기화
    pair<char, char> lower = make_pair('a', 'z');
    pair<char, char> upper = make_pair('A', 'Z');
    pair<char, char> arr[] = {lower, upper};
    for (int i = 0; i < 2; i++)
    {
        for (char ch = arr[i].first; ch <= arr[i].second; ch++)
        {
            visited.insert(make_pair(ch, unordered_map<char, int>()));
        }
    }
    unordered_map<char, unordered_map<char, int> >::iterator itr;
    for (itr = visited.begin(); itr != visited.end(); itr++)
    {
        for (int i = 0; i < 2; i++)
        {
            for (char ch = arr[i].first; ch <= arr[i].second; ch++)
            {
                (*itr).second[ch] = INF;
            }
        }
    }

    // 그래프에서 있는 소들만 enqueue
    for (char ch = upper.first; ch <= upper.second; ch++)
    {
        if (graph.find(ch) != graph.end())
        {
            if (ch == DST)
            {
                continue;
            }
            Q.push(node(ch, ch, 0));
        }
    }
}
node bfs()
{
    node ret = node('a', 'a', INF);
    while (!Q.empty())
    {
        node n = Q.front();
        Q.pop();

        char from = n.cur_pos;
        // printf("%c %c %d\n", n.farm, n.cur_pos, n.moved);
        unordered_map<char, int>::iterator itr;
        for (itr = graph[from].begin(); itr != graph[from].end(); itr++)
        {
            char to = (*itr).first;
            int dist = (*itr).second;
            int moved = n.moved + dist;
            if (moved < visited[from][to])
            {
                visited[from][to] = moved;
                visited[to][from] = moved;
                node next = node(n.farm, to, moved);
                Q.push(next);
                if (to == DST && moved < ret.moved)
                {
                    ret = next;
                }
            }
        }
    }

    return ret;
}
void debug()
{
    unordered_map<char, unordered_map<char, int> >::iterator itr;
    unordered_map<char, int>::iterator in_itr;
    for (itr =graph.begin(); itr != graph.end(); itr++)
    {
        unordered_map<char, int> dict = (*itr).second;
        printf("%c\t", (*itr).first);
        for (in_itr = dict.begin(); in_itr != dict.end(); in_itr++)
        {
            printf("(%c, %d)\t", (*in_itr).first, (*in_itr).second);
        }
        printf("\n");
    }
}
int main()
{
    
    InputData(); // 입력받는 부분

    // 여기서부터 작성
    init();

    node res = bfs();
    cout << res.farm << " " << res.moved << endl; // 출력하는 부분
    return 0;
}