#include <iostream>
#include <string>
#include <deque>

using namespace std;

string str;
string boom;
deque<char> check_queue;
deque<char> res;

void InputData()
{
    cin >> str;
    cin >> boom;
}
bool solve()
{
    bool is_boomed = false;
    int bomb_idx = 0;

    for (int i = 0; i < res.size(); i++)
    {
        check_queue.push_back(res[i]);
        // 문자열이 일치하는지 확인
        // if-else 를 사용하는 경우, CC44처럼 중복되는 경우를 잡을 수 없음
        // C"C" 부분에서 C != bomb_idx[1] -> C != 4로 bomb_idx = 0으로 초기화되기 때문
        if (check_queue.back() != boom[bomb_idx])
        {
            bomb_idx = 0;
        }
        if (check_queue.back() == boom[bomb_idx])
        {
            bomb_idx++;
        }

        // bomb_idx 가 폭탄 str 의 길이와 같아진 경우, 일치하는 문장을 찾은 것을 의미
        if (bomb_idx == boom.size())
        {
            for (int j = 0; j < boom.size(); j++)
            {
                check_queue.pop_back();
            }
            is_boomed = true;
            bomb_idx = 0;
        }
    }
    return is_boomed;
}

int main(void)
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    InputData();
    // res dqeue로 문자열 복사
    for (int i = 0; i < str.size(); i++)
    {
        res.push_back(str[i]);
    }

    bool is_boomed = true;
    while (is_boomed)
    {
        is_boomed = solve();
        // 문자열 deque 비운 후 완성된 문자열 복사
        res = check_queue;
        check_queue = deque<char>();
    }

    if (res.empty())
    {
        cout << "FRULA\n";
    }
    else
    {
        deque<char>::iterator itr;
        for (itr = res.begin(); itr != res.end(); itr++)
        {
            cout << (*itr);
        }
        cout << '\n';
    }
    return 0;
}
