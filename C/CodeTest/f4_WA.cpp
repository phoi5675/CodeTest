#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;
char map[5][10];

#define IDX(ch) ((int)(ch) - ('A' + 1));
#define TO_CHAR(idx) ((idx) + ('A' - 1));
#define EMPTY ('x')
#define MAGIC (26)
struct POS
{
    POS(int y, int x) : y(y), x(x) {};
    int y;
    int x;
};
vector<pair<POS, vector<int> > > graph; 
int sum[6];
bool visited[13];
void InputData()
{
    for (int h = 0; h < 5; h++)
    {
        cin >> map[h];
    }
}
void OutputData()
{
    for (int h = 0; h < 5; h++)
    {
        cout << map[h] << endl;
    }
}
int init()
{
    int count = 0;

    graph.push_back({POS(0, 4), {0, 2}});
    graph.push_back({POS(1, 3), {0, 3}});
    graph.push_back({POS(2, 2), {0, 4}});
    graph.push_back({POS(3, 1), {0, 1}});
    graph.push_back({POS(3, 3), {1, 4}});
    graph.push_back({POS(3, 5), {1, 5}});
    graph.push_back({POS(3, 7), {1, 2}});
    graph.push_back({POS(2, 6), {2, 5}});
    graph.push_back({POS(1, 5), {2, 3}});
    graph.push_back({POS(1, 1), {3, 4}});
    graph.push_back({POS(1, 7), {3, 5}});
    graph.push_back({POS(4, 4), {4, 5}});

    vector<pair<POS, vector<int> > >::iterator itr;
    for (itr = graph.begin(); itr != graph.end(); itr++)
    {
        for (int i = 0; i < 2; i++)
        {
            int pos = (*itr).second[i];
            int y = (*itr).first.y;
            int x = (*itr).first.x;

            if (map[y][x] != EMPTY)
            {
                printf("%d %d %c\n", y, x, map[y][x]);
                int idx = IDX(map[y][x]);
                sum[pos] += idx;
                visited[idx] = true;
            }
        }
    }
    for (int i = 1; i <= 12; i++)
    {
        if (visited[i])
        {
            count++;
        }
    }
    return count;
}

bool is_magic_able(int idx, vector<int> pos)
{
    for (int i = 0; i < 2; i++)
    {
        if (sum[pos[i]] + idx > MAGIC)
        {
            return false;
        }
    }
    return true;
}
bool dfs(int idx)
{
    if (idx == 12)
    {
        for (int i = 0; i < 6; i++)
        {
            if (sum[i] != MAGIC)
            {
                return false;
            }
        }
        return true;
    }
    for (int i = 1; i <= 12; i++)
    {
        vector<pair<POS, vector<int> > >::iterator itr;
        for (itr = graph.begin(); itr != graph.end(); itr++)
        {
            int y = (*itr).first.y;
            int x = (*itr).first.x;
            if (map[y][x] != EMPTY)
            {
                continue;
            }
            bool is_able = is_magic_able(i, (*itr).second);
            if (is_able)
            {
                vector<int> pos = (*itr).second;
                for (int j = 0; j < 2; j++)
                {
                    sum[pos[j]] += i;
                }
                map[y][x] = TO_CHAR(i);
                visited[i] = true;
                if (dfs(idx + 1))
                {
                    return true;
                }
                map[y][x] = EMPTY;
                visited[i] = false;
            }

        }
    }
    return false;
}

int main()
{
    InputData(); //입력받는 부분

    //여기서부터 작성
    int idx = init();
    for (int i = 0; i < 6; i++)
    {
        printf("%3d ", sum[i]);
    }
    printf("\n");

    dfs(idx);
    OutputData(); //출력하는 부분
    return 0;
}