#include <iostream>
#include <algorithm>
#include <list>
#include <vector>
using namespace std;

typedef struct _node
{
    _node(int id, int st, int end) : id(id), st(st), end(end) {};
    int id;
    int st;
    int end;
} node;

int N;
int ID[500 + 10];
int S[500 + 10];
int E[500 + 10];
int sol[500 + 10];
vector<node> table;
list<node> q;

int ans = 0;

bool compare(node first, node second)
{
    if (first.end < second.end)
    {
        return true;
    }
    else if (first.end == second.end)
    {
        return first.id < second.id;
    }
    else
    {
        return false;
    }
}

void InputData()
{
    cin >> N;
    for (int i = 0; i < N; i++)
    {
        cin >> ID[i] >> S[i] >> E[i];
        table.push_back(node(ID[i], S[i], E[i]));
    }
}
void OutputData(int ans)
{
    cout << ans << endl;
    for (int i = 0; i < ans; i++)
    {
        cout << sol[i] << " ";
    }
    cout << endl;
}

int main()
{
    InputData(); // 입력받는 부분

    //여기서부터 작성
    // 시간 / ID 순서로 정렬
    sort(table.begin(), table.end(), compare);

    // debug
    // for (int i = 0; i < N; i++)
    // {
    //     node n = table[i];
    //     cout << n.st << '\t' << n.end << '\t' << n.id << '\n';
    // }
    
    int end = table[0].end;
    sol[ans++] = table[0].id;
    for (int i = 0; i < N; i++)
    {
        if (table[i].st < end)
        {
            continue;
        }
        sol[ans++] = table[i].id;
        end = table[i].end;
    }

    OutputData(ans); // 출력하는 부분
    return 0;
}