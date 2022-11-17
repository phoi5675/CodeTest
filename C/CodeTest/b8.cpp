// https://www.acmicpc.net/problem/8980
#include <iostream>
#include <algorithm>
using namespace std;

typedef struct _node
{
    int from;
    int to;
    int loads;
} node;

int N, C, M;
int towns[2000 + 10];
node table[10000 + 10];
bool compare(node first, node second)
{
   if (first.to == second.to)
   {
        return first.from < second.from;
   } 
   else
   {
        return first.to < second.to;
   }
}
void InputData()
{
    cin >> N >> C;
    cin >> M;
    for (int i = 0; i < M; i++)
    {
        cin >> table[i].from >> table[i].to >> table[i].loads;
    }
}

int main()
{
    int ans = 0;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    sort(table, table + M, compare);

    // debug
    // for (int i = 0; i < M; i++)
    // {
    //     cout << table[i].from << '\t' << table[i].to << '\t' << table[i].loads << '\n';
    // }

    // 각 마을에서 실을 수 있는 짐 용량 초기화
    for (int i = 0; i < N; i++)
    {
        towns[i] = C;
    }
    for (int i = 0; i < M; i++)
    {
        int max_capacity = C;
        int loaded = 0;
        // 해당 구간에서 가져갈 수 있는 최대 짐 용량 계산(해당 구간에서 이미 사용된 공간 제외하기)
        for (int t = table[i].from; t < table[i].to; t++)
        {
            max_capacity = min(max_capacity, towns[t]);
        } 
        // 가져갈 수 있는 최대 용량과 실을려고 하는 용량 비교 -> 실을 수 있는 용량 계산
        if (max_capacity >= table[i].loads)
        {
            loaded = table[i].loads;
        }
        else if (0 < max_capacity && max_capacity < table[i].loads)
        {
            loaded = max_capacity;
        }
        // 각 마을에 실은 짐 무게 감소
        for (int t = table[i].from; t < table[i].to; t++)
        {
            towns[t] -= loaded;
        }
        ans += loaded;
    }
    cout << ans << endl; // 출력하는 부분
    return 0;
}
