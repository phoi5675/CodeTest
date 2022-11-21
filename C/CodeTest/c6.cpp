#include <iostream>
#include <string>
#include <deque>

using namespace std;

#define MAX_N (300000)
#define MAX_NAME (25)
int N, K;
string name[MAX_N + 10];
deque<int> name_stack[MAX_NAME];

void Input_Data(void)
{
    string str;
    cin >> N >> K;
    for (int i = 0; i < N; i++)
    {
        cin >> name[i];
    }
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    long long sol = -1;

    // 입력 받는 부분
    Input_Data();

    // 여기서부터 작성
    // 두 사람의 이름 길이가 같은 경우 -> Best
    sol = 0;
    for (int i = 0; i < N; i++)
    {
        int name_idx = name[i].length();
        // K 보다 거리 긴 친구들 제거
        while (!name_stack[name_idx].empty() &&
            i - name_stack[name_idx].front() > K)
        {
            name_stack[name_idx].pop_front();
        }
        sol += name_stack[name_idx].size();
        name_stack[name_idx].push_back(i);
    }
    // 출력하는 부분
    cout << sol << '\n';

    return 0;
}