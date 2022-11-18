#include <iostream>
using namespace std;
#define MAXN ((int)1e5)
const char L = '(';
const char R = ')';
char str[MAXN + 10];
int prev_l_brk[MAXN + 10];
void InputData()
{
    cin >> str;
}

int solve()
{
    int depth = 0, open = 0, close = 0;
    for (int i = 0; str[i]; i++)
    {
        if (str[i] == L)
        {
            depth++;
            open++;
        }
        else
        {
            depth--;
            close++;
        }
        if (depth == 1)
        {
            open = 0;
        }
        if (depth < 0)
        {
            return close;
        }
    } 
    return open;
}

int main()
{
    int ans = 0;

    InputData(); // 입력받는 부분

    // 여기서부터 작성
    ans = solve();
    cout << ans << endl; // 출력하는 부분
    return 0;
}