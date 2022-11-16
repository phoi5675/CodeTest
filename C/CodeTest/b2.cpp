#include <iostream>
using namespace std;

const char OPEN = '(';
const char CLOSE = ')';
char str[100000 + 10];
void InputData()
{
    cin >> str;
}

int main()
{
    int ans = 0;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    int pair_checker = 0;
    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == OPEN)
        {
            pair_checker++;
        }
        else
        {
            pair_checker--;
        }

        // CLOSE 짝이 남는 경우에는 해당 괄호 방향 바꿔줘야 함
        if (pair_checker < 0)
        {
            ans++;
            // 방향 바꾸고(+1), '(' 개수 세는 것(+1) 해서 총 +2로 계산
            pair_checker += 2;
        }
    }

    // 남은 짝 없는 괄호 처리
    if (pair_checker > 0)
    {
        if (pair_checker == 1)
        {
            ans++;
        }
        else
        {
            ans += (pair_checker / 2);
        }
    }
    else if (pair_checker < 0)
    {
        ans -= pair_checker;
    }

    cout << ans << endl; // 출력하는 부분
    return 0;
}
